# Below, you are given a list of scrambled letters. 
# Your task is simply to re-order the letters in the list so when you print(list) it says CodeFlex
# Target Output: 
# ['C', 'o', 'd', 'e', 'F', 'l', 'e', 'x']

# You are NOT permitted to hardcode this. 
# Instead, your code should re-order the list and then output it.

# Good luck!

# your code goes below here!
# ----------------------------------------------------------------
# here is your list!
list = ["o", "e", "F","C", "l", "e", "x", "d"]
# the order list should be arranged in!
order = [3, 0, 7, 1, 2, 4, 5, 6]

# rearrange
list = [list[i] for i in order]

print(list)