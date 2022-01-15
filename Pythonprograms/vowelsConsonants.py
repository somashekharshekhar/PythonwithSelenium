#program 2
#write a program to calculate the number of vowels and consonants in a string

value = input('enter a string :')

vowelsList = ['a','e','i','o','u']
vowelsCount = 0
consonantsCount = 0

for i in value :
    if i in vowelsList :
        vowelsCount = vowelsCount + 1
    else   :
        consonantsCount = consonantsCount + 1

print('number of vowels in {} number of consonants {}'.format(vowelsCount,consonantsCount))