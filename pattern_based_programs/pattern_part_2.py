# pattern 7:
 #    *
 #   ***
 #  *****
 # *******
 #*********


n=5
for i in range(n):

    # spaces
    for j in range(n-(i+1)):
        print(" ", end="")

    # character - star
    for j in range(2*i+1):
        print("*", end="")

    # spaces
    for j in range(n-(i+1)):
        print(" ", end="")

    print()


# pattern-8
# *********
#  *******
#   *****
#    ***
#     *
#
for i in range(n):

    #spaces
    for j in range(i):
        print(" ", end="")

    # stars
    for j in range(2*n-(2*i+1)):
        print("*", end="")

    # spaces
    for j in range(i):
        print(" ", end="")

    print()


# pattern- 9 = pattern 7 + 8
 #    *
 #   ***
 #  *****
 # *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


for i in range(n):

    # spaces
    for j in range(n-(i+1)):
        print(" ", end="")

    # character - star
    for j in range(2*i+1):
        print("*", end="")

    # spaces
    for j in range(n-(i+1)):
        print(" ", end="")

    print()

for i in range(n):

    #spaces
    for j in range(i):
        print(" ", end="")

    # stars
    for j in range(2*n-(2*i+1)):
        print("*", end="")

    # spaces
    for j in range(i):
        print(" ", end="")

    print()

# pattern 10
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# pattern 11
# 1
# 01
# 101
# 0101
# 10101

for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2, end="")
    print()


# pattern 12->
# 1      1
# 12    21
# 123  321
# 12344321

n=4
for i in range(n): # i=1
    # first char
    for j in range(i+1):
        print(j+1, end="")
    #spaces
    for j in range(2*n-(2*(i+1))):
        print(" ", end="")
    # next char
    for j in range(i+1,0,-1):
        print(j, end="")
    print()

