# Check the given array is sorted or not

def is_sorted(arr):
    if not arr:
        return None
    elif len(arr) == 1:
        return arr
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
        

input_1 = [7,2,3,4,5,6]
input_2 = [1,2,3,4,5,6]
output = is_sorted(input_2  )
print(output)        