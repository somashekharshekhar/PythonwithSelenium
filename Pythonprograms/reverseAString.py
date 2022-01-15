#program2
#write a program to reverse a String

value = input('enter a string to reverse :')

print('Given String is :' ,value)

#using slicing default function
print(value[::-1])

#using control statements
rev = ""
for name in value :
   print(name)
   rev = name + rev #name + rev( name is added before rev. latest character is added in the begining , here first added character will be in last, hence reversed

print('revese of string is :',rev)
   
   