# program 17
#find missing number in an array that contains integers from 1 to 100
#total sum without missing number - total sum with missing number = remainder is missing number
#num = int(input('enter a number'))
numbers = [1,2,3,4,6,7,8,9,10]
n = len(numbers)+1
total = n*(n+1)//2
print('total sum is : ', total)
sum = 0
for i in numbers :
    sum = sum+i
print('missing number is :', total-sum)

