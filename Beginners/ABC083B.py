# -*- coding: utf-8 -*-
max,a,b = map(int, input().split())
amount = 0

for i in range(max + 1):
  	# 数値を1桁づつ分割して和を取得するため
    # 文字列に変換後listで分割、その後合計値取得のためintへ
    val = sum(map(int,list(str(i))))
    if val >= a and val <= b:
        amount = amount + i

print(amount)
