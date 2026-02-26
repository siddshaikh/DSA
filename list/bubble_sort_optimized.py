# Optimized version - if no swaps happen in a pass - list is already sorted -> stop early


def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n- i -1):
            if arr[j] >  arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break    
    return arr

arr = [9,8,7,6,5,4,3,2,1,0]
result = bubble_sort_optimized(arr)
print(result)