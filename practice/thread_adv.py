import threading
import time
now = None

def getTime():

  # 1000ミリ秒待つ
  time.sleep(1)

  # 現在時刻を取得
  global now 
  now = time.time()

def printTime():

  global now
  print(now)

if __name__ == '__main__':

  threading.Thread(target=getTime).start()

  while True:
    
    if now != None:
      threading.Thread(target=printTime).start()
      break

    else:
      time.sleep(1)


