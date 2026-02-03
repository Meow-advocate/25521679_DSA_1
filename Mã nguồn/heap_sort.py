import time

tong_thoi_gian = 0  # Biến để cộng dồn
def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[i] < arr[l]: largest = l
    if r < n and arr[largest] < arr[r]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

files = ["thuc_tang_1.inp", "nguyen_giam_2.inp", "thuc_ngau_3.inp", "nguyen_ngau_4.inp", "nguyen_ngau_5.inp", "thuc_ngau_6.inp", "nguyen_ngau_7.inp", "thuc_ngau_8.inp", "thuc_ngau_9.inp", "nguyen_ngau_10.inp"]

for ten_file in files:
    with open(ten_file, 'r') as f:
        data = list(map(float, f.read().split()))# Đọc toàn bộ số vào list
    #Đếm thời gian cho heap sort từng file
    start = time.perf_counter()
    heap_sort(data)
    end = time.perf_counter()
    thoi_gian = round((end - start) * 1000, 2)
    tong_thoi_gian += thoi_gian
    print(f"File: {ten_file} | HeapSort: {thoi_gian} ms")
print(f"Trung binh: {round(tong_thoi_gian / 10, 2)} ms")

