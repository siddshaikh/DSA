# Rotate Kth Element
# Given an array of integers and a number k, rotate the kth element to the end of the array. The order of the other elements should be maintained.



def rotate_kth(arr,k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]


input = [1,2,3,4,5,6,7,8,9]
output = rotate_kth(input,8)
print("Rotated array",output)