import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("--- Khởi động tiến trình phân tích hệ thống log ---")

# 1. Sử dụng Pandas đọc và làm sạch dữ liệu từ file CSV
try:
    df = pd.read_csv('data-analysis/system_logs.csv')
    print("[✓] Đã đọc file log thành công qua thư viện Pandas.")
    
    # Trích xuất 2 đặc trưng quan trọng nhất để đưa vào mô hình toán học
    X = df[['CPU_Usage', 'Memory_Usage']]
    
    # 2. Triển khai thuật toán Học máy K-Means Clustering
    # Giả định chia hệ thống thành 3 cụm trạng thái (An toàn - Cảnh báo - Nguy hiểm)
    print("[+] Đang tiến hành gom cụm dữ liệu bằng thuật toán K-Means...")
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster_ID'] = kmeans.fit_predict(X)
    
    # 3. Trực quan hóa kết quả gom cụm ra biểu đồ bằng Matplotlib
    plt.figure(figsize=(8, 6))
    
    # Vẽ các điểm dữ liệu log, tô màu khác nhau dựa theo ID của từng cụm
    scatter = plt.scatter(df['CPU_Usage'], df['Memory_Usage'], c=df['Cluster_ID'], cmp='viridis', s=100)
    
    # Vẽ các tâm cụm (Centroids) - vị trí đại diện cho từng nhóm hành vi
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Tâm cụm')
    
    plt.title('Biểu đồ phân tích cụm Log hệ thống (CPU vs Memory)')
    plt.xlabel('Mức độ sử dụng CPU (%)')
    plt.ylabel('Mức độ sử dụng RAM (%)')
    plt.grid(True)
    plt.legend()
    
    # Lưu kết quả đồ thị thành một file ảnh trong thư mục dự án
    output_image = 'data-analysis/elbow_chart.png'
    plt.savefig(output_image)
    print(f"[✓] Đã xuất biểu đồ phân tích thành công: {output_image}")
    
except Exception as e:
    print(f"[X] Có lỗi xảy ra trong quá trình xử lý. Chi tiết: {str(e)}")

print("--- Tiến trình hoàn thành ---")