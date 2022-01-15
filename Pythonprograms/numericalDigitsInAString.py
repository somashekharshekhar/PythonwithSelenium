#program 15
# how to calculate the number of numerical digits in a string


value = input('enter a string : ')

#using isdigit()
count = 0
for i in value:
    if (i.isdigit()):
        print(i)
        count = count + 1
        
print('total number os digits are ',count)

#using logic

digits = ['0','1','2','3','4','5','6','7','8','9']
count = 0
for i in value  :
    if i in digits:
        print('digits are : ',i)
        count = count + 1
print('total number os digits are :',count)