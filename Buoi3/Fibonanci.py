# Fn = Fn-1 + Fn-2, F0 = 0, F1 =1
x_0 = 0
x_1 = 1
F=1
def Fibonanci(number):
    if number <= 1:
        return number
    return Fibonanci(number-1) + Fibonanci(number-2)

print(Fibonanci(6))
        
    
