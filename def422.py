# #클래스 자가진단 2
#
# class Program:
#     def __init__(self, school, grade):
#         self.school = school
#         self.grade = grade
#
#     def School(self):
#         print("6 grade in Jejuelementary School \n {}grade in {} ".format(self.grade, self.school))
#
#
#
# school = input("학교이름은?? ")
# grade = int(input("학년은?  "))
#
# a = Program(school, grade)
# a.School()

class School:
    #생성자(초기값을 저장)
    def __init__(self, school="abc", grade="6학년"):
        self.school = school
        self.grade = grade

    #정보출력함수
    def info(self):
        print("{} grade in {} School ".format(self.grade, self.school))

#객체생성(인스턴스)
person1 =School()
person2 =School("cba", "3학년")
person1.info()
person2.info()





