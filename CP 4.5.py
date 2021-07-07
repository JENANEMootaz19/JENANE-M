import math
numbers=input("D:")
numbers=numbers.split(',')
result_list = []
C=50
H=30
def calculate(D):
    Q= round(math.sqrt(2 * C * int(D)/H))
    return Q
for i in numbers:
    Q=calculate(i)
    result_list.append(Q)
print(result_list)
