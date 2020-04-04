# -*- coding: utf-8 -*-
N, Y = map(int, input().split())

if N * 1000 == Y:
    print("0 0 {}".format(N))
    exit(0)

if N * 5000 == Y:
    print("0 {} 0".format(N))
    exit(0)

if N * 10000 == Y:
    print("{} 0 0".format(N))
    exit(0)

tmp = Y - 1000 * N

for i in range(N):
    man = i
    gosen = (tmp - 9000 * i) // 4000
    sen = (Y - (5000 * gosen) - (10000 * man))//1000

    if gosen < 0 or sen < 0 or gosen > N or sen > N:
        continue

    if (tmp - 9000 * i) % 4000 == 0:
        print(man, gosen, sen)
        exit(0)

print('-1 -1 -1')