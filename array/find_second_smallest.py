# find second smallest element in an array


def find_second_smallest(arr:[]):
    if len(arr) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

    return second_smallest if second_smallest != float('inf') else None


# Example usage
arr = [5, 2, 9, 1, 5, 6,1.5]
result = find_second_smallest(arr)
print("Second smallest element is:", result)