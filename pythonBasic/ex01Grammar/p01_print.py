# Python은 Script언어 : 소스코드를 한줄씩 읽어 바로 실행하는 Interpreter 방식
# 핵심 철학: 쉬워야 한다. 효율적이어야 한다. 읽기 쉬워야 한다.

a = 100
print(type(a))
b = 200
print("a, b :", a, b)
# tmp = a
# a = b
# b = tmp
a, b = b, a
print("a, b :", a, b)

print('=== 특수 문자 ===')
print("\\")
print("a\tb")
print("\"")
print('\'')
print("Hello \nWorld")
print("""  파이썬은 쉬운 언어입니다.
    배우기가 무척 쉽습니다.
    열심히 보다 재미있게 하세요! 
""")
'''
긴문자 주석 처리 할 경우 
사용 됩니다.
'''

print("'A'")
print('"A"')

print("%d %s %3.2f %c" % (10, "LGH", 10.12, 'A'), end='\n\n')
print(f"{' ' + 'LGH' + ' ':=^30}")
print("{0:=^20}".format("청산에 살으리라"))
print("{0:=<20}".format("청산에 살으리라"))
print("{0:=>20}".format("청산에 살으리라"))
print("나는 수풀 우거진 청산에 살으리라 \n\
       나의 마음 푸르러 청산에 살으리라 \
       이 봄도 산허리엔 초록빛 물들었네 \
       세상 번뇌 시름 잊고 청산에서 살리라".replace('       ', ''))
print()
print("{0:=^20}".format('부호 출력'))
print("{:+d}".format(52))  # + 는 양의 부호,
print("{:-d}".format(52))  # - 는 양의 부호, 음수일 경우
print("{:d}".format(-52))  # - 는 양의 부호, 음수일 경우
print("{:5d}".format(-52))  # 총 5자리에서 숫자 앞 부호 표시(  -52)
print("{:+5d}".format(52))  # 총 5자리에서 숫자 앞 부호 표시(  +52)
print("{:=5d}".format(-52))  # 총 5자리에서 부호와 숫자 표시(-  52)
print("{:=+5d}".format(52))  # 총 5자리에서 부호와 숫자 표시(+  52)
print("{:+05d}".format(52))  # 총 5자리에서 부호와 숫자 표시(+0052)
print("{:=#5d}".format(-52))  # 총 5자리에서 부호와 숫자 표시(   52)
print("{:+15f}".format(1234.5678))  # 소수,부호포함 15자리
print("{:-15f}".format(1234.5678))  # 소수,부호포함 15자리
print("{:-015f}".format(1234.5678))  # 소수,부호포함 15자리
print("({0:10.2f})".format(1234.5678))  # 총 10자리, 소수 2째 자리.(   1234.57) 소수자리 반올림

print("({0:<10})".format('Hello'))  # 총 10자리, (<,>,^ 는 방향)
print("({0:>10})".format('Hello'))  # 총 10자리
print("({0:^10})".format('Hello'))  # 총 10자리
print("{0:=^11}".format('Hello'))  # 총 10자리
print("({0:0>10})".format('Hello'))  # 총 10자리, 빈자리는 0으로 채움
print("{{ }}는 클래스이다.".format())

print(f'{"기타 문자열 함수":=^20}')
print("Hello World".count("l"))
print("Hello World".find("l"))  # 없으면 -1반환
print("Hello World".rfind("l"))
print("Hello World".index("l"))  # 없으면 error 반환
print(",".join('12345'))
print("hello".upper())
print("hello".lower())
print("hello".capitalize())

str = '1,2,3,4,5'.split(',')
print(type(str))
for item in str:
  print(item, end="\n")

with open("청산에 살으리라.txt", 'w') as f:
  print("""나는 수풀 우거진 청산에 살으리라 
나의 마음 푸르러 청산에 살으리라
이 봄도 산허리엔 초록빛 물들었네
세상 번뇌 시름 잊고 청산에서 살리라""")

f = open('청산에 살으리라.txt', 'r')
lines = f.readlines()
for line in lines:
  print(line)
