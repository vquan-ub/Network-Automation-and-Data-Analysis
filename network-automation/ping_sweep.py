#Dùng để quét IP kiểm tra thiết bị online/offline
from scapy.all import IP, ICMP, sr1

def ping_sweep(subnet):
    print(f"--- Bắt đầu quét dải mạng giả lập: {subnet}.0/24 ---")
    
    # Quét thử nghiệm các IP từ .1 đến .10 trong dải mạng nội bộ
    for ip_suffix in range(1, 11):
        target_ip = f"{subnet}.{ip_suffix}"
        
        # Ứng dụng thư viện Scapy để tự chế gói tin ICMP (gói tin Ping)
        packet = IP(dst=target_ip)/ICMP()
        
        # Gửi gói tin đi và chờ phản hồi trong vòng 1 giây (timeout=1)
        reply = sr1(packet, timeout=1, verbose=0)
        
        if reply is None:
            print(f"[MẤT KẾT NỐI] Thiết bị tại IP: {target_ip} không phản hồi.")
        else:
            print(f"[ONLINE] Thiết bị tại IP: {target_ip} đang hoạt động bình thường.")

if __name__ == "__main__":
    # Thử nghiệm quét dải mạng nội bộ phổ biến
    ping_sweep("192.168.1")