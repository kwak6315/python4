num = int(input("정수 입력 : "))
a= []

for i in range(num, 101): #num, num+1,...., 100
    a.append(i)

result = sum(a)    #리스트 안의 모든 원소를 더해줌
print(result)