#program 5
# write a program to check whether a number is armstrong
#153 -> 1^3 + 5^3 + 3^3 = 153
#if each number itself cubed and added should get the same value than it is armstrong
''' type 1
value = int(input('enter the number:'))
print('entered number is', value)

#integer is not iterable
#for i in value :
 #   print(i)

toString = str(value)
sum = 0
total = 0
# using iteration
for i in toString:
    i = int(i)
     
    #sum = i * i * i
    #total = total + pow(i,3)
    total = total + (i**3)
#print('total',total)

if value == total :
    print('given number is armstrong',value)
else:
    print('given number is not armstrong',value)'''
    

#type 2, 153,371,1634
value = int(input('enter a number :'))
values = value
total = 0
while(value>0):
    num = value%10
    total = total + pow(num,3)
    value = value // 10
    print(value)
print(total)
    
    
if values == total:
    print('armstrong')
else:
    print(' not armstrong')