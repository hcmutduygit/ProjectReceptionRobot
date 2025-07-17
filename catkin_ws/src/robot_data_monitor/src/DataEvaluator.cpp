#include "robot_data_monitor/DataEvaluator.h"

namespace DataEvaluator {
    uint64_t total_bytes_received = 0;
    uint64_t throughput_bytes_last_sec = 0;

    uint32_t count_velocity = 0;
    uint32_t count_yaw = 0;

    uint32_t expected_packets_per_sec = 5;

    ros::Time last_velocity_time = ros::Time(0);
    ros::Time last_yaw_time = ros::Time(0);
}
