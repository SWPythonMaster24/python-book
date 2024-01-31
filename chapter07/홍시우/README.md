---
title: Chapter_06 사용자 입력과 while 루프
author: rain_poem
date: 2024-01-29 22:32:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## input() 함수의 동작 방식
```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

```input()``` 함수의 인수는, 사용자가 어떤 정보를 입력해야 할지 알리는 **프롬프트**<br>
사용자의 입력은 **message** 변수에 할당<br>
변수를 함수의 인수로 쓰기 가능<br>
해당 함수를 통해, 입력받은 값은 **문자열**!<br>

## int() 함수를 사용해, 정수 입력 받기
```python
age = input("How old are you?") # "18"
age = int(age)                  # 18

if age >= 18 :
    print("True")   # True가 출력된다!
```
## while 루프 소개
```python
current_number = 0
while current_number < 10:
    current_number += 1
   
    if current_number % 2 == 0:
        continue
    elif current_number == 9:
        break

    print(current_number)
```
```while``` 를 통해 조건을 통과할때 까지 계속 반복합니다.<br>
```continue```를 통해 루프의 처음으로 돌아갑니다.<br>
```break``` 를 통해 루프를 즉시 종료합니다.<br>

## 리스트, 딕셔너리와 함께 while 루프 사용하기
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets) # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets) # ['dog', 'dog', 'goldfish', 'rabbit']
```
**pets** 리스트에 **'cat'** 값이 없을때 까지 반복하는 ```while``` 루프입니다.<br>

```python
responses = {}

# 설문조사를 제어할 플래그
polling_active = True

while polling_active:
    # 참가자 이름과 응답을 받습니다.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장합니다.
    responses[name] = response

    # 설문조사에 참가할 사람이 더 있는지 확인합니다.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 설문조사가 끝났으므로 결과를 출력합니다.
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```
빈 딕셔너리에 사용자가 입력한 값으로 종료할 수 있는 ```while``` 루프입니다.