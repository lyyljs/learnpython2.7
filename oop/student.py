class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
