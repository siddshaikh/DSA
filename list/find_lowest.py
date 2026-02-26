unsorted_list = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]

output = unsorted_list[1]


for i in unsorted_list:
    if i < output:
        output = i
print(output)



# dont give suggestions please wait let me try from my side


second_list = [10, 2, 3, 4, 5, 6, 7, 8, 9,0]

second_output = second_list[5]



for item in second_list:
    if item < second_output:
        second_output = item

print(second_output) 


# find second lowest number in the list

third_list = [10, 3, 4, 5, 6, 7, 8, 9, 1]

min1 = float('inf')
min2 = float('inf')

for item in third_list:
    if item < min1:
        min2 = min1
        min1 = item
    elif item < min2 and item != min1:
        min2 = item

print(min2)



# find second lowest number

fourth_list = [10, 3, 4, 5, 6, 7, 8, 9, 1]

min1 = float('inf')
min2 = float('inf')

for item in fourth_list:
    if item < min1:
        min2 = min1
        min1 = item
    elif item < min2 and item != min1:
        min2 = item
print(min2)


# find third lowest number
fifth_list = [10, 3, 4, 5, 6, 7, 8, 9, 1]


min1 = float('inf')
min2 = float('inf')
min3 = float('inf')

for item in fifth_list:
    if item < min1:
        min3 = min2
        min2 = min1
        min1 = item
    elif item < min2 and item != min1:
        min3 = min2
        min2 = item
    elif item < min3 and item != min2 and item != min1:
        min3 = item
print(min3)
