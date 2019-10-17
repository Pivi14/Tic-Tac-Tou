a = [[1, [0,2]], [2, [0,1]], [-2, [0,1]], [0, [3,1]], [-1, [2,0]]]

a.sort(reverse=True)
if a[0][0] == 2:
    line = a[0][1:]
elif a[0][0] == -2:
    line = a[0][1:]
elif a[0][0] == 1:
    line = a[0][1:]
elif a[0][0] == 0:
    line = a[0][1:]
elif a[0][0] == -1:
    line = a[0][1:]
print(a)
print(line)
