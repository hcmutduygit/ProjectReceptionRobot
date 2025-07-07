import serial
import time
import struct

def read_serial_data(port='/dev/ttyUSB1', baudrate=2000000, timeout=1):
    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=timeout
        )
        
        print(f"Đã kết nối với cổng {port} tại tốc độ {baudrate} baud")
        
        while True:
            if ser.in_waiting > 0:
                raw_data = ser.read(ser.in_waiting)
                print(f"Dữ liệu CAN (hex): {raw_data.hex()[19]}")
                
                # # Kiểm tra dữ liệu nhận được (giả sử SLCAN)
                # if raw_data[2:4] == b'\x01\x01' and raw_data[4:6] == b'\x01\x23': # ID 0x123
                #     # Gửi khung CAN xác nhận (ID 0x200, DLC=1, dữ liệu=0x01)
                #     ack_frame = bytearray()
                #     ack_frame.extend(b'\xAA\x55\x01\x01\x02\x00\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\xA0')
                #     ser.write(ack_frame)
                #     print("Đã gửi xác nhận (ID=0x200)")
            
            time.sleep(0.01)
            
    except serial.SerialException as e:
        print(f"Lỗi kết nối serial: {e}")
        print("Hãy kiểm tra cổng hoặc quyền truy cập (nhóm 'dialout').")
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình bởi người dùng")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Đã đóng cổng serial")
 
if __name__ == "__main__":
    read_serial_data(port='/dev/ttyUSB0', baudrate=2000000)
