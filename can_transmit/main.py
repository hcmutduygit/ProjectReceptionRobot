from USB_CAN_A_Waveshare.waveshare_can import WaveshareCAN
import time
import struct
def process_frame(can_id, data):
    if can_id == 0x130:
        # Example: publish to topic_A
        print(f"ID 0x130 received: {data.hex(' ')}")
    elif can_id == 0x200:
        # Maybe decode as float?
        value = struct.unpack('<f', data[0:4])[0]
        print(f"ID 0x200 float value: {value:.2f}")
    else:
        print(f"Ignored ID: 0x{can_id:03X}")
# 4-byte unsigned int
value = 555555
payload = struct.pack('<I', value)  # Little endian uint32

if __name__ == "__main__":
    with WaveshareCAN(port='/dev/ttyUSB0') as can_dev:
        can_dev.send(0x130, "HELLO")
        can_dev.send(0x130, [0x00, 0x02, 0xBF, 0x20])
        can_dev.send(0x130, payload)
        # Start continuous receive loop in a separate thread
        can_dev.start_receive_loop(process_frame)

        # Main loop: send command only when needed
        while True:
            user_input = input("Enter message to send (or press ENTER to skip): ")
            if user_input:
                can_dev.send(0x130, user_input)
            time.sleep(0.1)
