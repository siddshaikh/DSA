# The frequency of an element in an array is the number of times it appears in the array.



def max_frequency(nums:list[int],k:int):
    nums.sort()
    left = 0
    total = 0
    max_freq = 0
    for right in range(len(nums)):
        total += nums[right]

        while nums[right] * (right - left + 1) - total > k:
            total -= nums[left]
            left += 1
        max_freq = max(max_freq, right-left+1)
    return max_freq

nums = [1,2,4]
k = 5
output = max_frequency(nums=nums,k=k)
print(output)          