#정올 LCoder_Python  클래스- 자가진단1
class Program :
    #생성자 정의
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade

    def info(self):
        return "이름: {} \n학교: {} \n학년: {}".format(self.name, self.school, self.grade)



name = input("이름:  ")
school = input("학교:  ")
grade = input("학년:   ")


a = Program(name, school, grade)
print(a.info())
