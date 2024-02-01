---
marp: true
theme: uncover
---
# **챕터7 입력과 while루프**
---
## **input()함수**
```python
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```
##### input()함수는 프로그램을 일시 중지하고<br>사용자가 입력할 때까지 기다립니다. 해당 함수의 인수는 <br>사용자가 어떤 정보를 입력해야 할지 알리는 프롬프트입니다.
---
## **int()를 사용해 숫자 입력 받기**
##### input()함수는 사용자가 입력한<br>내용을 전부 문자열로 간주합니다.<br>int()를 통해 문자를 숫자로 변환할 수 있습니다.
```python
height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```
---
## **while 루프**
##### while문은 조건문이 참인 동안 <br>while문에 속한 문장들이 반복 수행됩니다.
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```
---
## **플래그 사용**
##### 하나가 아닌 여러 가지 조건을 통과해야만 프로그램<br>실행 여부가 결정될 경우, 이런 실행 여부를 결정하는 변수를<br> 정의 할 수 있는데 이를 플래그(flag)라고 합니다.
```python
message = input("Tell me something, and I will repeat it back to you:")
prompt = "\nTell me something, and I will repeat it back to you:"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```
---
## **break, continue**
##### break문은 while 루프를 즉시 종료합니다.<br>continue문은 조건 테스트 결과에 따라 루프의 처음으로 돌아갑니다.
```python
num = 0
while num < 10:
    num += 1
    if num == 9:
        break;
    elif num % 2 == 0:
        continue;
print(num)
# 1, 3, 5, 7
```