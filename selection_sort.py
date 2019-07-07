"""
Algorithm Name: Selection Sort
The time complexity of above algorithm is log2base(n).
"""


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
last_index = len(nlist) - 1
for i in range(last_index - 1):
    cheaking_index = i
    for j in range(i + 1, last_index):
        if nlist[j] < nlist[cheaking_index]:
            cheaking_index=j

    if cheaking_index !=i:
        nlist[i],nlist[cheaking_index]=nlist[cheaking_index],nlist[i]

print(nlist)