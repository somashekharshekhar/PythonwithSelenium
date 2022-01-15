#program 6
#write a program to print numbers from 1 to 100
# 1 is not a prime number
value = 100
primeNumber = []
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
           break
    else:
        print(i)
        primeNumber.append(i)

print('number of prime numbers in 1 to 100 is :', len(primeNumber))

'''
for i in range(1,10):
    print(i)
    if i == 5 :
        break
else:
    print('else stme')'''