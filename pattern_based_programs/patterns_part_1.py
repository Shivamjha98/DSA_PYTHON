# pattern 1: square pattern

# *****
# *****
# *****
# *****
# *****

# first loop for rows
# second loop for columns
# find synergy between rows and columns
# print character or number in inner loop

n=int(input())
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# pattern 2 - right angle triangle
# *
# **
# ***
# ****
# *****

# n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

# pattern - 3 number based rt. angle triangle
# 1
# 12
# 123
# 1234
# 12345

# n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print()

# pattern 4
# 1
# 22
# 333
# 4444
# 55555

# n=int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1, end="")
    print()

# pattern 5 (reverse rt. angle triangle)
# *****
# ****
# ***
# **
# *
# n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

# pattern 6 -
# 12345
# 1234
# 123
# 12
# 1
# n=int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()
