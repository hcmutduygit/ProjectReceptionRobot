#include "USB_CAN_A_Waveshare/waveshare_can.hpp"
#include <thread>
#include <chrono>
#include <iomanip>

// Convert two bytes to a signed 16-bit integer (equivalent to Python's hex_to_signed)
int16_t hex_to_signed(const std::vector<uint8_t>& data, size_t start_idx, size_t bits = 16) {
    // Combine two bytes into a 16-bit unsigned integer (big-endian)
    uint16_t value = (data[start_idx] << 8) | data[start_idx + 1];
    // Adjust for signed representation (two's complement)
    if (value >= (1U << (bits - 1))) {
        value -= (1U << bits);
    }
    return static_cast<int16_t>(value);
}

// For Yaw angle
uint16_t hex_to_unsigned(const std::vector<uint8_t>& data, size_t start_idx) {
    // Little-endian: byte thấp trước, byte cao sau
    return static_cast<uint16_t>(
        data[start_idx] | (data[start_idx + 1] << 8)
    );
}

void send_vel(WaveshareCAN& can) {
    float right_vel = 5.5;
    float left_vel = 5.5;

    uint8_t left_bytes[4];
    uint8_t right_bytes[4];
    std::memcpy(left_bytes, &left_vel, sizeof(float));
    std::memcpy(right_bytes, &right_vel, sizeof(float));

    std::vector<uint8_t> left_data(left_bytes, left_bytes + 4);
    std::vector<uint8_t> right_data(right_bytes, right_bytes + 4);

    can.send(0x013, left_data);
    std::cout << "Sent left velocity to ID 0x013\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm

    can.send(0x014, right_data);
    std::cout << "Sent right velocity to ID 0x014\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm

    can.send(0x015, {0x01, 0x02, 0x03, 0x04});
    std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm
    can.send(0x016, {0x05, 0x06, 0x07, 0x08});
    std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm
    // can.send(0x017, {0x09, 0x0A, 0x0B, 0x0C});
    // std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm
    // can.send(0x018, {0x0D, 0x0E, 0x0F, 0x10});
    // std::this_thread::sleep_for(std::chrono::milliseconds(50)); // thêm
    // std::cout << "Sent ID 0x016\n";
}
// Process CAN frame (equivalent to Python's process_frame)
void process_frame(uint16_t can_id, const std::vector<uint8_t>& data) {
    if (can_id == 0x012) {
        // Ensure data has at least 6 bytes for roll, pitch, yaw (2 bytes each)
        if (data.size() < 6) {
            std::cerr << "❌ Error: Insufficient data bytes for ID 0x012\n";
            return;
        }

        // Extract roll, pitch, yaw as signed 16-bit integers and scale by 100.0
        double roll = hex_to_signed(data, 0) / 100.0;  // Bytes 0-1
        double pitch = hex_to_signed(data, 2) / 100.0; // Bytes 2-3
        double yaw = hex_to_signed(data, 4) / 100.0;   // Bytes 4-5
        if (yaw > 180.0) {
            yaw -= 360.0;
        }
        else if (yaw <= -180.0) {
            yaw += 360.0;
        }
        // Print data in hex format
        std::cout << "ID 0x012 received: ";
        for (uint8_t b : data) {
            std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)b << " ";
        }
        std::cout << std::dec << "\n";

        // Print roll, pitch, yaw with 2 decimal places
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Roll: " << roll << "\n";
        std::cout << "Pitch: " << pitch << "\n";
        std::cout << "Yaw: " << yaw << "\n";
    }
}

int main() {
    WaveshareCAN can("/dev/ttyUSB0", 2000000, 2.0);
    can.open();
    can.start_receive_loop(process_frame);
    send_vel(can);
    while (true) {
        // std::cout << "\n=== CAN Control Menu ===" << std::endl;
        // std::cout << "1. Send single float value (ID 0x123)" << std::endl;
        // std::cout << "2. Send wheel velocities (Left: ID 0x013, Right: ID 0x014)" << std::endl;
        // std::cout << "3. Skip/Continue" << std::endl;
        // std::cout << "Enter your choice (1/2/3): ";
        
        // std::string choice;
        // std::getline(std::cin, choice);

        // if (choice == "1") {
        //     std::cout << "Enter float to send: ";
        //     std::string input;
        //     std::getline(std::cin, input);

        //     if (!input.empty()) {
        //         try {
        //             float value = std::stof(input);

        //             uint8_t bytes[4];
        //             std::memcpy(bytes, &value, sizeof(float));

        //             std::vector<uint8_t> data(bytes, bytes + 4);
        //             can.send(0x123, data);
        //             std::cout << "Sent float " << value << " to ID 0x123" << std::endl;

        //         } catch (const std::exception& e) {
        //             std::cerr << "Invalid input: " << e.what() << "\n";
        //         }
        //     }
        // }
        // else if (choice == "2") {
        //     send_vel(can);
        // }
        // else if (choice == "3") {
        //     std::cout << "Continuing..." << std::endl;
        // }
        // else {
        //     std::cout << "Invalid choice. Please enter 1, 2, or 3." << std::endl;
        // }
        send_vel(can);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}