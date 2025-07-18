from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer, QRectF

import yaml
import math
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped, PoseStamped
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from std_msgs.msg import Float32MultiArray
import threading

class MapGuiNode(Node):
    def __init__(self):
        super().__init__('map_gui_node')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.pose_pub = self.create_publisher(Float32MultiArray, 'gui_robot_pose', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        self.timer = self.create_timer(0.1, self.publish_pose)  # Cập nhật mỗi 100ms

    def odom_callback(self, msg):
        self.last_odom = msg

    def publish_pose(self):
        if not hasattr(self, 'last_odom'):
            return
        try:
            transform = self.tf_buffer.lookup_transform(
                "odom",
                "base_link",
                rclpy.time.Time()
            )
            x = transform.transform.translation.x
            y = transform.transform.translation.y
            q = transform.transform.rotation
            siny_cosp = 2 * (q.w * q.z + q.x * q.y)
            cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
            theta = math.degrees(math.atan2(siny_cosp, cosy_cosp))
            pose_msg = Float32MultiArray()
            pose_msg.data = [x, y, theta]
            self.pose_pub.publish(pose_msg)
        except Exception as e:
            self.get_logger().info(f"❌ Lỗi tra cứu transform: {e}")

class MapGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.zoom_factor = 1.25

    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)

class LocationTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.map_scene = QGraphicsScene()

        layout = self.ui.view_map.parent().layout()
        self.ui.view_map.setParent(None)

        self.ui.view_map = MapGraphicsView()
        layout.addWidget(self.ui.view_map)
        self.ui.view_map.setScene(self.map_scene)

        self.load_map("Reception_Robot_GUI/resources/Map/map_2.png")

        # Tạo robot
        triangle = QPolygonF([
            QPointF(0, -4),
            QPointF(2, 5),
            QPointF(-2, 5)
        ])
        self.robot_item = QGraphicsPolygonItem(triangle)
        self.robot_item.setBrush(QBrush(QColor(101, 230, 248)))
        self.robot_item.setPen(QPen(Qt.GlobalColor.black, 1))
        self.robot_item.setTransformOriginPoint(0, 0)
        self.map_scene.addItem(self.robot_item)

        # Lưu trữ vị trí mới nhất
        self.last_position = [0.0, 0.0, 0.0]

        # Khởi động node ROS2
        self.start_ros_node()

        # Thiết lập QTimer để cập nhật GUI định kỳ
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_robot_gui)
        self.update_timer.start(100)  # Cập nhật mỗi 100ms (10 Hz)

    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print(f"❌ Không thể load bản đồ: {path}")
            return
        
        # Thêm ảnh vào scene và giữ lại object
        self.map_item = self.map_scene.addPixmap(pixmap)

        # Gán sceneRect đúng với kích thước ảnh (ảnh gốc là đơn vị pixel)
        self.map_scene.setSceneRect(0, 0, pixmap.width(), pixmap.height())
        
        # Lấy kích thước của view để tính scale
        view_size = self.ui.view_map.viewport().size()
        scale_x = view_size.width() / pixmap.width()
        scale_y = view_size.height() / pixmap.height()
        scale = min(scale_x+2, 2+scale_y)

        # Scale thủ công
        self.ui.view_map.resetTransform()
        self.ui.view_map.scale(scale, scale)

        # Lưu thông tin ảnh
        self.map_width = pixmap.width()
        self.map_height = pixmap.height()


        # Đọc thông số từ file map.yaml từ SLAM
        yaml_path = "Reception_Robot_GUI/resources/Map/map_2.yaml"
        try:
            with open(yaml_path, 'r') as file:
                map_config = yaml.safe_load(file)
                self.map_resolution = map_config['resolution']
                self.map_origin = (map_config['origin'][0], map_config['origin'][1])
                print(f"Loaded YAML: resolution={self.map_resolution}, origin={self.map_origin}, "
                      f"map_width={self.map_width}, map_height={self.map_height}")
        except Exception as e:
            print(f"❌ Lỗi khi đọc file map.yaml: {e}")
            self.map_resolution = 0.05  # Giá trị mặc định nếu không đọc được
            self.map_origin = (-1.38, -2.4)  # Giá trị mặc định

    def start_ros_node(self):
        self.node = MapGuiNode()
        self.subscription = self.node.create_subscription(
            Float32MultiArray,
            'gui_robot_pose',
            self.pose_callback,
            10
        )
        self.executor = MultiThreadedExecutor()
        self.executor.add_node(self.node)
        self.ros_thread = threading.Thread(target=self.run_executor, daemon=True)
        self.ros_thread.start()

    def run_executor(self):
        """Chạy executor trong thread riêng"""
        try:
            self.executor.spin()
        except Exception as e:
            print(f"❌ Lỗi trong executor: {e}")

    def closeEvent(self, event):
        """Dọn dẹp khi đóng cửa sổ"""
        print("Đóng cửa sổ, dọn dẹp tài nguyên...")
        self.executor.shutdown()
        self.node.destroy_node()
        rclpy.shutdown()
        event.accept()

    def pose_callback(self, msg):
        """Callback nhận pose từ node ROS"""
        self.last_position = msg.data

    def update_robot_gui(self):
        """Cập nhật vị trí robot trên GUI"""
        x, y, theta = self.last_position
        # Chuyển đổi tọa độ từ /map sang GUI với ảnh xoay 90 độ
        px_raw = (y - self.map_origin[1]) / self.map_resolution  # y của map thành x của Qt
        py_raw = (x - self.map_origin[0]) / self.map_resolution  # x của map thành y của Qt
        # Điều chỉnh cho Qt và ảnh xoay 90 độ
        px = self.map_width - px_raw
        py = self.map_height - py_raw
        # Tính phạm vi hợp lệ dựa trên kích thước bản đồ
        map_max_x = self.map_width
        map_max_y = self.map_height
        # Giới hạn tọa độ trong kích thước bản đồ
        px = max(0, min(px, map_max_x))
        py = max(0, min(py, map_max_y))
        #print(f"[SIM] x={x:.2f}, y={y:.2f}, px_raw={px_raw:.1f}, py_raw={py_raw:.1f}, "f"px={px:.1f}, py={py:.1f}, θ={theta:.1f}")
        self.robot_item.setPos(px, py)
        self.robot_item.setRotation(-theta)  # Giữ nguyên theta
