# find the second largest element in an array

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None



input_arr = [1,2,3,4,5,6,7]
result = find_second_largest(input_arr)
print("second largest element",result)
