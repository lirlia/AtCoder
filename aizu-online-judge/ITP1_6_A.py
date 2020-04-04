a = input()
b = list(map(int, input().split()))

print(" ".join(map(str,b[::-1])))
