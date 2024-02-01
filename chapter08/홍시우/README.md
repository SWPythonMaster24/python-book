---
title: Chapter_08 클래스
author: rain_poem
date: 2024-02-01 20:00:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## 함수 정의하기
```python
def greet_user():
    print("Hello!")

greet_user()
```

```def```키워드를 통해 함수를 정의할 수 있다.<br>
이를 **함수 정약**이라 부릅니다.<br>
해당 예제의 함수의 이름은 **greet_user()** 이고, 들여쓰기한 행은 모두 함수 **바디**이다.<br>

## 인수와 매개변수
```python
def greet_user(username):
    # 단순한 인사말을 표시합니다
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```
**greet_user()** 함수에 필요한 정보를 전달할 수 있습니다.<br>
해당 예제에서는 **username**을 변수로 받게 하였고, 이를 ```매개변수```라고 합니다.<br>
함수를 호출할 때에는 필요한 값을 넣었고, 이를 ```인수```라고 합니다.<br>

## 여러개의 매개변수
```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')    # I have hamster    My hamster's name is Harry.
describe_pet('dog', 'willie')       # I have dog        My dog's name is Willie.
```

이처럼 매개변수와 **똑같은 순서**로 전달하는 인수를 ```위치 인수```라고 합니다.<br>

```python
def describe_pet(animal_type, pet_name = 'harry'):
    print(f"\nI have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster')                              # I have hamster   My hamster's name is 
describe_pet('dog', pet_name = 'willie')             # I have dog       My dog's name is Willie.
describe_pet(pet_name = "willie", animal_type="dog") # I have dog       My dog's name is Willie.
```

이처럼, 함수에 전달하는 매개변수이름과 값을 동시에 전달하는 인수를 ```키워드 인수```라고 합니다.<br>
또한, 함수를 정의할 때 각 매개변수의 ```기본값```을 정의할 수 있으며, 함수를 호출할 때 인수가 없어도 됩니다.<br>

## 반환 값
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician) # Jimi  Hendrix

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician) # John Lee Hooker
```
```return 문```을 통해, 함수의 결과 값을 반환할 수 있습니다.

```python
def build_person(first_name, last_name):
    person = {"first" : first_name, "last" : last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician) # {'first': 'jimi', 'last': 'hendrix'}
```
**리스트**나 **딕셔너리** 같은 데이터 구조 또한 반환할 수 있습니다.

## 인자로 리스트 사용하기
```python
def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()!}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!
```
리스트를 **greet_user()** 함수에 전달하여 사용자 이름을 출력하는 예제입니다.<br>

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_complete_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []

print_models(unprinted_designs[:], complete_models)
show_complete_models(complete_models)


print(unprinted_designs) # ['phone case', 'robot pendant', 'dodecahedron']

complete_models = []
print_models(unprinted_designs, complete_models)

print(unprinted_designs) # []
```
함수 내부에서 리스트의 값을 수정할 수도 있습니다.<br>
반대로 리스트 내부의 값을 수정하지 못하게 하려면 인수 전달 시,<br>
```[:]``` 슬라이스 문법을 통해 리스트의 사본을 함수에 전달하면 됩니다.<br>

## 인수를 임의의 개수로 전달
```python
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
```*```을 통해, 여러개수의 인수를 전달할 수 있습니다.<br>
이때, 전달된 매개변수는 **튜플**의 형태로 전달됩니다.<br>

## 임의의 키워드 인수 사용
```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name']  = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile) 
# {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```
```**```을 통해 여러개수의 키워드 인수를 전달할 수 있습니다.<br>
이때, 전달된 매개변수는 **딕셔너리**의 형태로 전달됩니다.<br>

## 정의한 함수를 모듈에 저장하기
```python
#pizza.py
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
```import```문 을 통해서 **making_pizzas.py**에서 **pizza.py**에 정의된 **make_pizza()** 함수를 사용할 수 있습니다.

그 외에도, 아래와 같이 모듈을 임포트할 수 있습니다.<br>
```python
# 특정 함수 임포트하기
from pizza import make_pizza

make_pizza(16, 'pepperoni')

# as로 함수에 별칭 부여하기
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# as로 모듈에 별칭 부여하기
import pizza as p

p.make_pizza(16, 'pepperoni')

# 모듈의 함수를 모두 임포트하기
from pizza import *

make_pizza(16, 'pepperoni')
```
- 특정 함수를 임포트할 시, 전체 임포트할때처럼 점 표기법을 사용하지 않아도 됨
- as로 함수에 별칭을 부여할 시, **make_pizza()** 함수를 **mp()** 라는 별칭으로 바꿈<br>
- as로 모듈에 별칭을 부여할 시, **pizza**라는 모듈을 **p**라는 별칭으로 바꿈
- 모듈의 함수를 모두 임포트할 시, 마찬가지로 점 표기법을 사용하지 않아도 됨<br>
단, 해당 방식으로 임포트할 시 예기치 않은 오류가 발생할 수 있어 권장하지 않음<br>
예를 들어, 직접 정의한 함수와 같은 이름의 함수가 있다면 덮어씀.

