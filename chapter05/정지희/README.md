---
marp: true
theme: uncover
---
# **챕터 5 IF문**
---
## **IF문**
##### IF문의 핵심은 TRUE/FLASE로 평가되는 표현식입니다. <br>조건 테스트(conditional test)라고도 부릅니다.
---
## **IF활용**
```python
answer = 17
# 동등 연산자
if answer == 17:
    print("That is the correct answer.")
# 불일치 연산자
if answer != 42: 
    print("That is not the correct answer. Please try again!")
# 여러조건 확인하기
if answer < 42 and answer >= 17: 
    print("That is the correct answer.")
# 하나만 만족해도되는 조건
if answer == 42 or answer == 17: 
    print("That is the correct answer.")
# 값이 리스트에 있는지 확인
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
```
---
## **if-elif-else**
##### 경우의 수가 셋 이상일 때 if-elif-else를 사용합니다. <br>각 조건 테스트를 순서대로 실행 중 통과하는 테스트가 <br>있을 시 나머지 테스트는 건너뜁니다.
```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
```
---
## **if문 스타일**
>비교 연산자 주위에 공백 한 칸을 사용하면 좋습니다.