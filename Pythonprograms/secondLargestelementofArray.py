#program 20
#write a program to determine the second largest element of an array

#[1,2,3,4,5] -> 2

numbers = [6,2,3,4,5]

#using sort
numbers.sort()
print('second large',numbers[-2])

numbers = [6,2,3,4,5]

fstmax = max(numbers[0],numbers[1])
secmax = max(numbers[0],numbers[1])

length = len(numbers)
for i in range(2,length):
    if(numbers[i]>fstmax):
        secmax=fstmax
        fstmax =numbers[i]
    elif(numbers[i]>secmax):
        secmax=numbers[i]

print('second largest number is',secmax)
        