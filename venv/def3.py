#반복문
#for문
def square(r):
    count = 1
    for i in range(r): # 1 5 9 13
        for j in range(r): # 1 2 3 4
            print(count, end =" ")
            count += 1
        print("")
user = int(input("숫자를 입력하시오>> "))
square(user)

