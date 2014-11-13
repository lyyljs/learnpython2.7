# print all names in order
names = ['lyy','ljs','floyd']
for name in names:
	print name

# sum 1 - 10
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print sum

# sum 1 - 100
sum = 0
for x in range(101):
	sum = sum + x
print sum

# sum odd in 1 - 100
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print sum
