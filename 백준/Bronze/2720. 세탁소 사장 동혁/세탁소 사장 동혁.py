for i in range (int(input())):
    coin = int(input())
    
    a = coin // 25
    b = (coin % 25) // 10
    c = ((coin % 25) % 10) // 5
    d = (((coin % 25) % 10) % 5) // 1
    print(a,b,c,d)