# linear search implementation in Python

def linear_search(list_items=[int], target=int) -> int:
    for i in range(len(list_items)):
        if list_items[i] == target:
            return i
 
    return -1
        

list_items = [2,8,14,4,33,1]
target = 33

print(linear_search(list_items, target))


