# recursive binary search



def recursive_binary_search(arr,low,high,target):
    # base case: range exhausted
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        # search the left half: low .. mid-1
        return recursive_binary_search(arr, low, mid - 1, target)


arr = [10,20,30,40,50,60,70,80,90]
target = 30

result = recursive_binary_search(arr,0, len(arr)-1,target)

print("The final result:",result)