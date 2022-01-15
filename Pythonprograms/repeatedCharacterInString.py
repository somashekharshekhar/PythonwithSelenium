#program 10
#write a program to get the matching(repeated) characters in a string

value = input(' enter a string ')
 
#print(value.count('u'))

matchingCharacters = set()
for i in value :
    if(value.count(i) > 1):
        matchingCharacters.add(i)

print(matchingCharacters)
        
	