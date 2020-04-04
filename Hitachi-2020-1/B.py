A, B , M = map(int, input().split())
a = list(map(int, input().split()))
a_s = sorted(a)
b = list(map(int, input().split()))
b_s = sorted(b)

# cheapest
cheap = a_s[0] + b_s[0]

for i in range(M):

    # discount
    x, y, c = map(int, input().split())
    dis_cheap = a[x - 1] + b[y - 1] - c

    if cheap > dis_cheap:
        cheap = dis_cheap

print(cheap)

