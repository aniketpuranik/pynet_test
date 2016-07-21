#!usr/bin/env python


def func(x, y, z=20):
     return x+y+z

output= func(10,20,50)
print output

output=func(x=10, y=20 )
print output

output=func(10, y=20, z=50)
print output

output=func(x='str1', y='str2', z='str3')
print output

x=range(3)
y=range(10,13)
z=range(110,114)

output=func(x,y,z)
print output
