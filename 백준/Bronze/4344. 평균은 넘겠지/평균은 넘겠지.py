C = int(input())

for i in range(C):
    count = 0
    M = list(map(int, input().split()))

    mean = sum(M[1:]) / M[0]

    for j in M[1:]:
       if j > mean:
           count += 1

    print('{:.3f}%'.format(count / M[0] * 100))