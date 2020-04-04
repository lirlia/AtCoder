import math
a, b = map(int, input().split())

tax8 = math.floor(a/0.08)
tax10 = math.floor(b/0.1)


if math.floor(tax8 * 0.08) != a or math.floor(tax10 * 0.1) != b:
    print(-1)
    exit(0)

cnt = 0
while True:
    cnt = cnt + 1
    if math.floor((tax8 + cnt) * 0.08) != a:
        tax8max = tax8 + cnt - 1
        break

cnt = 0
while True:
    cnt = cnt + 1
    if math.floor((tax8 - cnt) * 0.08) != a:
        tax8min = tax8 - cnt + 1
        break

cnt = 0
while True:
    cnt = cnt + 1
    if math.floor((tax10 + cnt) * 0.1) != b:
        tax10max = tax10 + cnt - 1
        break

cnt = 0
while True:
    cnt = cnt + 1
    if math.floor((tax10 - cnt) * 0.1) != b:
        tax10min = tax10 - cnt + 1
        break

tax8s = set(range(tax8min, tax8max))
tax10s = set(range(tax10min, tax10max))
taxl = sorted(list(tax8s & tax10s))

if taxl == []:
    print(-1)
    exit(0)

print(taxl[0])
