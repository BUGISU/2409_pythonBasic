import random
import sys
import threading
import time


class Bomb(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    # 변수명 앞에 __ 를 붙이게 되면 private하게 사용 가능
    self.__life = random.randint(1, 2)
    self.__state = False

  def run(self):
    for i in range(10, 0, -1):
      if self.__state: break;
      print(i)
      time.sleep(0.5)
    if not self.__state: print("꼬ㅏㅇ~!!")
    sys.exit()

  def choose(self, line):
    try:
      line = int(line)
    except:
      line = 1
    print(f'{line}을 선택하셨습니다.')
    if (self.__life == line):
      print('휴~ 살았다!')
    else:
      print('Bomb~!')
    self.__state = True

  def __str__(self):
    return "폭탄"
