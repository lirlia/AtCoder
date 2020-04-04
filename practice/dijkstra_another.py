#route_list = [
#  [0, 50, 80, 0, 0], 
#  [0, 0, 20, 15, 0 ], 
#  [0, 0, 0, 10, 15], 
#  [0, 0, 0, 0, 30], 
#  [0, 0, 0, 0, 0]
#  ] # 初期のノード間の距離のリスト

route_list = [
  [0, 2, 5, 0, 0, 0, 0],
  [0, 0, 4, 6, 10, 0, 0],
  [0, 4, 0, 2, 0, 0, 0],
  [0, 6, 2, 0, 0, 1, 0],
  [0, 10, 0, 0, 0, 3, 5],
  [0, 0, 0, 1, 3, 0, 9],
  [0, 0, 0, 0, 0, 0, 0]]

route_list = [
    [0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]] # 初期のノード間の距離のリスト

node_num = len(route_list)
node_cost = [float('inf')] * node_num
node_cost[0] = 0
node_used = [False] * node_num

# 探索が完了（node_usedがすべてTrueになる）までループする
while (False in node_used):

  # 一時的にtmpに無限（infinity）を代入
  tmp = float('inf')

  # 各ノードがすでに計算済みかを確認し
  # 計算済みの場合はノードの値を取得しておく
  for k, node_used_bool in enumerate(node_used):
    # もしノードが計算済み（True）の場合は
    # ノードの値とtmpを比較し、ノードの値の方が小さい場合はtmpに代入する
    if (not node_used_bool):
      if tmp > node_cost[k]:
        tmp = node_cost[k]

  # 
  i = node_cost.index(tmp)

  # route_listにて定義されている各ノードから伸びる道が存在していれば(>0のところ)
  # その道を利用した時のコストとすでに設定されているコスト（node_cost[j]）の小さい方を選択する
  for j in range(node_num):
    if route_list[i][j] > 0:
      node_cost[j] = min(node_cost[j], route_list[i][j] + node_cost[i])

  print("各ノードの値: {}".format(node_cost))
  node_used[i] = True

print("各ノードの値: {}".format(node_cost))
print("距離: {}".format(node_cost[len(node_cost) - 1]))