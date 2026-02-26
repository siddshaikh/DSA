from array import *

result = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# result1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8.5])
# result2 = array('i', ['a','b'])


for i in range(0,len(result)):
    print(result[i], end=" ")


print('\n')

for i in result:
    print(i)

print('\n')

# array.reverse(result)   reverse the array

# add element at start
# result.insert(1,50)

# add element at end
# result.append(100)


copyArray = array(result.typecode,(x*5 for x in result))


for i in copyArray:
    print(i)



