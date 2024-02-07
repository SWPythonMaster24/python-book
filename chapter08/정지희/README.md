---
marp: true
theme: uncover
---
# **챕터8 함수**
---
## **함수**
##### 함수는 별도의 이름을 지니며, <br> 특정 작업만 하도록 설계된 코드 블록이다.<br>모듈이라는 별도의 파일에 함수를 저장해 간결하게 정리가능.
---
## **함수 정의**
```python
def greet_users() :
    """"단순한 인사말을 표시합니다"""
    print("Hello")

greet_user()
```
##### def를 통해 함수 정의가 가능하다. <br>def greet_user(): 다음에 들여쓴 행은 모두 함수 바디.<br>두번째 행은 수행하는 작업을 설명하는 독스트링.<br>마지막행과 같이 함수 호출을 통해 코드 실행을 지시한다.
---
## **인수와 매개변수**
```python
def greet_users(names) :
```
##### 함수가 동작하기 위해 필요한 정보를 매개변수라고 부른다
```python
greet_users('coco') :
```
##### 실제 함수호출 시 넘기는 names로 넘기는 값을 인수라 부름.
---
## **인수 전달1**
```python
def describe_pet(pet_name, animal_type):
describe_pet('harry', 'dog')
```
###### 인수의 순서를 매개변수 순서와 맞춰 할당하는데 이렇게 전달하는 인수를 위치 인수라 한다.<br>단, 순서가 틀리면 예상치 못한 문제가 발생할 수 있어 주의해야함.
```python
describe_pet(animal_type='hamster', pet_name='harry')
```
###### 키워드 인수는 함수에 이름(매개변수명)-값(인수) 쌍으로 전달한다.<br>순서는 상관없음. 단, 매개변수 이름을 정확히 사용해야함.
---
## **인수 전달2**
```python
def describe_pet(pet_name, animal_type='dog'):

describe_pet('whille')
```
###### 함수 정의 시 각 매개변수의 기본 값을 지정 가능하며,<br> 인수가 없을 시 기본 값을 사용한다.
```python
def describe_pet(pet_name, animal_type):

describe_pet(animal_type='cat')
```
###### 함수 호출 시 인수의 수가 매개변수의 수와 불일치 시 에러가 발생된다.
---
## **반환 값**
##### 함수가 반환하는 값을 반환 값이라 하며,<br> return문을 통해 값을 반환한다.
---
## **함수에 리스트 전달**
```python
def greet_users(names) :
    """"단순한 인사말을 표시합니다"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_users(username)
```
##### 이름, 숫자, 딕셔너리 등의 리스트를 함수에 전달할 수도 있다.
---
## **1) 함수 내부에서 리스트 수정**
###### 함수에 리스트 전달 후 함수 바디 내부에서 리스트 수정이 가능하며, 변경된 내용은 모두 영구적이므로 데이터가 방대하더라도 효율적으로 동작한다.
```python
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """"
    남은게 없을 때까지 디자인을 출력합니다.
    출력이 끝난 디자인을 completed_models 리스트로 이동합니다.
    """
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        completed_models.append(current_desing)
```
---
## **2) 함수가 리스트 수정 못하게 막기**
###### 리스트 사본을 만들어서 전달하는 방식으로 원본 리스트를 유지 할 수 있다.
```python
print_models(unprinted_designs[:], completed_models):
```
>사본을 만드는 작업에도 시간과 메모리가 소모되므로, <br>특별한 이유가 없다면 원본 리스트를 사용하는게 효율적이다.
---
## **인수를 임의의 개수로 전달**
```python
def make_pizza(*toppings):
    print(toppings)
    
make_pizza('cheese', 'mushroom')
```
###### 매개변수의 별(*)을 보고 함수가 전달받은 인수를 toppings 튜플에 모은다. 
```
('cheese', 'mushroom')
```
###### 함수가 받는 인수 개수를 미리 알 수 없을 때 사용한다.
---
## **함수를 모듈에 저장**
###### 함수를 모듈이라는 별도의 파일에 저장하고,<br> 이 모듈을 메인 프로그램으로 임포트해 사용가능하다. 
```python
# pizza.py
def make_pizza(size, *toppings):
```
###### 모듈은 프로그램으로 가져올 코드가 포함된 .py로 끝나는 파일이다. 
---
## **1) 함수 임포트**
```python
import pizza

pizza.make_pizza(16, "pepperoni")
```
###### import를 통해 pizza.py 파일을 열어 내부적으로 모든 함수를 복사한다.<br>임포트한 모듈에서 함수 호출을 하려면 모듈이름.함수이름을 쓰면된다.
---
## **2) 특정 함수 임포트, 별칭 부여**
```python
from module_name import function_name
```
###### 위와 같은 문법으로 모듈에서 원하는 함수만 임포트가 가능하다.
```python
from pizza import make_pizza as mp

mp(16, "pepperoni")
```
###### 임포트할 함수명이 기존 함수명과 충돌 혹은, 너무 길다면 짧고 고유한 별칭을 as 키워드를 통해 만들 수 있다.