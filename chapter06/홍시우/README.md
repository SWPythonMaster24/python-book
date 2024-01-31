---
title: Chapter_06 딕셔너리
author: rain_poem
date: 2024-01-28 22:32:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## 딕셔너리
```python
#alien.py
#            key      value     key     value
alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])         # green
print(alien_0['points'])        # 5
```

파이썬 **딕셔너리**는 **키-값 쌍** 컬렉션입니다.<br>
각 **키**는 값에 연결되어 있고, 키를 통해 값에 접근할 수 있습니다.<br>
딕셔너리는 **중괄호 ({})** 로표현하고, 그안에 키와 값을 **콜론 (:)** 으로 구분합니다.<br>
키-값 쌍은 **콤마 (,)** 로 구분합니다.<br>
딕셔너리 값에 접근할때는 **대괄호 ([])** 안에 키 이름을 씁니다.<br>

## 딕셔너리 사용하기
```python
# 딕셔너리 키-값 쌍 추가하기
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0) # {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y position'] = 25

print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y position': 25}
```
딕셔너리에 새로운 **키-값 쌍**을 추가할 수 있습니다.

```python
# 딕셔너리 값 수정하기
alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")  # The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  # The alien is now yellow.
```
딕셔너리에 값을 수정할 수 있습니다.<br>

```python
# 키-값 쌍 제거하기
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0) # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # {'color': 'green'}
```
```del 문```을 통해서 딕셔너리의 키-값 쌍을 제거할 수 있습니다.<br>

```python
# 비슷한 객체의 딕셔너리
favorite_languages = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'rust',
    'phil'  : 'python',

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.") # Sarah's favorite language is C.
}
```
딕셔너리를 여러 행에 나눠쓰려면 **중괄호** 이후에 다음 행부터 작성합니다.<br>
첫번째 키-값 정의 이후 콤마를 통해 **키-값 쌍**을 추가합니다.<br>

```python
# get() 메서드
alien_0 = {'color' : 'green', 'speed' : 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) # No point value assigned.
```
```get() 메서드```를 통해 보다 안전하게 딕셔너리에 접근할 수 있습니다.<br>
get 메서드의 첫번째 인자는 딕셔너리의 키, 두번째 인자는 키가 없을때 반환하는 기본값<br>

## 딕셔너리 순회하기
딕셔너리 하나에 수백만 개 이상의 키-값 쌍을 저장할 수 있기때문에, 순회하는 방법을 배웁니다.

```python
# 키-값 쌍 순회하기
user_0 = {
    'username'  : 'efermi',
    'first'     : 'enrico',
    'last'      : 'fermi',
}

for key, value in user_0.items() :
    print(f"\nKey : {key}")
    print(f"Value : {value}")
```
```items() 메서드```는 키-값 쌍을 반환합니다.<br>
따라서, for문에서 items 메서드가 반환하는 값을 변수 **key**와 **value**에 각각 할당하여 사용합니다.<br>

```python
# 키 순회하기
favorite_languages = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'rust',
    'phil'  : 'python'
}

for name in favorite_languages.keys():
    print(name.title())

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```
```keys() 메서드```는 딕셔너리 키를 반환합니다.<br>
이 메서드는 생략해도 상관없습니다.<br>
```sorted() 함수```를 통해 정렬된 키의 사본을 가져올 수 있습니다.<br>

```python
# 값 순회하기
favorite_languages = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'rust',
    'phil'  : 'python'
}

for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
```
```values() 메서드```는 딕셔너리의 값을 반환합니다.<br>
```set()```를 통해 중복을 제거할 수 있습니다.<br>

## 중첩
리스트 안에 딕셔너리를 저장<br>
딕셔너리의 값으로 리스트를 저장<br>
딕셔너리 안에 딕셔너리를 저장<br>
하는 형태를 **중첩**이라 부른다.<br>

```python
# 리스트 안에 딕셔너리 저장
alien_0 = {'color' : 'green',   'points' : 5}
alien_1 = {'color' : 'yellow',  'points' : 10}
alien_2 = {'color' : 'red',     'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# {'color' : 'green',   'points' : 5}
# {'color' : 'yellow',  'points' : 10}
# {'color' : 'red',     'points' : 15}
```
위 형태는 3개의 딕셔너리를 만들어 **aliens**라는 리스트에 저장한 형태이다.

```python
# 딕셔너리의 값으로 리스트를 저장

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
```
딕셔너리의 값으로 **toppings** 키에 **['mushrooms', 'extra cheese']** 값을 저장한 형태이다.

```python
# 딕셔너리 안에 딕셔너리 저장
users = {
    'aeinstein' : {
        'first'     : 'albert',
        'last'      : 'einstein',
        'location'  : 'princeton',
    },

    'mucurie': {
        'first'     : 'marie',
        'last'      : 'curie',
        'location'  : 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```
각 키의 값으로 딕셔너리를 정의한 형태이다.<br>
개인적으로는 코드의 복잡도가 올라갈 가능성이 매우 높지만, 그만큼 활용가능한 범위도 넓어보임<br>
