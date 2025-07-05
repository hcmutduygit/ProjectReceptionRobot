                # # Kiểm tra dữ liệu nhận được (giả sử SLCAN)
                # if raw_data[2:4] == b'\x01\x01' and raw_data[4:6] == b'\x01\x23': # ID 0x123
                #     # Gửi khung CAN xác nhận (ID 0x200, DLC=1, dữ liệu=0x01)
                #     ack_frame = bytearray()
                #     ack_frame.extend(b'\xAA\x55\x01\x01\x02\x00\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\xA0')
                #     ser.write(ack_frame)
                #     print("Đã gửi xác nhận (ID=0x200)")