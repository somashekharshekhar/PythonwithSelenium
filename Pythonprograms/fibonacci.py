#program 11
#Write a program to print fibonacci sequence or series

value = int(input('enter a number :'))

#0,1,1,2,3,5,8,13,21,33,54

n1 = 0
n2 = 1
count = 0
if value <= 0:
    print('invalid number')
elif value == 1:
    print('fibonacci series of 1 is 0')
else:
    while(count < value):
        print(n1)
        nextElement = n1 + n2
        n1 = n2
        n2 = nextElement
        count = count + 1
