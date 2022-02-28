# 반복 제어2 - 자가진단 7

a = list(map(int, input("정수를 입력해주세요: ").split()))
avg = sum(a) / len(a)   #총합 / 길이
print("avg : {}".format(avg))

if avg >= 80:
    print("pass")
else:
    print("fail")