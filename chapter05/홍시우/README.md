---
title: Chapter_05 if문
author: rain_poem
date: 2024-01-26 22:32:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## 조건 테스트
```python
#cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())  # 현재 car의 값이 bmw인지 체크
    else
        print(car.title())
```

**if**문의 핵심은 **True** 또는 **False**로 평가되는 표현식 (= **조건 테스트**)<br>
**True**면 **if**문 다음 코드를, **False**면 **else** 다음 코드를 실행<br>

## if문에 쓰이는 연산자
```python
>>> car = 'bmw'
>>> car == 'bmw'            # True

# lower 메서드를 통해 문자열간 조건 비교 시 대소문자를 무시할 수 있다.
>>> car = 'Audi'
>>> car == 'audi'           # False
>>> car.lower() == 'audi'   # True

>>> car = 'subaru'
>>> car != 'bmw'            # True

>>> age = 19
>>> age < 21                # True
>>> age <= 21               # True
>>> age > 21                # False
>>> age >= 21               # False
```

- ```==``` 동등연산자       : 연산자 왼쪽과 오른쪽 값이 동일하면 **True**
- ```!=``` 불일치 연산자    : 연산자 왼쪽과 오른쪽 값이 일치하지 않으면 **True**
- 그 밖에도 이상, 이하, 미만, 초과 같은 조건도 테스트 가능

## 여러 조건 확인하기
```python
#multiple_conditional.py
age_0 = 22
age_1 = 18

# and conditional return false
if age_0 >= 21 and age_1 >= 21
    print("and conditional return true")   
else
    print("and conditional return false")

# or conditional return true
if age_0 >= 21 or age_1 >= 21
    print("or conditional return true")
else
    print("or conditional return false")
```

```and 키워드```를 통해 두 조건이 모두 True인지 확인<br>
```or 키워드``` 를 통해 두 조건 중 하나라도 True인지 확인<br>

## 불리안 표현식 
```python
edit_permmision = True
```
boolean 값은 조건 표현식의 결과와 마찬가지로 **True** 또는 **False**<br>
if를 통한 조건값을 저장할 때 자주 사용 

## if문
```python
# 단순한 if문
age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else 문
age = 17

if(age >= 18)
    print("You are old enough to vote!")            
    print("Have you registered to vote yet?")
else                                     
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else 문
age = 12

if age < 4:
    print("Your admission cost is $0.")     
elif age < 18:
    print("Your admission cost is $25.")    
elif age < 65:
    print("Your admission cost is $40.") 
else      # else는 생략할 수 있다.
    print("Your admission cost is $20.")    
```
```if문```은 조건 테스트가  **True**로 평가되면 코드를 수행합니다.<br>
```if-else 문```은  **if문**과 비슷하며, **else** 블록을 통해 **False**일 경우에 코드를 수행할 수 있습니다.<br>
```if-elif-else문```은 경우의 수가 셋 이상일때 사용할 수 있으며, 마지막 **else** 블록은 생략 가능합니다.

## 리스트와 if문
```python
#toppings.py
requested_toppings = ['mushrooms', 'onions', 'pineapple', 'green peppers']

# mushrooms exist..
if 'mushrooms' in requested_toppings:
    print("mushrooms exist..")

# pepperoni not exist..
if 'pepperoni' not in requested_toppings:
    print("pepperoni not exist..")

# 리스트에 특정 값을 찾기
for requested_topping in requested_toppings:
    if rerequested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

# 리스트가 비어 있지 않는지 확인
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 여러 리스트 다루기
available_toppings =    ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

```in 키워드```를 통해서, 리스트 안에 값이 있는지 확인<br>
```not in 키워드```를 통해서, 리스트 안에 값이 없는지 확인<br>
```if 문```을 통해서, 리스트에 값이 들어 있는지 확인<br>
