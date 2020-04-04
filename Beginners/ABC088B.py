# -*- coding: utf-8 -*-
#
# 全てのカードを降順に並べ、偶数番目をAliceが引き、
# 奇数番目をBobが引くことになるのでその合計から差を出す
#

num = int(input())
cards = map(int, input().split())
cards = sorted(cards, reverse = True)

# alice cards
aliceAmount = sum(cards[0::2])

# bob cards
bobAmount = sum(cards[1::2])

print(aliceAmount - bobAmount)
