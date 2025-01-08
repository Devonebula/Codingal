#Write a function are_anagrams(s1, s2) that checks if two strings s1 and s2 are anagrams of each other.
def anagrams(s1,s2):
    for i in s1:
        if i in s2:
            return True
    return False

s1=input("Enter the first string:\t")
s2=input("Enter the second string:\t")
print(anagrams(s1,s2))