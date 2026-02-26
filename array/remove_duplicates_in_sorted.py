# Remove duplicates from sorted array

def remove_duplicates(arr):
    if not arr:
        return False
    elif len(arr) == 1:
        return arr

    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
      

input_1 = [1,1,2,2,3,4,5,5]
output = remove_duplicates(input_1)
print(output)