import random
import math

N = 100000
N_c = 0 # Số điểm thuộc đường tròn

for i in range(N):
    x = random.random() + 2 - 1
    y = random.random() + 2 - 1
    x2 = math.pow(x,2)
    y2 = math.pow(y,2)
    if math.sqrt(x2+y2) <= 1.0:
        N_c += 1
pi = (N_c * 4) / N # Cong thuc tinh PI theo uniform distribution
print(pi)