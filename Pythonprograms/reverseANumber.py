#program 8 
# write a program to reverse a number without using string 

value = int(input('enter a number :'))
numOriginal = value
#n =135
#5   5*10+3 =53
#53  53*10 = 530
#531 530 +1 = 531

reverse = 0
while( value > 0):
    num = value % 10
    reverse = reverse * 10 + num 
    value = value // 10
print(' reverse of number {} is {} .' .format(numOriginal,reverse))

