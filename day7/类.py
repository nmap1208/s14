#Auther nmap
class Foo(object):
    def __init__(self,name,age,sex,salary,course):
        super(Foo, self).__init__(name,age,sex)
        self.salary=salary
        self.course=course


class SchoolMember():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course,school_obj):
        super(Teacher,self).__init__(name,age,sex)
        self.school=school_obj
        self.course=course
        self.salary=salary
    def tell(self):
        pass