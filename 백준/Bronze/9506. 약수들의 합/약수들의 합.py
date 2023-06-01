while True:
    n = int(input())
    if n == (-1):
        break
    else:
        data = []
        sum = 0
        for i in range(1, n): 
            if n % i == 0:
                data.append(i)
        for i in data: 
            sum += i
        if sum == n:
            print(f'{n} = 1',end = "")
            for i in range(1,len(data)):
                print(f' + {data[i]}',end = "")
            print()
        else:
            print(f'{n} is NOT perfect.')