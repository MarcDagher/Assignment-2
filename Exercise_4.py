# Exercise 4: Python has an inbuilt function called max() that returns the element with the maximum value.
# Create a function that does a very similar thing (without using the max() function). The function takes a list of numbers l as a parameter and returns the highest number in the list and its index.
# EX: if l = [5,6,3,2,7,2,0,1,6], the function should return “the highest value in the list is 7 at
# index 4”
# (BONUS: do the same but for the minimum)

def maximum(l): # Simple way
    sorted_list = sorted(l)
    return sorted_list[-1]


def maximum_recursive(l): # Recursive Way
  def move_max_to_the_end(l, index = 1):
    if len(l) == index:
      return l
    else:
        if l[index] > l[-1]:
          l[-1] = l[index]
        elif l[index] < l[0]:
           l[0] = l[index]
    return move_max_to_the_end(l, index+1)
  
  return move_max_to_the_end(l)[-1]
  

l = [ 10, 20, 50, 99, 1, 5]
print(maximum_recursive(l))