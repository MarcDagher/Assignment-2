# Out of bounds when: 
# - index surpassed the list
# - index is before the loop - less than 0
# Cycle when:
# - when we return to the same index multiple times
# - element == 0

def list_jumps(jumps):
    # Out of bounds:
    index = 0
    count_of_index = {}
    while index < len(jumps) and index >= 0: #if index surpasses the end or preceeds the start = out-of-bounds
        
        if jumps[index] == 0: # if we are adding 0
            return "Cycle"
        
        if index in count_of_index: # if we returned to the same index add 1 if not keep track of indicies reached
            count_of_index[index] += 1
        elif index  not in count_of_index:
            count_of_index[index] = 1
        
        if count_of_index[index] > 2: # if we returned to the same index more than 2 times
            return "Cycle"

        index += jumps[index]

    return "Out-of-Bounds"

list1 = [0] # cycle
list2 = [1] # out
list3 = [1, -1] # cycle
list4 = [-1] # out
list5 = [3, 1, 1, 2, -1, 2, 2, -1, 1, -2] # cycle
list6 = [3, 1, 2, -1] # out

print(list_jumps(list6))