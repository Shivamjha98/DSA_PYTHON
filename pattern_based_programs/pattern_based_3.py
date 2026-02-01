# pattern 13
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14

n=5
num=1
for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()



# print(ord('A'))
# print(chr(65))

# pattern 14:
# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+j), end="")
    print()


# pattern 15
# ABCDE
# ABCD
# ABC
# AB
# A

for i in range(n):
    for j in range(n-i):
        print(chr(ord('A')+j), end="")
    print()



# # pattern 16
# A
# BB
# CCC
# DDDD

for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+i), end="")
    print()



# pattern 17
#    A
#   ABA
#  ABCBA
# ABCDCBA
for i in range(n):
    # space
    for j in range(n-(i+1)):
        print(" ", end="")

    # increasing
    for j in range(i+1):
        print(chr(ord('A')+j), end="")

    # decreasing
    for j in range(i-1, -1, -1):
        print(chr(ord('A')+j), end="")

    print()


# pattern 18
# E
# DE   i=1
# CDE
# BCDE
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+(n-i+j)), end="")
    print()
