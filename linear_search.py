"""
Algorithm Name: Linear Search
The time complexity of above algorithm is O(n).
"""


def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
search_item = 21
result = search(nlist, search_item)
if result == -1:
    print(search_item, " is not in the list")
else:
    print(search_item, " is found in the list at index ", result)
