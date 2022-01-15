#program 7
#write a program to swap two numbers without using temporary(third) variable

#using temporary variable


a = 10
b = 20
# using temp variable 
temp = a
a = b
b = temp 

print(' a = {}  b = {} '.format(a,b))

a = 10
b = 20
a = a + b  #30
b = a - b  #30 - 20 = 10
a = a - b  #30 - 10 = 20

print(' a = {}  b = {} '.format(a,b))

