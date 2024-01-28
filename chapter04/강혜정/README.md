# Chapter 4. 리스트 다루기

## 1. 전체 리스트 순회하기
- 루프란 리스트의 모든 요소에 순서대로 접근하는 것을 말하며, 이 과정에서 모든 요소에 같은 동작을 수행할 수 있음.
- 리스트의 모든 요소에 같은 행동을 반복할 때는 for 루프 사용.
- for 루프 안에 쓸 수 있는 코드의 양에 제한이 없음.
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 출력:
# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# David, that was a great trick!
# I can't wait to see your next trick, David.

# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina
```


## 2. 들여쓰기 에러 피하기
- 파이썬은 들여쓰기를 사용해 프로그램의 각 부분을 구분함.
- 들여쓰기를 잘못했을 때 들여쓰기 에러가 발생함.
    - 들여쓰기를 잊었을 때
    - 일부 행을 들여 쓰지 않았을 때
    - 불필요한 들여쓰기를 했을 때
    - 루프 다음에 불필요한 들여쓰기를 했을 때
    - 콜론을 잊었을 때
```shell
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 3
    print(magician)
    ^
IndentationError: expected an indented block after 'for' statement on line 2

[Execution complete with exit code 1]
```


## 숫자 리스트 만들기

### range() 함수 사용하기
- range() 함수로 일련의 숫자를 쉽게 만들 수 있음.
```python
# range() 함수 사용
for value in range(5): # == range(0, 5)
    print(value)
for value in range(1, 5+1):
    print(value)

# 숫자 리스트
numbers = list(range(1, 6))

# 숫자 건너뛰기
numbers = list(range(2, 11, 2))

# 제곱 숫자 리스트
for value in range(1, 11):
    print(value ** 2)
```

### 숫자 리스트와 단순한 통계
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 최소 값
min(digits) # 1

# 최대 값
max(digits) # 9

# 합계
sum(digits) # 45
```

### 리스트 내포
- 리스트 내포는 단 한줄의 코드로 똑같은 리스트를 생성하는 파이썬 문법임.
- squeres 같은, 뜻이 분명한 리스트 이름으로 시작. 다음에는 대괄호를 열고, 새 리스트에 저장할 값의 표현식을 작성. 그 다음 표현식에 사용할 숫자를 생성하는 for 루프를 쓰고 대괄호를 닫음.
- 리스트 내포 문법에서는 for 문 마지막에 콜론을 쓰지 않음.
```python
squeres = [value**2 for value in range(1, 11)]
print(squeres)
```


## 리스트 일부분 다루기
- 리스트의 일부분만 다루는 문법을 슬라이스라고 부름.
```python
# 슬라이스 사용
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4]) # 0부터
print(players[2:]) # 인덱스 2부터
print(players[-3:]) # 마지막 세 명의 플레이어

# 슬라이스 순회
for player in players[:3]:
    print(player)

# 리스트 복사
new_players = players[:]
```


## 튜플
- 변하지 않는 불변의 값 튜플.
- 튜플을 정의할 때 대괄호 대신 괄호를 사용한다는 점을 제외하면 리스트와 동일함.
- 튜플의 요소를 개별적으로 변경하는 건 불가능
- 튜플을 변경하는 건 불가능하지만, 튜플을 가리키는 변수에 새 값을 할당하는 건 가능.
```python
size = (960, 640)

size[0] = 1960

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 2, in <module>
    size[0] = 1960
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment

[Execution complete with exit code 1]

size = (1960, 960)
```

## 스타일 가이드
- **PEP 8**은 가장 오래된 PEP로 코드 스타일에 관한 가이드임.
- 대부분의 파이썬 프로그래머는 각 행의 길이가 80자 미만이어야 한다고 권함.
    대부분의 컴퓨터가 터미널의 한 행에 79자만 표시할 수 있었던 과거에 확립