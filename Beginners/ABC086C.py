# -*- coding: utf-8 -*-
N = int(input())
tList = list(map(lambda x:x.split(), [input() for i in range(N)]))

if N == 1:
  cnt = 1
else:
  cnt = N - 1

for i in range(cnt):

  if N == 1:
    if int(tList[0][0]) == 1:
      diffTime = 1
    else:
      diffTime = int(tList[0][0]) - 1

    diffX = int(tList[0][1])
    diffY = int(tList[0][2])
  else:
    diffTime = int(tList[i + 1][0]) - int(tList[i][0])
    diffX = abs(int(tList[i + 1][1])) - abs(int(tList[i][1]))
    diffY = abs(int(tList[i + 1][2])) - abs(int(tList[i][2]))

  diffAll = diffX + diffY

  # 移動時間と移動量が偶数偶数or奇数奇数の時のみ
  # 到達可能なためチェックする
  if (diffTime % 2) != (diffAll % 2):
    print("No")
    exit(0)

  # 移動時間よりも移動量の方が大きい場合は到達不可能
  if diffTime < diffAll:
    print("No")
    exit(0)

print("Yes")
