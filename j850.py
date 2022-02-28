#반복제어2 - 형성평가 1
n = int(input("10이하의 자연수를 입력하세요>>  "))
while True:
    if n > 10:
        n = int(input("10이하의 자연수를 다시 입력하세요>>  "))
    else:
        break
for i in range(n):
    print("JUNGOL")

