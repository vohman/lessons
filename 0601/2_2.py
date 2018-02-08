#!/usr/bin/env python
# coding: utf8

# first lesson

a, b = 3, 8
print('a', a, 'b', b)

c = a % 2
d = b % 2
e = c + d
print('c', c, 'd', d, 'e', e)

a = str(a)
print(a)
b = str(b)
print(b)
c = a + b
print('c=', c)

l = list(a) + list(b)
c = ''.join(l)
print('c=', c, type(c))

a = int(c)
print(a, type(a))
a = a*2
print(a)

