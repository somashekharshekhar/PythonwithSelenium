#program 16
#find the first character of string that is not repeated

value = input('enter a string :')

#using count
for i in value :
    if value.count(i) == 1 :
        print('first non repeated character is: ' ,i)
        break
print()
        
'''      
#using sets try again
 
name = set()
for i in value :
    name.add(i)

print(name[-1])

'''

foundNonRepeated = False
while value!="":
    originalNameLen = len(value)
    char = value[0]
    value = value.replace(char,'')
    afterReplaceLen = len(value)
    if(originalNameLen-1 == afterReplaceLen):
        print('first non repeated character is ', char)
        foundNonRepeated =True
        break
if(foundNonRepeated == False):
    print('no non repeated character')