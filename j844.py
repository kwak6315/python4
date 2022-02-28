num = int(input("2이상 100이하의 정수를 입력하세요>>  "))
while (num < 2) or (num > 100):
    num = int(input("2이상 100이하의 정수를 다시 입력하세요>>  "))

if num%2 == 0:
    for i in range(2,num+1,2):
        print(i, end = " ")

if num%2 == 1:
    for i in range(2, num, 2):
        print(i, end =" ")

