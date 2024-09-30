import random

print("{0:=^20}".format("반복문"))
'''
for 변수 in 리스트(또는 튜플, 문자열):
  수행 문장1
  수행 문장2
  ...
'''

ls = ['one', 'two', 'three']
for i in ls:
  print(i)  # 원소를 직접 다룸

for i in range(len(ls)):
  print(ls[i], ', index:', ls.index(ls[i]))  # 리스트의 인덱스를 이용한 접근

a = [(97, 'a'), [98, 'b'], (99, 'c')]
for (k, v) in a:
  print("{} : {}".format(v, k), end="\n")

for i in range(97, 97 + 26):
  if (i != 97): print('', end=',');
  print(chr(i), end='');
print()
marks = [90, 25, 67, 45, 80]
print('marks에서 60점 이상인 점수만 출력하시오')
for mark in marks:
  # if mark > 60: print(mark)
  if mark < 60: continue
  print(mark)

a = "12ㄱ345"
result = 'Number'
for i in a:
  # try:int(a)
  # except:result = "Not a Number";break;
  if not i.isnumeric(): result = "Not a Number";break;
  # if (ord(i) < ord('0') or ord(i) > ord('9')):
  #   result = "Not a Number";break;
print(result)
if a.isnumeric():
  print(result)
else:
  print("Not a Number")

for i in range(2, 10, 3):
  for j in range(1, 10):
    for k in range(0, 3):
      if not ((i + k) == 10):
        print('%d * %d = %2d' % ((i + k)
                                 , j, (i + k) * j), end='\t')
    print()
  print()

a = list(range(1, 10))
i = 0
while i < len(a):
  print("짝수" if a[i] % 2 == 0 else "홀수");
  i += 1

from tkinter import simpledialog as sd

print("{0:=^30}".format('1~100 사이의 숫자를 맞추시오'), end="\n")
rand = int(random.random() * 100) + 1
print(rand)

cnt = 0
while True:
  input = sd.askinteger("Input", "Your Answer?", parent=None)
  cnt += 1
  if (input > rand):
    print('큽니다')
  elif (input < rand):
    print('작습니다')
  else:
    print(f"정답입니다. {cnt}번 만에 맞췄습니다.")
    break

import Bomb

b = Bomb.Bomb()
b.start()
input = sd.askinteger("폭탄을 막아라",
                      "파란선(0) 또는 빨간선(1)중에 고르시오?", parent=None)
b.choose(input)
