# Binary search works only on sorted lists
# 1> Start with two pointer  - low (start of the list) and end (end of the list)
# 2> find the middle index
# 3> Compare the middle element with the target.
#    A> If it matches  ->  Element found
#    B> If the target is smaller -> search left
#    c> If the target is large ->  search right
# Repeat until element found or low >  high
 

# def binary_search(arr=[int], target=int):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2 # find the middle index (element)
#         if arr[mid] == target:
#             return mid # return mid if matches with the target
#         elif arr[mid] < target:
#             low = mid + 1 # Go for the left side if the target is lower than mid
#         else:
#             high = mid - 1 # Go for the right side if the target higher than mid
#     return -1   


# arr = [10,20,30,40,50,60,70,80,90,100]

# target = 60

# print(binary_search(arr,target))



def binary_search(arr=[int], target=int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1,2,3,4,5,6,7,8,9]

target = 5

print(binary_search(arr, target))

