def merge_two_sorted_list(left_arr, right_arr, arr):
    # sorted_list=[]
    i=j=k=0

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            # sorted_list.append(left_arr[i])
            i+=1
        else:
            arr[k] = right_arr[j]
            # sorted_list.append(right_arr[j])
            j+=1
        k+=1

    while i<len(left_arr):
        arr[k] = left_arr[i]
        # sorted_list.append(left_arr[i])
        i+=1
        k+=1

    while j< len(right_arr):
        arr[k] = right_arr[j]
        # sorted_list.append(right_arr[j])
        j+=1
        k+=1

    return arr

# left_arr=[1, 3,15, 17,21,29,38]
# right_arr=[4,9, 25,32]
# print(merge_two_sorted_list(left_arr, right_arr))


def merge_sort(arr):

    if len(arr)<=1:
        return arr

    mid=len(arr)//2   # 4  # 2 # 1
    # left=0
    # right=len(arr)-1
    # mid=left + (right-left)//2

    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)

    return merge_two_sorted_list(left_arr, right_arr, arr)

print(merge_sort([7,2,8,9]))
