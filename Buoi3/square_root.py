def square_root(N, num_loop):
    x_n = N / 2
    
    for i in range(num_loop):
        x_np1 = (x_n + N / x_n) / 2
        x_n = x_np1
    return x_np1
N = int(input("Nhập số cần tính square_root: "))
n = int(input("Nhập số lần lặp: "))
print(f"Căn bậc 2 của {N} là: {square_root(N, n)}")