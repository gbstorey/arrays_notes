import numpy as np

twoDArray = np.array([ #complexity with new values: O(mn)
[11,15,10,6],
[10,14,11,5],
[12,17,12,8],
[15,18,14,9]
])

#insertion
#adding column: o(mn)
# newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
# print(newTwoDArray)
#adding row: o(mn)
# newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0)
# print(newTwoDArray)
#append row/column: o(1)
# newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

#accessing element; i = row index, j = column index: a[i][j]
# time complexity: O(1) space complexity: O(1)
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])
# accessElements(twoDArray, 1, 2)

#traversal: O(mn)
# for i in twoDArray:
#     for j in i:
#         print(j)

#searching: O(mn)
# def searchTDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return 'The value is located at index ' + str(i) + " " + str(j)
#       return 'The element is not found'
# print(searchTDArray(twoDArray, 14))

#deletion: O(mn), space complexity = O(1)
newTDarray = np.delete(twoDArray, 0, axis=0)
print(newTDarray)