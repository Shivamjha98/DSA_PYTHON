arr=[7,3,11,6,4,1]


for i in range(1, len(arr)):
    min_index=i
    current_element=arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] > current_element:
            min_index=j
            arr[j+1] = arr[j]
        else:
            break
    arr[min_index]=current_element

print(arr)
