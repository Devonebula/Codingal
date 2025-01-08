#Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    count=0
    for i in s:
        if i in ['a','e','i','o','u']:
            count=count+1
    return count    
print(count_vowels("hello"))
