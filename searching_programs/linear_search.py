def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None

# returning None if not found (-1 can be interpreted as last index)
print(linear_search([1,2,3,4,5], 99))
