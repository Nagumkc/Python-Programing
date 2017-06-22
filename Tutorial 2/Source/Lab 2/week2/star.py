a=10
b = 10
for i in range(a):
    for j in range(b):
        print('*' if i in [j] or j == 0 or j==9 else ' ', end='')
    print()