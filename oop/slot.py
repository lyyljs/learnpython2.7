class Student(object):
	__slots__ = ('name','age')
	pass

class GraduateStudent(Student):
	pass

s = Student()
s.name = 'lyyljs'
s.age = 25
#s.score = 99

g = GraduateStudent()
g.score = 99
