#program 14
#find the count for the occurrence of a particular character in a string

value = input('enter the string :')
value2 = input('enter character to count :')

print(value.count(value2))

count = 0

for i in value:
    if i == value2:
        count = count + 1
print('entered character "{}" occurred "{}" times'.format(value2,count))