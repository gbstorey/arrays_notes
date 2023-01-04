def middle(lst):
    #takes in a list and returns a new list that contains all but the first and last elements
    #index the list from 1 to -1
    return lst[1:-1]

test = {
    "list": [1, 2, 3, 4],
    "ans": [2, 3]
}

if middle(test['list']) != test['ans']:
    print(f"Sorry, the test case for {test['list']} failed.")
else:
    print("Congrats, all test cases passed")