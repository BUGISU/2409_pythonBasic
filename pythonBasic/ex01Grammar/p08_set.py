# Set (중복과 순서가 없는 자료형)
# 순서가 없기 때문에 인덱싱이 지원 안됨
# 중괄호를 사용

s = set()
print(s, type(s))

s = set([1,2,3,4,5])
print(s, type(s))

s = set("HELLO")
print(s, type(s))

s = set(range(5))
print(s)

s = set('기러기')
print(s)

s = {} # 주의 빈 중괄호는 dict가 됨!
print("s = {}", type(s))

# set은 list, dict와 달리 set안에 set을 넣을 수 없다.
# s = {
#   {1,2,3},
#   {3,4,5}
# }
# print(s)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

print(f'합집합: s1 ∪ s2')
print(s1.union(s2))
print(set.union(s1, s2))
print(s1 | s2)

print(f'교집합: s1 ∩ s2')
print(s1.intersection(s2))
print(set.intersection(s1,s2))
print(s1 & s2)

print(f'차집합: s1 - s2')
print(s1.difference(s2))
print(set.difference(s1, s2))
print(s1 - s2)

print(f'대칭차집합(XOR): s1 ^ s2')
print(s1.symmetric_difference(s2))
print(set.symmetric_difference(s1, s2))
print(s1 ^ s2)

print('할당연산자:기존의 집합에 연산을 진행함으로 주소 동일')
a = {1,2,3,4}; print(id(a))
a |= {3,4,5,6}
print('| ', a)

a = {1,2,3,4};
a &= {3,4,5,6}
print('& ', a)

a = {1,2,3,4};
a -= {3,4,5,6}
print('- ', a)

a = {1,2,3,4};
a ^= {3,4,5,6}
print('^ ', a)

print('set의 관계 연산')
a = {1,2,3,4}
print('부분집합 <= ', a <= {1,2,3,4})
print('부분집합 issubset', a.issubset({1,2,3,4}))
print('진부분집합 < ', a < {1,2,3,4,5})
print('상위집합 >= ', a >= {1,2,3,4})
print('상위집합 issuperset', a.issuperset({1,2,3,4}))
print('진상위집합 >= ', a >= {1,2,3})

print(a == {1,2,3,4}); print(a == {3,2,1,4})
print('겹침여부 isdisjoint: ', a.isdisjoint({5,6,7,8}))
print('겹침여부 isdisjoint: ', a.isdisjoint({3,4,5,6}))

a.add(5); print(a)
a.remove(5); print(a) # element가 없으면 에러
a.discard(9); print(a)# element가 없으도 OK
a.pop(); print(a) # 임의의 element를 삭제
print(len(a))

a = {1,2,3,4}; print(a, id(a))
b = a; # 주소를 복사 a와 b가 동일
print(b, id(b))
print(a is b)
b.add(5)
print(a, b)

a = {1,2,3,4}; print(a, id(a))
b = a.copy() # a와 b는 다른 set
b.add(5)
print(a, b)

for i in a: print(i, end=" ")
print()
for i in {1,2,3,4}: print(i, end=" ")
print()
a = {i for i in 'pineapple' if i not in 'apl'}
a = set(i for i in 'pineapple' if i not in 'apl')
print(a)

#집합의 내용 수정 안됨, 2 차원 이상 생성 가능
a = frozenset(range(5))
a = frozenset({0,1,2,3,4})
print(a)
a = frozenset({
  frozenset({1,2}), frozenset(range(3,5))
})
print(a)



print()
print()
print()
print()
print()
print()