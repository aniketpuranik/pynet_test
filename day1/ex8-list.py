#!usr/bin/env python

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.append(7)

print numbers

numbers.pop(0)
print numbers
print "length is: {}".format(len(numbers))
numbers.sort()
print numbers
