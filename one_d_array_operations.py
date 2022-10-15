from array import *

# arr1 = array('i', [1,2,3,4,5,6])
# arr2 = array('d', [1.3, 1.5, 1.6])

#insertion ; O(n) worst case, O(1) best case, O(n) if new array must be created no matter index
# arr1.insert(0,0)

#traversal ; O(n) for full array
def traverseArray(array):
    for i in array:
        print(i)
#traverseArray(arr1)

#accessing element ; O(1) time and space complexity
def accessElement(array, index):
    if index >= len(array):
        print('Element does not exist.')
    else:
        print(array[index])
# accessElement(arr1, 6)

#locating element ; O(n) time complexity, O(1)_space complexity
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value) # O(n) time complexity
    return "The element does not exist in this array."
# print(searchInArray(arr1, 3))

#deleting element ; O(n) time complexity, O(1) space complexity
#arr1.remove(4)
#print(arr1)


#1. Create an array and traverse.
my_array = array('i', [1,2,3,4,5])
# for i in my_array:
#     print(i)

#2. Access individual elements through indices.
# print(my_array[0])

#3. Append any value to the array using append().
# my_array.append(6)
# print(my_array)

#4. Insert value in an array using the insert() method
# my_array.insert(0,0)
# print(my_array)

#5. Extend python array using extend() method
# my_array2 = array('i', [10,11,12])
# my_array.extend(my_array2)
# print(my_array)

#6 Add items from list into array using fromList() method
# tempList = [20, 21, 22]
# my_array.fromlist(tempList)
# print(my_array)

#7 Remove an array element using remove() method
# my_array.remove(1)
# print(my_array)

#8. Remove last array element using pop() method
# my_array.pop()
# print(my_array)

#9. Fetch any element through its index using the index() method
# print(my_array.index(5))

#10. Reverse a python array using reverse() method
# my_array.reverse()
# print(my_array)

#11. Get array buffer information through buffer_info() method
# print(my_array.buffer_info())

#12. Check for number of occurences of an element using count()
# print(my_array.count(2))

#13 Convert array to string using tostring() method
# strTemp = my_array.tobytes()
# print(strTemp)
# ints = array('i')
# ints.frombytes(strTemp)
# print(ints)

#14. Convert array to list using tolist() method
# my_list = my_array.tolist()
# print(my_list)

#15. Slice elements from an array
# print(my_array[0:2])
