from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QImage
import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.executors import SingleThreadedExecutor
from sensor_msgs.msg import Image


class CameraSubscriberThread(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def __init__(self, target_label):
        super().__init__()
        self.target_label = target_label
        self._active = False
        self._node = None
        self._executor = None

    def run(self):
        self._node = rclpy.create_node('camera_subscriber')
        self._executor = SingleThreadedExecutor()
        self._executor.add_node(self._node)
        self._bridge = CvBridge()
        self._active = True

        self._node.create_subscription(Image,'image_raw',self._image_callback,10)

        try:
            while self._active:
                self._executor.spin_once(timeout_sec=0.001)
        finally:
            self._shutdown()

    def _image_callback(self, msg):
        try:
            print("[SUB] Received image")
            frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            scaled = qimg.scaled(self.target_label.size(), Qt.KeepAspectRatio)
            self.ImageUpdate.emit(scaled)
        except Exception as e:
            print(f"[CameraSubscriber] Failed to process image: {e}")

    def stop(self):
        self._active = False
        self.quit()
        self.wait()

    def _shutdown(self):
        if self._executor:
            self._executor.shutdown()
        if self._node:
            self._node.destroy_node()
        rclpy.shutdown()
