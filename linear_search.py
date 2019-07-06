"""
Algorithm Name: Linear Search
The time complexity of above algorithm is O(n).
"""

# Desired List
arr = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]

# Searching Item
x = 22

found = False

for i in range(len(arr)):
    if arr[i] == x:
        found = True
        print(x, " is found in the list at index ", i)
        break
if found == False:
    print(x, " is not found in the list")
