while True:
    t, y = map(int, input().split())
    if t == 0 and y == 0:
        break
    for i in range(t):
        print("#"*y)
    print("")