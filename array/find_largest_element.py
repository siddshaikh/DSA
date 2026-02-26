
# find the larges element from given array

def find_largest_element(input_list:[int]):
    if not input_list:
        return 0
    large_elem = input_list[0]
    for elem in input_list:
        if elem > large_elem:
            large_elem = elem
    return large_elem


input_1 = [1,2,3,4,5]         
input_2 = [5,6,2,3]

output = find_largest_element(input_list=input_2)
print(output) 
