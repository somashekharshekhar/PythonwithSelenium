#program3
# write a program to check the string is palindrome or not
# madam,level,mom,dad reverse is also same old string  

value = input('enter the string to check palindrom or not :')
print('entered string is :',value)

#reversing the string
rev = ""
for name in value :
    rev = name + rev

print('reversed string is : ',rev)

if rev == value :
    print(" entered string is palindrom")
else:
    print(" entered string is not a palindrome")