# Exercise 1: Create a function that takes a string s and an integer i as parameters and returns a string that
# ~~~~~~~~~~  has in it s reversed and concatenated i times.

def concatinate(s, i):
    def recursive_reverse(s):
        if len(s) == 0:
            return s

        last_letter = s[-1]
        remaining_string = s[0 : -1]

        return last_letter + recursive_reverse(remaining_string)

    answer = recursive_reverse(s)
    return answer * i 

# print("Enter any word and any number")
# s = str(input("Word: "))
# while type(s) != str:
#     print("Invalid. Re-enter word.")
#     print("Enter any word: ")
#     s = str(input("Word: "))

# i = int(input("Number: "))
# while type(i) != int:
#     print("Invalid. Re-enter Number.")
#     print("Enter any number: ")
#     s = str(input("Number: "))

# print(concatinate(s, i))