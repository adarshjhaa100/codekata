a = [[1]*5, [2]*5, [3]*5, [4]*5, [5]*5]
# a = [[1]*5]*5
a = [[0]* 5 for _ in range(5)]

# TODO: Complete the function
print(a)
print(len(a))
for i in range(0, len(a)):
    for j in range(0, len(a)):
        if(i<2 and j<2):
            a[i][j] = -3
print(a)