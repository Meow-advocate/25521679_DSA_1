import time
import numpy as np

tong_thoi_gian = 0  # Biến để cộng dồn
files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]

for ten_file in files:
    with open(ten_file, 'r') as f:
        # Numpy có cách đọc file .txt/.inp nhanh
        data = np.fromstring(f.read(), sep=' ')
    #Đếm thời gian cho numpy sort từng file
    start = time.perf_counter()
    np.sort(data)
    end = time.perf_counter()
    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | NumpySort: {thoi_gian} ms")
print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")

