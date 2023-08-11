def list_jumps(jumps):
    index = sum(jumps)

    if index < 0 or index > len(jumps):
      return "out-of-bounds"
    else:
       return "cycle"
    
print(list_jumps([1,2,3,4, -5 ]))