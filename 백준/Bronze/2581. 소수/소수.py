N = int(input())
M = int(input())
L = []

for i in range(N, M+1):
    for j in range(2, i+1):
        if i == j:
            L.append(i)
        
        if i % j == 0:
            break


if not L:
    print('-1')

else:
    print(sum(L))
    print(min(L))