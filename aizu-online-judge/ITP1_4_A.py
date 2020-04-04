import math
a, b = map(int, input().split())

waru = a//b
amari = a - waru * b
#https://www.sejuku.net/blog/73255
waru_s = format(a/b, "f")

print(waru,amari,waru_s)