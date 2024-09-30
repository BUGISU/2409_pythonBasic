print("{0:=^20}".format(' 1. 사칙 연산자 '))
print("Quiz) 10을 3으로 나누었을 때 몫과 나머지를 구하시오")
print(int(10 / 3), 10 % 3)
print("몫: %d, 나머지: %d " % (10 // 3, 10 % 3))
print("몫: {}, 나머지: {} ".format(10 // 3, 10 % 3))
print("10의 3승: {}".format(10 ** 3))

print("{0:=^20}".format(' 2. 비트 연산자 '))
print(0b1010 & 0b1100)
print(bin(0b1010 & 0b1100))
print(bin(0b1010 | 0b1100))
print(bin(0b1010 ^ 0b1100))
print(bin(~0b1010))  # 2의 보수로 출력
print("%s<<2 = %s" % (bin(2), bin(2 << 2)))

print("{0:=^20}".format(' 3. 대입 연산자 '))
tot = 0
for i in range(1, 11):  # 끝 자리는 미포함, 증감 기본값 1
  tot += i
print("합은 %d" % tot)
tot = 10
for i in range(1, 11):  # 끝 자리는 미포함, 증감 기본값 1
  # tot += i
  print("%d // %d = %d" % (tot, i, tot // i))
  print("%d %% %d = %d" % (tot, i, tot % i))

print("{0:=^20}".format(' 4. 비교 연산자 (>,<,<=,>=,==,!=) '))
print("{0:=^20}".format(' 5. 논리 연산자 (and, or, not) '))
print(not (1 > 2) and (4 > 3))

print("{0:=^20}".format('6. 삼항 연산자가 없다. 대신에'))
a = 1
a = 10 if a > 5 else 5
print(a)

print("{0:=^20}".format('7. 문자열 연산자 +, *'))
a = "hello"; b = "world"; c = 10
print(a + b + str(c)) # 문자열은 같은 문자열일 경우 연산가능
print("{} {} {}".format(a, b, c))
print("%s %s %d" % (a, b, c))
print(f'{a} {b} {c}')

print("=" * 10)

a='A'
print("ascii(%s), str(%s) of \n Ascii Code is %d"
      % (ascii(a), str(a), ord('A')))
a = 65
print("ascii(%s), str(%s), chr(%s) \n of Ascii Code is %d"
      % (ascii(a), str(a), chr(a), ord('A')))

print("Hello Python"[0])
print("Hello Python"[-2])
print("Hello Python"[0:12:2])

