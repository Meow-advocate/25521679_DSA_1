import time
import sys

tong_thoi_gian = 0  # Biến để cộng dồn
sys.setrecursionlimit(2000000) # Đặt giới hạn đệ quy cao hơn số phần tử (1 triệu)
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: res.append(left[i]); i += 1
        else: res.append(right[j]); j += 1
    return res + left[i:] + right[j:]

files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]

for ten_file in files:
    with open(ten_file, 'r') as f:
        data = list(map(float, f.read().split()))# Đọc toàn bộ số vào list
    #Đếm thời gian cho merge sort từng file
    start = time.perf_counter()
    merge_sort(data)
    end = time.perf_counter()
    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | MergeSort: {thoi_gian} ms")
print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")

