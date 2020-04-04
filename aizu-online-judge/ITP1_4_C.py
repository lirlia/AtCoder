while True:
    a, way, b = input().split()
    a = int(a)
    b = int(b)
    way = str(way)

    if way == "+":
        print(a + b)
    elif way == "-":
        print(a - b)
    elif way == "*":
        print(a * b)
    elif way == "/":
        print(a // b)
    else:
        break
