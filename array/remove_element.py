# Remove element from array and return new length of array

def remove_elem(nums:list[int],elem:int):
    length = 0
    for i in range(len(nums)):
        if nums[i] != elem:
            nums[length] = nums[i]
            length += 1
    return length


input = [0,1,2,2,3,0,4,2]
print(remove_elem(input,2))
         