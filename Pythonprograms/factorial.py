# program 4
# write a program to find the factorial of a number
# factorial of 0 is 1
# 5! =120, 5*4=20, 20*3=60, 60*2=120, 120*1=120
# 5*4*3*2*1

value = int(input('enter the number : '))

print('entered number is : ',value)

if value < 0 :
    print('invalid numer')
elif value==0:
    print('factorial of 0 is 1')
else:
    mul = 1
    for i in range(1,value+1):
        mul = mul * i

print('factorial of {} is {} '.format(value,mul) )      
