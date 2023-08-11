# Exercise 5 Write a function that counts the digits of a given number recursively.
# Ex: input= 123 output : 3, input 10000 output:5

def recursive_counter(n, count = 0):

    if abs(n) < 10:
        return 1 + count
    else: 
        n = n // 10
        return recursive_counter(n, count + 1)

print(recursive_counter(2984))