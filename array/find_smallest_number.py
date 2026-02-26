# Find smallest number in an array


def finds_smallest_number(input_list:[int]):
    if not input_list:
        return None
    smallest_number = input_list[0]

    for elem in input_list[1:]:
        if elem < smallest_number:
            smallest_number = elem
    return smallest_number


input_1 = [-2,1,4,5,6,4]
input_2 = [-2,3,12,23,1]

output = finds_smallest_number(input_list=input_2)
print("output is here",output)