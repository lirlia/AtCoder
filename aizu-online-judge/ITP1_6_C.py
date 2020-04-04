n = int(input())
w = [[[0]*10 for _ in range(3)] for _ in range(4)]
#[[[0]*10]*3 for i in range(4)]

for i in range(n):
    b, f ,r, v = map(int, input().split())
    w[b - 1][f - 1][r - 1] = w[b - 1][f - 1][r - 1] + v

cnt = 0
for i in w:
    cnt = cnt + 1
    for j in range(3):
        print(" " + " ".join(map(str, i[j])))
    
    if len(w) != cnt:
        print("#" * 20)