import numpy as np
import time
import sys

sys.setrecursionlimit(2000000)

def quick_sort(arr):
    if arr.size <= 1:
        return arr
    pivot = arr[arr.size // 2]
    left = arr[arr < pivot]
    mid = arr[arr == pivot]
    right = arr[arr > pivot]
    return np.concatenate((quick_sort(left), mid, quick_sort(right)))

files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]
tong_thoi_gian = 0

for ten_file in files:
    with open(ten_file, 'r') as f:
        data = np.fromstring(f.read(), sep=' ')
    
    start = time.perf_counter()
    quick_sort(data)
    end = time.perf_counter()
    
    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | QuickSort: {thoi_gian} ms")

print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")
