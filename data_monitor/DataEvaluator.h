#ifndef DATA_EVALUATOR_H
#define DATA_EVALUATOR_H

#include <ros/ros.h>
#include <vector>
#include <stdint.h>

namespace DataEvaluator {

// ==============================
// Biến toàn cục
// ==============================

// Thông tin thống kê byte/gói
extern uint64_t total_bytes_received;
extern uint64_t throughput_bytes_last_sec;

extern uint32_t count_velocity;
extern uint32_t count_yaw;

extern uint32_t expected_packets_per_sec;

// Thời gian nhận gói gần nhất
extern ros::Time last_velocity_time;
extern ros::Time last_yaw_time;

// ==============================
// Throughput
// ==============================

inline void evaluate_Throughput(const ros::TimerEvent&) {
    throughput_bytes_last_sec = total_bytes_received;
    total_bytes_received = 0;

    ROS_INFO_STREAM("Throughput: " << throughput_bytes_last_sec << " bytes/s");
}

// ==============================
// LossRate
// ==============================

inline void evaluate_LossRate(const ros::TimerEvent&) {
    float loss_v = 100.0f * (expected_packets_per_sec - count_velocity) / expected_packets_per_sec;
    float loss_yaw = 100.0f * (expected_packets_per_sec - count_yaw) / expected_packets_per_sec;

    if (count_velocity == 0)
        ROS_ERROR_STREAM("Không nhận gói velocity!");
    else if (count_velocity < expected_packets_per_sec)
        ROS_WARN_STREAM("Thiếu velocity: " << loss_v << "%");
    else
        ROS_INFO_STREAM("Velocity OK (" << expected_packets_per_sec << " Hz)");

    if (count_yaw == 0)
        ROS_ERROR_STREAM("Không nhận gói yaw!");
    else if (count_yaw < expected_packets_per_sec)
        ROS_WARN_STREAM("Thiếu yaw: " << loss_yaw << "%");
    else
        ROS_INFO_STREAM("Yaw OK (" << expected_packets_per_sec << " Hz)");

    count_velocity = 0;
    count_yaw = 0;
}

// ==============================
// Checksum
// ==============================

inline bool evaluate_Checksum(const std::vector<uint8_t>& data_tach) {
    if (data_tach.size() < 17) {
        ROS_WARN("Data ít hơn 17 byte!");
        return false;
    }

    uint8_t id = data_tach[0];
    uint8_t length = data_tach[12];
    uint8_t received_checksum = data_tach[16];

    uint16_t sum = id + length;

    if ((id == 0x01 || id == 0x02) && length == 0x08) {
        for (int i = 4; i < 12; ++i) {
            sum += data_tach[i];
        }
    } else {
        ROS_WARN("ID hoặc Length sai. ID = 0x%02X, Len = %d", id, length);
        return false;
    }

    uint8_t computed_checksum = sum & 0xFF;

    if (computed_checksum != received_checksum) {
        ROS_WARN_STREAM("Checksum FAIL! Nhận: " << int(received_checksum)
                        << ", Tính: " << int(computed_checksum));
        return false;
    }

    return true;
}

// ==============================
// Sanity Check (giá trị hợp lý)
// ==============================

inline bool check_Sanity(float velocity, float yaw) {
    bool ok = true;

    if (velocity < -5.0 || velocity > 5.0) {
        ROS_ERROR_STREAM("Sanity fail: Velocity out of range! v = " << velocity);
        ok = false;
    }

    if (yaw < -180.0 || yaw > 180.0) {
        ROS_ERROR_STREAM("Sanity fail: Yaw out of range! yaw = " << yaw);
        ok = false;
    }

    return ok;
}

// ==============================
// Delay detection (trễ gói)
// ==============================

inline void detect_Delay(bool is_velocity) {
    ros::Time now = ros::Time::now();
    double dt = 0.0;

    if (is_velocity) {
        dt = (now - last_velocity_time).toSec();
        if (last_velocity_time.toSec() > 0 && dt > 0.5) {
            ROS_WARN_STREAM("Velocity DELAY! dt = " << dt << " s");
        }
        last_velocity_time = now;
    } else {
        dt = (now - last_yaw_time).toSec();
        if (last_yaw_time.toSec() > 0 && dt > 0.5) {
            ROS_WARN_STREAM("Yaw DELAY! dt = " << dt << " s");
        }
        last_yaw_time = now;
    }
}

} // namespace DataEvaluator

#endif // DATA_EVALUATOR_H
