#Auther nmap

class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        teacher_list=[]

    def create_course(self,type,period,price):
        self.type=type
        self.period=period
        self.price=price

    def create_class(self,name):
        self.name=name
    def hire_teacher(self,teach_obj):
        self.teacher_list.append(teach_obj)
        print('雇佣了新老师，名字是%s,授课为%s'%(teach_obj.name,teach_obj.Teaching_name))

    def enroll(self,stu_obj):
        print('为学员%s办理入学手续'%(stu_obj.name))


class Teacher(object):
    def __init__(self,name,age,salary,Teaching_name):
        self.name=name
        self.age=age
        self.salay=salary
        self.Teaching_name=Teaching_name

    def show_class(self):
        print('查看班级')
    def show_stu(self):
        print('查看班级学员列表')


class Student(object):
    def __init__(self,name):
        self.name=name
    def enroll(self,course_obj,addr):
        self.course_obj=course_obj
        self.addr=addr
        print('%s注册学习%s课程'%(self.name,course_obj.name))


class Course(object):
    def __init__(self,type):
        self.type=type


    def create_course(self,period,price):
        pass







def inter():
    print('hehe')