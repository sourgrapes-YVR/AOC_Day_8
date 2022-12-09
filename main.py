import numpy as np

f = open("/Users/davidbrown/PycharmProject/AOC Day 8/data")
fred = f.read().splitlines()
trees = np.array([[int(y) for y in list(x)] for x in fred])
rows, cols = trees.shape
treechart = np.zeros(trees.shape)
count = 0

def lookaround(x):
    if treechart[i,j] == 1:
        return True
    biggest = x.max(initial=0)
    # print("Number is",num, "position of number is:", i, j ,"max is:", biggest, "range is:", x)
    if num > biggest:
        treechart[i, j] = 1
        # print(treechart)
        # return("yay")
    elif num == 0 and num == biggest:
        treechart[i, j] = 1
        # print(treechart)

for i in range(rows):
    for j in range(cols):
        num = trees[i, j]
        lookL = trees[i,:j]
        lookR = trees[i,j + 1:]
        lookU = trees[:i, j]
        lookD = trees[i + 1:, j]
        if lookaround(lookL) is not True:
            if lookaround(lookR) is not True:
                if lookaround(lookU) is not True:
                    if lookaround(lookD) is not True:
                        continue

print(treechart)
print(np.sum(treechart))