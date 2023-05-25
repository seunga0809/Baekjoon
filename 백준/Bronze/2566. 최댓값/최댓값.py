Max = 0
B = 0
C = 0
for i in range(9):
    A = list(map(int, input().split()))
    if Max <= max(A):
        Max = max(A)
        B = i + 1
        C = A.index(Max) + 1
        
print(Max)
print(B, C)