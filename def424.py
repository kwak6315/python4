#클래스 자가진단 4             삼각형의 무게중심 round

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        #ctrl + d : 복사 붙여넣기
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
    #무게 중심을 구하는 함수

    def center_of_triangle(self):

        #round(값, 반올림할 자리수)
        x = round((self.x1+self.x2+self.x3)/3,1)
        y = round((self.y1+self.y2+self.y3)/3,1)
        print("({},{})".format(x,y))

T1 = Triangle(0,0,1,2,10,15)  #객체
T1.center_of_triangle()



