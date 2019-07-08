"""
Algorithm Name: Insertion Sort
The time complexity of above algorithm is O(n^2).
"""

nlist = [46, 14, 43, 27, 57, 41, 45, 70, 21]
for index in range(1, len(nlist)):
    currentValue = nlist[index]
    position = index
    while position > 0 and nlist[position - 1] > currentValue:
        nlist[position] = nlist[position - 1]
        position = position - 1
    nlist[position] = currentValue

print(nlist)
