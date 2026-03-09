# search the insertion position of the target in given array

def search_insert_position(nums:list[int],target:int):
    left, right = 0 , len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] ==  target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left   


input = [1,3,5,6]
target = 5
print(search_insert_position(input,target))
