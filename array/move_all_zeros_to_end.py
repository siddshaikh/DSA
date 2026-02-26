# Move all given zeros to end

def move_zeros_to_end(arr):
    l = len(arr)
    i = 0

    for j in range(l):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr



input = [2,0,3,4,0,5,6,0]
output = move_zeros_to_end(input)
print("Here is the output",output)