#include <ros/ros.h>
#include "robot_data_monitor/DataEvaluator.h"

int main(int argc, char **argv) {
    ros::init(argc, argv, "monitor_node");
    ros::NodeHandle nh;

    // Load param (có thể load từ yaml)
    nh.param("expected_packets_per_sec", DataEvaluator::expected_packets_per_sec, 5U);

    // Khởi tạo timer
    ros::Timer t1 = nh.createTimer(ros::Duration(1.0), DataEvaluator::evaluate_Throughput);
    ros::Timer t2 = nh.createTimer(ros::Duration(1.0), DataEvaluator::evaluate_LossRate);

    ROS_INFO_STREAM("DataEvaluator node started");

    ros::spin();
    return 0;
}
