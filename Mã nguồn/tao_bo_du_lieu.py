import numpy as np

N = 1000000

def tao_file(ten_file, mang):
    with open(ten_file, 'w') as f: 
        f.write(" ".join(map(str, mang))) #Ghi trực tiếp các số, cách nhau bởi dấu cách
    print(f"Đã tạo xong: {ten_file}")

# 5 dãy số thực (0 đến 1)
tao_file("thuc_tang_1.inp", np.sort(np.random.rand(N)))
tao_file("thuc_ngau_3.inp", np.random.rand(N))
tao_file("thuc_ngau_6.inp", np.random.rand(N))
tao_file("thuc_ngau_8.inp", np.random.rand(N))
tao_file("thuc_ngau_9.inp", np.random.rand(N))

# 5 dãy số nguyên (0 đến 1.000.000)
tao_file("nguyen_giam_2.inp", np.sort(np.random.randint(0, 10**6, N))[::-1])
tao_file("nguyen_ngau_4.inp", np.random.randint(0, 10**6, N))
tao_file("nguyen_ngau_5.inp", np.random.randint(0, 10**6, N))
tao_file("nguyen_ngau_7.inp", np.random.randint(0, 10**6, N))
tao_file("nguyen_ngau_10.inp", np.random.randint(0, 10**6, N))
