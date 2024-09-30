# a = input("숫자를 입력하세요: ")
# print(a)

from tkinter import simpledialog

score = simpledialog.askinteger("Input", "Your Answer", parent=None)
result = ''

if(score == None):
  print("입력된 숫자가 없습니다.")
  exit(-1)

if score >= 90:
  result = 'A'
elif score >= 80:
  result = 'B'
elif score >= 70:
  result = 'C'
else:
  result = 'F'
print(f'당신의 학점은 {result}')

season = simpledialog.askinteger("Input",
                                 "What is Your favorite month?", parent=None)
result = ''
if season in (12, 1, 2):
  result = "Winter"
elif season in (3,4,5):
  result = "Spring"
elif season in (6,7,8):
  result = "Spring"
elif season in (9,10,11):
  result = "Spring"
else:
  result = "해당하는 월이 없습니다."
print(f'당신이 좋아하는 {season}월의 계절은 {result}')