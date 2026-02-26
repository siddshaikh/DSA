# count a frequency of the each element in given array and return a dictionary.


def count_frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

inp = [1,2,3,4,5,6,1,2]            
output = count_frequency(inp)
print(output)
