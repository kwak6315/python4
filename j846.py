#반복제어2 - 자가진단 6
a = map(int, input("숫자를 입력해주세요: ").split())    #split 숫자를 띄어쓰기
# a는 map object(맵 객체)
#list(a)  --> a에 들어있는 값 확인
three = []
five = []
for i in a: # a = 맵 오브젝트
    if i % 3 == 0: #3의 배수
        three.append(i)
    if i % 5 == 0: #5의 배수
        five.append(i)

print("Multiples of 3 : %d" %len(three))
print("Multiples of 5 : %d" %len(five))