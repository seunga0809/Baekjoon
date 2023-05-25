a, b = input().split()

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

a = a[::-1]
b = int(b)

for i in range(len(a)):
    result += num.index(a[i]) * (b**i)

print(result)