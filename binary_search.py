"""
Algorithm Name: Binary Search
The time complexity of above algorithm is log2base(n).
"""

item_list = [1, 2, 3, 5, 8]
item = 5

first = 0
last = len(item_list) - 1
found = False
while (first <= last and not found):
    mid = (first + last) // 2
    if item_list[mid] == item:
        found = True
        print(item, " is found in the list at index ", mid)
        break
    else:
        if item < item_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

if found == False:
    print(item, " is not found in the list")
