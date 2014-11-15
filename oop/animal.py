class Animal(object):
	def run(self):
		pass
#	def eat(self):
#		pass

class Dog(Animal):
	def run(self):
		print 'Dog is running'
	def eat(self):
		print 'Eating meat'

class Cat(Animal):
	def run(self):
		print 'Cat is running'
	def eat(self):
		print 'Eating fish'

def eating(animal):
	animal.eat()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

eating(Dog())
