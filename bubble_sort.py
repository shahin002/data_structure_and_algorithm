"""
Algorithm Name: Bubble Sort
The time complexity of above algorithm is O(n^2).
"""

nlist = [14, 46, 43, 27, 57, 41, 45, 70, 21]
last_index = len(nlist) - 1
for i in range(last_index):
    for j in range(last_index - i):
        if nlist[j] > nlist[j + 1]:
            nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
print(nlist)
