#program 19
# write a program to determine the largest and the smallest element of an array which is not sorted

#[12,10,9,44,88] - > 9,88

numbers = [77,4,33,66,2,3,8,99]

#using min and max
print('min : ',min(numbers))
print('max : ',max(numbers))

#sorted array
numbers.sort()

print('min :',numbers[0])
print('max :',numbers[-1])

#using logic
small = numbers[0]
large = numbers[0]
length = len(numbers)
for i in range(1,length):
    if(small > numbers[i]):
        small = numbers [i]
    if(large < numbers[i]):
        large = numbers[i]
print('small :',small)
print('large :',large)
    
        