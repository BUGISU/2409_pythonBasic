import random

from ex01Grammar import Bomb

print("1. list (다양한 자료형을 순차적으로 저장하는 집합적 자료형")
l = list()
print(id(l))  # id(): hash code의 값을 불러옴
l = [1, 2, 3]  # list 새로 초기화
print(id(l))
print(l, type(l))

l = []
print(id(l))
for i in range(0, 10):
  # l[i] = i
  # l.insert(i, i + 1) #(index, value)로 추가
  l.append(i + 1) #리스트의 끝부분부터 추가
print(l)
print(id(l))
print(l[0:3])
print(l[5:13])
print(len(l))

l[0] = True
l[1] = 10
l[2] = "A"
l[3] = Bomb.Bomb()
print(l)
print(l[3])
print(len(l))
# 인덱스 순서대로 출력
for i in range(len(l)):
  print(l[i], end='#')
print()
# 인덱스 역순으로 출력
for i in range(len(l)-1, -1, -1):
  print(l[i], end='#')
print()
l.reverse() # 리스트자체를 역정렬함.
print(l)
print(f'l.count(10): {l.count(10)}') #포함된 갯수
print(l.pop()) # 리스트의 맨끝에 자료 삭제와 출력
print(l.pop(0)) # 리스트의 맨앞에 자료 삭제와 출력
print(l)
print(l.pop(5)) # 리스트의 인덱스로 자료 삭제와 출력
print(l)
l.remove('A') # 리스트의 값을 찾아서 삭제, 리턴 없음
# print(l.remove(2)) # 리스트의 값을 못 찾으면 에러
del l[len(l)-1] # 인덱스로 삭제
# del l[10] # 인덱스로 못 찾으면 에러
print(l)
l_copy = l.copy()
print(l_copy)

list_2d = [
  ['강길동',100, 90, 100],
  ['김길동',70, 90, 100],
  ['고길동',100, 70, 90],
]
print(list_2d, type(list_2d))
for row in list_2d:
  for col in row:
    print('%3s' %(col), end=' ')
  print()

for r in range(len(list_2d)):
  for c in range(len(list_2d[r])):
    print('%-3s' %(list_2d[r][c]), end=' ')
  print()

a = [1,2,3]
b = list(range(4,7))
c = a+b
print(c, type(c))
d = [7,8,9]
d.extend(c)
d.insert(0,0)
print(d)
d.sort()
print(d)
# shuffle
for i in range(len(d)):
  rand = int(random.random()*10)
  d[i], d[rand] = d[rand], d[i]
print(d)

d.clear()
print(d)


print()
print()
print()
print()
print()
print()
print()