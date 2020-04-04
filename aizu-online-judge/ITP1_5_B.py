while True:
    t, y = map(int, input().split())
    if t == 0 and y == 0:
        break
    for i in range(t):
        if i == 0 or i == (t - 1):
            print("#"*y)
        else:
            print("#{}#".format("."* (y - 2)))

    print("")