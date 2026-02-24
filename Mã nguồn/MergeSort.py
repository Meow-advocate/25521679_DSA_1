import numpy as np
import time
import sys

sys.setrecursionlimit(2000000)

def merge_sort(arr):
    if arr.size <= 1:
        return arr

    mid = arr.size // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = k = 0
    res = np.empty_like(arr)

    while i < left.size and j < right.size:
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1

    if i < left.size:
        res[k:] = left[i:]
    if j < right.size:
        res[k:] = right[j:]

    return res

files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]
tong_thoi_gian = 0

for ten_file in files:
    with open(ten_file, 'r') as f:
        data = np.fromstring(f.read(), sep=' ')

    start = time.perf_counter()
    merge_sort(data)
    end = time.perf_counter()

    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | MergeSort: {thoi_gian} ms")

print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")
