# def : define
# 재사용, 여러 명령들의 묶음, 가독성 향상, 유지 보수 향상
# python에는 overloading 기능이 없다.

# 1) (매개변수 X, 리턴 타입 X)
def lines():
  s = "===" * 10
  print(s)


lines()


# 2) (매개변수 O, 리턴 타입 X)
def lines(str):
  s = "{0:=^20}".format(str)
  print(s)


# lines() # 에러 발생 : overloading 아예 없다.
lines("def")


# 3) (매개변수 X, 리턴 타입 O)
def lines():
  print("{0:=^20}".format('test'))
  return "===" * 10


print(lines())


# 4) (매개변수 O, 리턴 타입 O)
def lines(str):
  return f"{' ' + str + ' ':-^30}"


print(lines('LGH'))


# 매개 변수 a, b 사이의 모든 수의 합을 리턴하는 add 함수를 작성하시오.
def add(a, b):
  tot = 0
  for i in range(a, b + 1):
    tot += i;
  return tot


print(add(1, 10))


def share_remain(a, b):
  share = a // b
  remain = a % b
  return share, remain


print(share_remain(10, 3))

share, remain = share_remain(10, 3)
print(share, remain)


# 곱하기 연산자를 사용하지 않고 더하기 만으로 곱셈의 결과를 도출하시오
def plus(a, b):
  return a + b


def multiply(a, b):
  result = 0
  for i in range(b): result = plus(result, a)
  return result;


print(multiply(5, 3))

tot = 0


def add_str(*arg):
  txt = ''
  for item in arg:
    txt += str(item) # 문자 더하기는 반드시 문자끼리만 가능
  return txt;

# 복수개의 매개 변수를 받을 때 *를 사용
def add_num(*arg):
  global tot # 지역변수이지만 전역변수를 끌어올 때.
  for item in arg:
    tot += int(item)
  return tot;

print(add_num(1,2,3,4,5))
print(add_str(1,2,3))
print(add_str('a','b','c',))