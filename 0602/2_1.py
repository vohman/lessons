#!/usr/bin/env python
# coding: utf8

# first lesson

a = 'First Red Second Green'
print( a )

spl = a.split()
print( spl )
spl_a = str.split(a)
print( spl_a )
# почему не надо импортировать модуль string ?
# и не работает string.split(a)

print( a[0], a[6], a[10], a[17] )
print( spl[0][0], spl[1][0], spl[2][0], spl[3][0] )

print( a[len(a)-1] )
print( a[6:10] )
print( a[:6] )
print( a[17:] )

print( a.find( 'Second' )+1 )
print( a[a.find( 'Second' ):] )

b = a[1::2]
print( b )
c = a[::2]
print( c )
print( a[::-1] )


