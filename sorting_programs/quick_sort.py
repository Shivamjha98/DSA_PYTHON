def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot=arr[0]
    # smaller=[]
    # larger=[]
    # for i in arr[1:]:
    #     if i<pivot:
    #         smaller.append(i)
    #     else:
    #         larger.append(i)

    smaller=[i for i in arr[1:] if i<pivot]
    larger=[i for i in arr[1:] if i>pivot]

    print(smaller, pivot, larger)
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

arr=[6,3,11,12, 7,4,1]
print(quick_sort(arr))