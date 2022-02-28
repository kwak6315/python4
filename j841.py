# 반복제어문 2 - 자가진단1
#for문 사용한 반복 제어문

a = []   #빈리스트를 생성
n = int(input("자연수를 입력하세요>>  "))
for i in range(n,0, -1):       # 감소할 경우에는 줄어드는 범위 기입 필수 Ex) -1
    a.append(i)

print(a)

