# -*- coding: utf-8 -*-
# a ¥500, b ¥100, c ¥50
a, b, c, mount = map(int, [input() for i in range(4)])
cnt = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if (i * 500 + j * 100 + k * 50) == mount:
                cnt = cnt + 1
print(cnt)
