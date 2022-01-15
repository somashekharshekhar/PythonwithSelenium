#program 1
# Write a program to print sum of numbers from 1 to N
#1+2=3 ....1+n=?

#taking the input from the user

num = int(input('enter number to sum :'))
print('entered value is : ',num)

#initialising the sum 
sum = 0

#iteration from 1 to N
for numb in range(1,num+1) :
    sum = sum + numb
    
#printing the sum after summing all the numbers from 1 to n (user given input)
print('sum of 1 to {} numbers is :'.format(num),sum)
