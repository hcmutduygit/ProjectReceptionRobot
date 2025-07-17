# Robot Data Monitor

## Overview
The Robot Data Monitor package is designed to monitor and evaluate the quality of sensor data and overall system health for robotic systems. It provides real-time monitoring of various sensors including laser scanners, cameras, and odometry data.

## Features
- Real-time sensor data quality evaluation
- System health monitoring and scoring
- Configurable thresholds and parameters
- ROS-based architecture for easy integration
- Support for multiple sensor types:
  - Laser scanner (LaserScan)
  - Camera (Image)
  - Odometry (nav_msgs/Odometry)
  - Command velocity monitoring

## Package Structure
```
robot_data_monitor/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── monitor.launch
├── include/
│   └── robot_data_monitor/
│       └── DataEvaluator.h
├── src/
│   ├── DataEvaluator.cpp
│   └── monitor_node.cpp
└── README.md
```

## Dependencies
- roscpp
- rospy
- std_msgs
- sensor_msgs
- geometry_msgs
- nav_msgs

## Installation
1. Clone this package into your catkin workspace:
```bash
cd ~/catkin_ws/src
git clone <repository_url>
```

2. Build the package:
```bash
cd ~/catkin_ws
catkin_make
```

3. Source the workspace:
```bash
source devel/setup.bash
```

## Usage

### Launch the monitor node
```bash
roslaunch robot_data_monitor monitor.launch
```

### Run the node directly
```bash
rosrun robot_data_monitor robot_data_monitor_node
```

## Configuration Parameters
The following parameters can be configured in the launch file or via rosparam:

- `timeout_threshold` (default: 1.0): Maximum time (seconds) before considering sensor data stale
- `min_data_quality` (default: 0.5): Minimum acceptable data quality score (0.0 to 1.0)
- `status_topic` (default: "/robot_status"): Topic name for publishing system health status
- `check_rate` (default: 1.0): Rate (Hz) for periodic health checks

## Topics

### Subscribed Topics
- `/scan` (sensor_msgs/LaserScan): Laser scanner data
- `/camera/image_raw` (sensor_msgs/Image): Camera image data
- `/odom` (nav_msgs/Odometry): Odometry data
- `/cmd_vel` (geometry_msgs/Twist): Command velocity data

### Published Topics
- `/robot_status` (std_msgs/Float64): System health score (0.0 to 1.0)

## Data Evaluation Criteria

### Laser Scanner
- Checks for empty scan data
- Validates range readings for NaN and infinite values
- Monitors ratio of invalid readings (threshold: 50%)

### Camera
- Validates image data is not empty
- Checks for valid image dimensions

### Odometry
- Validates position and orientation values
- Checks for NaN values in pose data

## Health Scoring
The system health score is calculated as the average quality of all active sensors:
- Score ranges from 0.0 (poor) to 1.0 (excellent)
- Sensors are considered active if data has been received within the timeout threshold
- Individual sensor quality is binary: 1.0 for good data, 0.5 for poor data

## Example Output
```
[ INFO] [1642345678.123]: Starting Robot Data Monitor Node
[ INFO] [1642345678.124]: DataEvaluator initialized successfully
[ INFO] [1642345678.125]: DataEvaluator started
[ INFO] [1642345678.126]: Robot Data Monitor Node is running...
[ INFO] [1642345683.127]: System health score: 0.83
```

## Troubleshooting

### Common Issues
1. **No sensor data received**: Check if sensor nodes are running and topics are correct
2. **Poor health scores**: Review sensor configuration and data quality
3. **Build errors**: Ensure all dependencies are installed

### Debug Information
Enable debug output by setting the log level:
```bash
rosservice call /robot_data_monitor_node/set_logger_level "logger: 'ros.robot_data_monitor'
level: 'debug'"
```

## Contributing
Please follow the ROS coding standards and include appropriate documentation for any new features.

## License
This package is licensed under the [LICENSE] - see the LICENSE file for details.
