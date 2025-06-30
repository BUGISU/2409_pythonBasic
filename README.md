# 🐍 Python Basic Examples
> tkinter 및 Python 문법 학습을 위한 예제 모음

## 📁 프로젝트 구조

```
pythonBasic/
├── common/                  # 공통 유틸 및 도구 (tkinter 앱, 좌표 추적 등)
├── ex01Grammar/            # Python 기초 문법 예제
│   ├── p01_print.py        # 문자열 포매팅 및 출력 예제
│   ├── p11_tkinter_relative_layout.py  # tkinter 레이아웃 예제 (pack)
│   └── ...
└── ...
```

---

## 🔧 공통 유틸리티 (`common/`)

### 1. `MyPythonNote.py`

간단한 **텍스트 편집기**를 `tkinter`로 구현한 예제입니다.

* 파일 열기, 저장, 새로 만들기 기능 제공
* 스크롤 지원 (`scrolledtext`)
* 메뉴와 단축키 구성

```python
text_area = scrolledtext.ScrolledText(window)
text_area.grid(sticky=N + E + S + W)

menu_1.add_command(label="Open", command=open_file)
menu_1.add_command(label="Save", command=save_file)
```

### 2. `windowLocationInfo.py`

마우스 클릭 시 위치를 출력하고, 창 크기 변경 시 동적으로 창 타이틀을 갱신하는 **좌표 도구** 예제입니다.

```python
def on_click(self, event):
    click_position_str = f"클릭 위치: {event.x}, {event.y}"
    self.label.config(text=click_position_str)
```


## 📌 개발자 노트

* 모든 예제는 **GUI 입문자** 및 **Python 문법 초보자**를 대상으로 작성되었습니다.
* `tkinter` 구성요소를 중심으로, 실용적인 GUI 조작 예제를 포함하고 있습니다.
* 일부 예제는 파일 입출력, 문자열 처리 등 실전에서 자주 쓰이는 기법들을 포함합니다.

---

## 📘 Python 기초 문법 요약 정리

> `ex01Grammar/` 폴더의 예제를 기반으로 한 파이썬 핵심 문법 요약입니다.

### 🟢 변수와 자료형 (`p02_variable.py`)

* **동적 타이핑** 기반 언어이며, 타입 선언 없이 사용 가능
* 주요 자료형:

  * `int`, `float`, `complex`
  * `bool`: `True`, `False`
  * `str`, `list`, `tuple`, `set`, `dict`
* **Type Hinting**: `def func(x: int) -> str:`

### ➕ 연산자 (`p03_operator.py`)

* 산술: `+`, `-`, `*`, `/`, `//`, `%`, `**`
* 비교: `>`, `<`, `==`, `!=`, `>=`, `<=`
* 논리: `and`, `or`, `not`
* 비트: `&`, `|`, `^`, `~`, `<<`, `>>`
* 삼항 연산: `x if condition else y`
* 문자열 연산: `"hello" + "world"`, `"a" * 3`

### 🧭 조건문 (`p04_condition.py`)

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'F'
```

* 사용자 입력을 `tkinter.simpledialog`로 받아 조건 분기
* `in`, `not in` 등을 활용한 계절 구분

### 🔁 반복문 (`p05_loop.py`)

* `for`, `while`, `continue`, `break`
* 중첩 for문을 통한 구구단 출력
* `range()`, `enumerate()`, `zip()` 활용
* 숫자 판별: `str.isnumeric()`

### 📦 리스트 (`p06_list.py`)

* 인덱싱, 슬라이싱, `.append()`, `.insert()`, `.pop()`, `.remove()`
* 이중 리스트 탐색 및 출력
* `copy()`, `reverse()`, `sort()`, `extend()`

### 🔁 튜플 (`p07_tuple.py`)

* 불변(immutable) 시퀀스
* 소규모 고정 데이터 처리에 적합
* 리스트와 유사한 순회 방법
* 다차원 튜플로 표 구성 가능

### 🧮 집합 (`p08_set.py`)

* `set()`: 중복 제거, 순서 없음
* 합집합(`|`), 교집합(`&`), 차집합(`-`), 대칭차(`^`)
* `issubset`, `issuperset`, `isdisjoint` 등 집합 비교

### 🗃️ 딕셔너리 (`p09_dict.py`)

* `dict = {'key': value}`
* `.get()`, `.update()`, `.setdefault()`, `.items()`, `.keys()`, `.values()`
* 반복문 순회 및 안전한 삭제 (`.pop()`, `del`, `.clear()`)

### 📦 함수 (`p10_def.py`)

* 정의: `def 함수이름():`
* 반환: `return`
* 매개변수: 기본값, 가변 인자(`*args`)
* 여러 값 반환: `return a, b`
* 곱셈 구현 예: 더하기 기반 `multiply()` 함수

### 🖼️ tkinter 레이아웃 (`p11`, `p12`, `p13`)

* `pack()`, `grid()`, `place()` 레이아웃 비교
* 버튼 배치 및 UI 구성 실습

### 💣 클래스와 스레드 (`Bomb.py`)

* 클래스 정의: `class Bomb(threading.Thread)`
* `__init__`, `__str__`, `run()` 메서드 사용
* `threading`, `time.sleep()`, `sys.exit()` 활용

---

## 🧪 기초 문법 예제 (`ex01Grammar/`)

### `p01_print.py`

다양한 **문자열 포매팅 방식**과 특수문자, 인코딩 출력 등을 연습하는 예제입니다.

* `format`, f-string, `%` 포매팅 비교
* 특수문자 출력 (`\n`, `\t`, `\\`)
* 파일 출력 및 읽기 예제 포함

```python
print("{0:=^20}".format("청산에 살으리라"))
print(f"{' LGH ':=^30}")
with open("청산에 살으리라.txt", 'w') as f:
    print("나는 수풀 우거진 청산에 살으리라", file=f)
```

---

## 🎨 tkinter 레이아웃 실습

### `p11_tkinter_relative_layout.py`

* `pack()` 레이아웃 방식 실습
* 버튼 위젯 배치 및 `overrelief`, `anchor` 속성 테스트

```python
btnConfirm = Button(window, text="Confirm", overrelief="groove", anchor="n")
btnConfirm.pack(padx=10, pady=20, side="top")
```

---


## ✅ 실행 환경

* Python 3.10+
* Windows/Mac/Linux 환경
* 외부 라이브러리 불필요 (`tkinter` 기본 포함)
