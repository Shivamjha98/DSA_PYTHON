def binary_search(arr, lower, upper, item):
    if lower <= upper:
        mid = lower+(upper-lower)//2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binary_search(arr, lower, mid-1, item)
        else:
            return binary_search(arr, mid+1, upper, item)
    else:
        return None

# returning None if not found (-1 can be interpreted as last index)
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
item=25
lower=0
upper=len(arr)-1
print(binary_search(arr, lower, upper, item))


def binary_search_loop(arr, lower, upper, item):
    while lower <= upper:
        mid = lower+(upper-lower)//2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            upper = mid-1
        else:
            lower = mid+1
    else:
        return None

# returning None if not found (-1 can be interpreted as last index)
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
item=25
lower=0
upper=len(arr)-1
print(binary_search_loop(arr, lower, upper, item))