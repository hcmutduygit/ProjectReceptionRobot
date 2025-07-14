from USB_CAN_A_Waveshare.waveshare_can import WaveshareCAN
import time
import struct

def hex_to_signed(hex_str, bits=16):
    value = int(hex_str, 16)
    if value >= 2**(bits - 1):
        value -= 2**bits
    return value

def process_frame(can_id, data):
    if can_id == 0x012:
        # Example: publish to topic_A
        hex_str = data.hex()

        roll_raw = hex_to_signed(hex_str[0:4], 16)
        roll = roll_raw / 100.0

        pitch_raw = hex_to_signed(hex_str[4:8], 16)
        pitch = pitch_raw / 100.0

        yaw_raw = int(hex_str[8:12], 16)  # Không dùng hex_to_signed
        yaw = yaw_raw / 100.0
        if yaw > 180.0:
            yaw -= 360.0
        elif yaw < -180.0:
            yaw += 360.0
        print(f"ID 0x123 received: {data.hex(' ')}")
        print(f"Roll: {roll}")
        print(f"Pitch: {pitch}")
        print(f"Yaw: {yaw}")
        

    elif can_id == 0x200:
        # Maybe decode as float?
        value = struct.unpack('<f', data[0:4])[1]
        print(f"ID 0x200 float value: {value:.2f}")
    else:
        print(f"Ignored ID: 0x{can_id:03X}")

def send_vel():
    # Send velocity
    right_vel = float(input("Enter right wheel velocity: "))
    left_vel = float(input("Enter left wheel velocity: "))
    right_bytes = struct.pack('<f', right_vel)  # '<f': little-endian float
    left_bytes = struct.pack('<f', left_vel)    # '<f': little-endian float
    can_dev.send(0x013, right_bytes)
    time.sleep(0.1)  # Optional delay
    can_dev.send(0x014, left_bytes)  


if __name__ == "__main__":
    with WaveshareCAN(port='/dev/ttyUSB0') as can_dev:

        can_dev.start_receive_loop(process_frame)

        # Main loop: send command only when needed
        while True:
            # user_input = float(input("Enter message to send (or press ENTER to skip): "))
            # bytes_float = struct.pack('<f', user_input)  # '<f': little-endian float
            # if user_input:
            #     can_dev.send(0x130, bytes_float)
            # time.sleep(0.1)
            send_vel()
