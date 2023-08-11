# Exercise 3:Create a function that takes two strings s1 and s2 as parameters and returns True if s1 is a
# reordering of the characters in s2.
# EX: if s1=”abcde” and s2=”edacb” , the function returns True. If s1=”aabc” and s2=”edabc”, the function returns False.

def reordering(s1, s2):
    if sorted(list(s1)) == sorted(list(s2)):
        return True
    else: 
        return False
    
print(reordering("Marc", "carM"))
print(reordering("Dagher", "marc"))