# 변수에 대하여 동적 할당
# 변수의 명명규칙
# 1) 예약어 안됨
# 2) _, 영문자(대소문자 구별), 숫자(시작 안됨)
# 3) 특수문자, 공백 안됨
# 4) 클래스는 Pascal case, 변수나 함수는 Snake case
# 5) Python에서는 null 대신 None 사용
'''
[ 자료형 ]
논리 자료형 : True, False
숫자 자료형 : int, float, complex
시퀀스 자료형 : str, list, tuple
집합 자료형 : set
딕셔너리 자료형 : dict

군집 자료형 : str, list, tuple, dict, set
동적 자료형 : 입력시 타입이 결정
'''
from logging import exception

print("{0:=^20}".format('Boolean Type'))
a = True
print(type(a), type(False))

print("{0:=^20}".format('Numeric Type'))
b = 10
print(type(b))
print(type(1.0))
c = 10 + 5j + 3J  # 복소수에 사용되는 문자 j, J
print(type(c))  # 복소수
print(c.real)  # 실수
print(c.imag)  # 허수(Imaginary Number)
print(c) # (10+8j)

print("{0:=^20}".format('Sequence Type'))
print(type('Hello Python'))  # str
print(type([1, 2, 3, 4, 5]))  # list
print(type((1, 2, 3)))  # tuple

print("{0:=^20}".format('Set Type'))
집합 = set([1, 2, 3])
print(type(집합))
s1 = set('hello')
print(s1)

print("{0:=^20}".format('Dictionary Type'))
dic1 = {'name': 'LGH', 'phone': '010-1111-7474'}
print(type(dic1))

print("{0:=^20}".format('type annotation'))
# type annotation이라고 하고 hinting 한다. 강제되지 않음.
n1: int = 10
print(n1, type(n1))
n1 = True
print(n1, type(n1))


def repeat(message: str, times: int = 2) -> list[str]:
  return [message] * times


def greet(name: str) -> None:
  print("Hi! " + name)


print("{0:=^20}".format('변수의 종류'))
print("{0:=^20}".format('1. NoneType'))
print(type(None))  # null 대신에 None사용

print("{0:=^20}".format('2. Numeric: int, float, complex'))
a = 10;
print(a, end=" ");
print(type(a))
a = 12.345;
print(a, end="\t");
print(type(a))
# BIN (Binary) : 2진수
a = 0b1010;
print(a, end="\t");
print(type(a))
# OCT (Octal) : 8진수
a = 0o12;
print(a, end="\t");
print(type(a))
# HEX (Hexadecimal) : 16진수
a = 0x2a;
print(a, end="\t");
print(type(a))

a = 123e2;
print(a, end="\t");
print(type(a))
a = 123E-2;
print(a, end="\t");
print(type(a))

# DEC (Decimal) : 10진수
print(format(10, 'b'))
print(format(10, 'o'))
print(format(10, 'x'))
print(format(10, 'd'))
print(format(10, '#b'))
print(format(10, '#o'))
print(format(10, '#x'))
print(format(10, '#X'))
print(format(10, '#d'))

a = 1234.5678;
print(int(a))  # 형변환
a = 10;
print(float(a))  # 형변환

a = "123"  # str
a = "123a"  # str
a = int("123")  # int
# a= int("123a") # exception!!

try:
  a = int("123a");
except:
  print("문자열이 포함되었습니다.")

# python에는 상수가 없다.  python은 동적언어이기 때문에 상수가 불필요
from typing import Final
SIZE:Final = 5
SIZE = 10
print(SIZE)

import common.constant as const
const.PI = 3.14
print(const.PI)

# 에러 발생. 재할당이 안됨.
const.PI = 3.141592
print(const.PI)


a = 10
print(a)
del a       # 변수 지우기
print(a)



