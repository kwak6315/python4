
user1 = int(input("10 미만의 수를 입력하시오 >>>   "))

while(user1 >10) :
    user1 = int(input("10 미만의 수를 다시 입력하시오 >>>   "))       #a가 10 보다 작아지면 while 문을 탈출함

user2 = int(input("10 미만의 수를 입력하시오 >>>   "))
while(user2 > 10) :
    user2 = int(input("10 미만의 수를 다시 입력하시오 >>>   "))





def mul(user1, user2):
    result = user1 ** user2
    return result

print(mul(user1, user2))



