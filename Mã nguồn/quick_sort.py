import time
import sys

tong_thoi_gian = 0  # Biến để cộng dồn
sys.setrecursionlimit(2000000) # Đặt giới hạn đệ quy cao hơn số phần tử (1 triệu)
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]

for ten_file in files:
    with open(ten_file, 'r') as f:
        data = list(map(float, f.read().split())) # Đọc toàn bộ số vào list
    #Đếm thời gian cho quick sort từng file
    start = time.perf_counter()
    quick_sort(data)
    end = time.perf_counter()
    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | QuickSort: {thoi_gian} ms")
print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")

