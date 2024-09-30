# tuple (다양한 자료형을 순차적으로 저장하는 집합 자료형)
# list 와 다르게 원소 변경이 불가!
# 상수 적인 특징을 가지고 있기 때문에 list보다 연산에 빠르다.

t = tuple()
print(id(t))
t = (1,2,3,4,5)
print(id(t))
t = tuple(range(0,5))
print(t, id(t))

for i in t:
  print(i, end=" ")
print()
print(t[0:2])

print(t.index(len(t)-1))
u = t + t
print(u)

groups = (
  ('강길동', 100, 90, 100),
  ('김길동', 70, 90, 100),
  ('고길동', 100, 70, 90),
)
print(groups, type(groups))
for row in groups:
  for col in row:
    print('%3s' %(col), end=' ')
  print()
for r in range(len(groups)):
  for c in range(len(groups[r])):
    print('%-3s' %(groups[r][c]), end=' ')
  print()


  