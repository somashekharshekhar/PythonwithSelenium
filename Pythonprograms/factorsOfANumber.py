#program 9
#write a program to determine the factors of a number

value = int(input('enter a number : '))

for i in range(1, value+1):
    if(value % i == 0):
        print(i)
    