# -*- coding: utf-8 -*-
a = int(input())
b = list(map(int, input().split()))
cnt = 0
even = [1, 3, 5, 7, 9]

while True:

  # 配列の各値の一桁目を取得
  lastVal = map(lambda x: int(str(x)[-1]), b)

  # 一桁目が奇数の場合処理を終了する
  if not set(even).isdisjoint(set(lastVal)):
    print(cnt)
    break

  cnt = cnt + 1
  # 配列の各値に対して2で徐算する
  b = list(map(lambda x: int(x/2), b))
