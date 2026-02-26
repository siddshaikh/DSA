# Bubble sort repeatedly steps through the list, compares adjacent element, and swap them if they are wrong order
# Each pass through the list "bubbles" the largest element to the end - like bubble rising water.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [22,10,12,19,6,3,9]
result = bubble_sort(arr)
print("bubble sort result",result)



