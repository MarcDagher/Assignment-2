# Exercise 2: Create a function that takes a string s as a parameter and returns another string where all
# ~~~~~~~~~~  the letters in s has been re-arranged such that upper case letters appear before the lower case letters.
#             EX: if s is “Hello World”, the function returns “HWelloorld”.

#QUESTION: When I want to adjust a string while iterating over it, is it better to have another empty list?

# Or we can simply print("".join(sorted(s)))
def recursive_capital_letters(s, index=0):
    s = list(s)
    
    if len(s) == 0 or len(s) == 1:
        return s 
    if len(s) != index:  #To iterate over the list
        letter = s[index]
        if letter == " ":
            s.pop(index)
            return recursive_capital_letters(s, index - 1)

        elif ord(letter) > 64 and ord(letter) < 91:
            s.pop(index)
            s.insert(0, letter)         
            
    else: # To stay in the range of the list
        return s
    return recursive_capital_letters(s, index + 1)

answer = recursive_capital_letters("aABa")
print("".join(answer))
answer = recursive_capital_letters("Marc Dagher")
print("".join(answer))