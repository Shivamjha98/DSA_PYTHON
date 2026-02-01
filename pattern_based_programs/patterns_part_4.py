# pattern-19

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

n=5
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    for j in range(2*i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*n-(2+i*2)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()

# pattern-20
# *          *
# **       **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*n-(2*i+2)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end="")
    for j in range(2*n-2*i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# pattern-21
# ****
# *  *
# *  *
# ****
n=4
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*", end="")
        else:
            print(" ",end="")
    print()

# pattern-22
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        down=2*n-1-i
        left=j
        right=2*n-1-j
        print(n-min(min(top, down), min(left, right)), end="")
    print()
