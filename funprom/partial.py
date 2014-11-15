import functools

int2 = functools.partial(int,base=2)

print int2('1000')
print int2(raw_input('input a binary\n'))
