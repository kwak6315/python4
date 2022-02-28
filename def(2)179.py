# 반올림  round()
# a = float(input("소수점이 포함된 실수를 입력하세요>> a: "))
# b = float(input("소수점이 포함된 실수를 입력하세요>> b: "))
# c = float(input("소수점이 포함된 실수를 입력하세요>> c: "))
#
# def abc(a,b,c):
#     sum = 0
#     sum = a + b + c
#     avg = sum /3
#     end = round(avg,1)
#     return end
#
# print(abc(a, b, c))


a = float(input("소수점이 포함된 실수를 입력하세요>> a: "))
b = float(input("소수점이 포함된 실수를 입력하세요>> b: "))
c = float(input("소수점이 포함된 실수를 입력하세요>> c: "))
A = round(a)
B = round(b)
C = round(c)

def ABC(A, B, C):
    sum = 0
    sum = A + B + C
    avg = sum/3
    return round(avg)

print(ABC(A,B,C))











