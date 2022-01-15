#program 13
#write a program to check if two strings are anagrams?

#two strings are said to be anagram if we can form the first string by arranging the characters of another string
#surya,yasur

value1 = input('enter first strings : ')
value2 = input('enter second string : ')

# sorting both string , if both are same then they said to be anagrams

if len(value1) == len(value2):
    if(sorted(value1) == sorted(value2)):
        print('entered strings are anagrams')
    else:
        print(' these are not anagrams')
else:
    print(' these are not anagrams')