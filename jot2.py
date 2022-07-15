# class school:
#     x=5
# print(school)
# p1=school()
# print(p1.x)
         

class student:
    def __init__(self,name,sex,age):
        self.name='name'
        self.sex='sex'
        self.age='age'
        
def studentprofile(self):
    return f' the student name is {self.name} and the studentsex is {self.sex} and the student age is {self.age} years old'
Betty = student("betty","female","19")
daniel = student("daniel","male","18")
print('Betty.studentprofile')
print('daniel.studentprofile')
        
