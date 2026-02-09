a=[2,25,8,10]

# bubble sort
for i in range(len(a)-1):
    print(i)
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

# modified bubble sort:
for i in range(len(a)-1):
    print(i)
    is_swapped=False
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            is_swapped=True
    if not is_swapped:
        break

print(a)
