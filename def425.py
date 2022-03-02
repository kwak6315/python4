#425

class Personal_Info:
    def __init__(self, name, height):
        self.name = name
        self.height = height



P1 = Personal_Info("Park", 175)
P2 = Personal_Info("Lee", 180)
P3 = Personal_Info("Choo", 185)
P4 = Personal_Info("Son", 193)
P5 = Personal_Info("Kim", 188)


Height = [P1.height,P2.height,P3.height,P4.height,P5.height]
Name = [P1.name, P2.name, P3.name, P4.name, P5.name]
current_index = 0

current_height = Height[0]   #비교대상
for i in range(0,5) :
    if (current_height > Height[i]):
        current_index = i  # 현재 키가 가장 작은 사람의 인덱스

print("{} {}".format(Name[current_index], Height[current_index]))