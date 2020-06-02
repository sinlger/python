class School:
    '''代表学校里的任何学院'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        '''告诉我有关的细节'''
        print('name:{},age:{}'.format(self.name,self.age))

class Teacher(School):
    '''代表一位老师'''
    def __init__(self,name,age,salary):
        School.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        School.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(School):
    '''代表一位学生'''
    def __init__(self,name,age,marks):
        School.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        School.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()