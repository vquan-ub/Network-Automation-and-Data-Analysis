#Dùng để tự động sao lưu cấu hình thiết bị
import time
from netmiko import ConnectHandler

# Giả lập danh sách các thiết bị mạng Cisco (Router/Switch) trong Packet Tracer
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',  # IP của Router giả lập
        'username': 'admin',
        'password': 'password123',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.2',  # IP của Switch giả lập
        'username': 'admin',
        'password': 'password123',
    }
]

print("--- Bắt đầu tiến trình tự động sao lưu cấu hình hệ thống mạng ---")

for device in devices:
    try:
        print(f"\n[+] Đang kết nối tới thiết bị: {device['host']}...")
        # Thiết lập kết nối SSH bằng thư viện Netmiko
        connection = ConnectHandler(**device)
        
        # Thực thi lệnh lấy cấu hình chạy hiện tại của thiết bị Cisco
        print(f"[+] Đang thực thi lệnh lấy running-config...")
        config_data = connection.send_command('show running-config')
        
        # Tạo tên file lưu trữ theo IP và mốc thời gian ngày-tháng-năm
        current_date = time.strftime("%Y%m%d")
        filename = f"backup_{device['host']}_{current_date}.txt"
        
        # Ghi dữ liệu cấu hình vào file text để lưu trữ
        with open(filename, "w", encoding="utf-8") as file:
            file.write(config_data)
            
        print(f"[✓] Đã sao lưu thành công! File lưu trữ: {filename}")
        connection.disconnect()
        
    except Exception as e:
        print(f"[X] Không thể kết nối tới {device['host']}. Lỗi: {str(e)}")

print("\n--- Tiến trình hoàn thành ---")