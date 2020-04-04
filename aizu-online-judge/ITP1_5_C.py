m = "#."

while True:
    t, y = map(int, input().split())
    if t == 0 and y == 0:
        break

    for i in range(t):
        if i % 2 == 0:
            n = m
        else:
            n = m[::-1]

        if y == 1:
            print(n[0])
            continue
        
        if y % 2 == 0:
            print(n * (y / 2))
        else:    
            print((n * (y // 2 + 1))[:-1])

    print("")