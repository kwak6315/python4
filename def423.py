

import math #모듈 불러오기
class Score:
    def __init__(self, name, Korean, English):
        self.name = name
        self.Korean = Korean
        self.English = English


Junho = Score("Junho", 88 ,100)
Seonbin = Score("Seonbin", 95, 96)

#math 모듈 사용하기 --floor
#round 는 파이썬 내장함수라서 import math 불러올 필요 X
K_avg = math.floor((Junho.Korean + Seonbin.Korean)/2)
E_avg = round((Junho.English + Seonbin.English)/2)

print("avg {} {}".format(K_avg, E_avg))


