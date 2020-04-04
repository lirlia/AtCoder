
# 経路情報(存在しないルートは0とする)
# 例：⓪ → ① は1なので以下の２箇所（① → ⓪も考えている）を1にしている
#
# [0, 1←ここ, 2, 3, 5, 0, 0, 0, 0],
# [1←ここ, 0, 3, 0, 0, 0, 0, 0, 0],

route_list = [
  [0, 1, 2, 3, 5, 0, 0, 0, 0],
  [1, 0, 3, 0, 0, 0, 0, 0, 0],
  [2, 3, 0, 2, 0, 3, 0, 0, 0],
  [3, 0, 2, 0, 0, 1, 0, 0, 0],
  [5, 0, 0, 0, 0, 4, 4, 0, 0],
  [0, 0, 3, 1, 4, 0, 0, 5, 7],
  [0, 0, 0, 0, 4, 0, 0, 7, 0],
  [0, 0, 0, 0, 0, 5, 7, 0, 2],
  [0, 0, 0, 0, 0, 7, 0, 2, 0]]

# ノード数
node_num = len(route_list)

# ノードのコストと計算有無を用意
nodes_status = \
  [{"no": i , "cost": float('inf'), "used": False, "prev": None } for i in range(node_num)]

#
# 【1：始点に0を書き込む】
#
nodes_status[0]["cost"] = 0

#
# nodes_statusの中から、
# まだ計算されていないノードのうち最小のものを返却する関数
#
def searchMinIndex(nodes_status):

  # まだ計算していないノードを出力し
  node = [node for node in nodes_status if node["used"] == False ]

  # 最小のコスト値のノードを出力する
  minNode = sorted(node, key=lambda x: x["cost"])[0]

  return minNode["no"]

#
# メイン処理
#
def main():

  while True:
    #
    # 【2：未確定の地点の中から最も小さい値を持つ地点を1つ選び、その値を確定させる】
    #
    minNodeNo = searchMinIndex(nodes_status)

    # 対象のノードのルートをチェックし
    # 各ノードの情報を更新する

    #
    # 【3：2で確定した地点から直接繋がっていて〜｝
    #
    for i, cost in enumerate(route_list[minNodeNo]):

      # 各ルートのコストが0より大きい場合
      if cost > 0:
        
        # すでに存在しているノードのコストと、今回の更新値を比較する
        if nodes_status[i]["cost"] > cost + nodes_status[minNodeNo]["cost"]:
          nodes_status[i]["cost"] = cost + nodes_status[minNodeNo]["cost"]
          
          # ノードのコスト値更新成功した際に、
          # 1つ前のノード情報をprevに登録しておく
          # 例: ②→③のルートが最速であるとわかったら、
          # 　　③のprevに②を登録しておく
          nodes_status[i]["prev"] = minNodeNo

    # ノード計算が完了したのでTrueに変更
    nodes_status[minNodeNo]["used"] = True
    
    #
    # 【4：全ての地点が確定していれば終了、そうでなければ2に戻る】
    # 
    if len([node for node in nodes_status if node["used"] == True ]) == node_num:
      break

  # 終了後の描画処理
  node = [node["cost"] for node in nodes_status]

  print("各ノードの値: {}".format(",".join(map(str, node))))
  print("距離　　　　: {}".format(node[-1]))

  # 移動経路の取得
  # 最終ゴールとゴールの手前のノード情報をセットしておく
  prevList = [nodes_status[-1]["prev"], nodes_status[-1]["no"]]

  # 他のルートについてチェック
  while True:
    if prevList[0] == 0: break
    prevList.insert(0, nodes_status[prevList[0]]["prev"])
    
  print("移動経路　　: " + " -> ".join(map(str, prevList)))

main()