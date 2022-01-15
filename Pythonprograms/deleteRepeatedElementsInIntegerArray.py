#program 18
#write a program to delete the repeated elements in an integer array

#[1,2,3,3,5,8,2] -> [1,2,3,5,8]

#list
numbers = [1,2,3,3,5,8,2] 

#convert list to set

print(set(numbers))

numbers = [1,2,3,3,5,8,2] 

num = []

for i in numbers :
    if(i not in num):
        num.append(i)
print('after removing duplicates : ',num)
