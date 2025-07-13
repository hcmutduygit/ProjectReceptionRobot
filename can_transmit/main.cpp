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

    while (true) {
        std::cout << "Enter float to send (or empty to skip): ";
        std::string input;
        std::getline(std::cin, input);

        if (input.empty()) continue;

        try {
            float value = std::stof(input);

            uint8_t bytes[4];
            std::memcpy(bytes, &value, sizeof(float));

            std::vector<uint8_t> data(bytes, bytes + 4);
            can.send(0x123, data);

        } catch (const std::exception& e) {
            std::cerr << "Invalid input: " << e.what() << "\n";
            continue;
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}