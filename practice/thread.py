import threading
counter = 0

# 
# スレッドによって呼び出される処理
# counterを加算していくだけ
#
def work():

  # スレッド間で共有する変数をglobalから持ってくる
  # 参考 : https://www.it-swarm.dev/ja/python/%E3%82%B9%E3%83%AC%E3%83%83%E3%83%89%E3%81%A7%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E5%A4%89%E6%95%B0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B/1043441666/
  global counter

  for i in range(5):
    counter = counter + 1
    print("{} : {}".format(threading.current_thread(),counter))

if __name__ == '__main__':

    # rangeで指定した数だけスレッドを生成する
    for i in range(2):
      threading.Thread(target=work).start()


