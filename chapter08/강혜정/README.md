# Chapter 8. 함수

## 함수 정의하기
```python
def greet_user():
    """단순한 인사말을 표시합니다"""
    print("Hello")

greet_user()

# 출력:
# Hello
```
- `def`는 함수를 정의하겠다는 뜻인 키워드이다. 이를 **함수 정의** 라 부른다.
- 함수 정의 다음에 들여 쓴 행은 모두 함수 **바디** 이다.
- 두 번째 행의 텍스트는 **독스트링** 으로 함수가 수행하는 작업을 설명하는 주석이다.
    - 파이썬은 함수 정의 바로 뒤에 있는 문자열을 사용해 함수에 대한 문서를 생성한다.
    - 독스트링은 보통 세 개의 따옴표(`"""docstring"""`)로 감싸며, 여러 행에 걸쳐 쓸 수 있다.
- **함수 호출** 은 파이썬에서 함수의 코드를 실행하도록 지시한다.

### 함수에 정보 전달하기
```python
def greet_user(username):
    """단순한 인사말을 표시합니다"""
    print(f"Hello, {username.title()}!")

greet_user("jesse")

# 출력:
# Hello, Jesse!
```
- 함수 정의 괄호 안에 username을 삽입하고, 함수 호출에 username을 추가하면 함수는 username에 지정한 값을 받는다.

### 인수와 매개변수
```python
def greet_user(username):   # username = 매개변수
    """단순한 인사말을 표시합니다"""
    print(f"Hello, {username.title()}!")

greet_user("jesse") # jesse = 인수
```
- greet_user()의 정의에 있는 username 변수는 함수가 동작하기 위해 필요한 정보로, **매개변수(parameter)** 라고 부른다.
- **인수(argument)** 는 함수를 호출할 때 함수로 전달되는 정보이다.


## 인수 전달하기
### 위치 인수
매개변수와 똑같은 순서로 전달하는 인수를 **위치 인수** 라고 한다.
```python
def describe_pet(animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 출력:
# I have a hamster.
# My hamster's name is Harry.
# 
# I have a dog.
# My dog's name is Willie.
```
- 함수는 필요한 만큼 호출할 수 있으며, 함수를 여러 번 호출하는 건 매우 효율적이다.
- 위치 인수의 순서가 틀리면 이상해질 수도 있기 때문에 순서가 중요하다.

### 키워드 인수
함수에 전달하는 이름-값 쌍이다. 이 문법에서는 인수를 쓸 때 이름과 값을 직접 연결하므로 잘못 할당되는 일이 없다.
```python
def describe_pet(animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```
- 키워드 인수를 사용하면 각 값이 매개변수에 정확히 할당되므로 순서는 중요하지 않다.
- 키워드 인수를 사용할 때는 함수 정의에 쓴 매개변수 이름을 정확히 사용해야 한다.

### 기본 값
함수를 정의할 때 각 매개변수의 기본 값을 지정할 수 있다. 매개변수의 기본 값을 지정해 두면 함수를 호출할 때 인수가 없어도 된다.

기본 값을 사용하면 함수 호출을 단순화하고 함수의 사용법도 명확해진다.

```python
def describe_pet(pet_name, animal_type='dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')  # 위치 인수
describe_pet(pet_name='willie') # 키워드 인수
```
> 기본 값이 있는 매개변수는 반드시 기본 값이 없는 매개변수보다 뒤에 정의해야 한다. 이렇게 해야 파이썬이 위치 인수를 정확히 해석할 수 있다.

### 인수 에러 피하기
- 매개변수 숫자와 인수 숫자가 일치하지 않으면 에러가 일어난다.
- 파이썬은 일부 정보가 누락됐음을 인식하고 다음과 같은 트레이스백을 표시한다.
```python
def describe_pet(pet_name, animal_type='dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

# Traceback (most recent call last):
#   File "pets.py", line 6, in <module>
#     describe_pet()
# TypeError: describe_pet() missing 1 required positional argument: 'pet_name'
```
매개변수 숫자와 인수 숫자가 일치하지 않으면 에러가 일어난다. 


## 반환 값
함수가 반환하는 값을 **반환 값(return value)** 이라고 한다. return 문은 함수 내부의 값을 가져와 처리한 후 호출한 행에 전달한다.

### 단순한 값 반환하기
값을 반환하는 함수를 호출할 때는 반환 값을 할당할 변수를 지정해야 한다.
```python
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 출력:
# Jimi Hendrix
```

### 인수를 옵션으로 만들기
중간 이름이 없는 사람도 있기 때문에 옵션으로 변경한다.
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 출력:
# Jimi Hendrix
# John Lee Hooker
```

### 딕셔너리 반환하기
함수의 반환 값에는 제한이 없으며 리스트나 딕셔너리 같은 복잡한 데이터 구조도 반환할 수 있다.
```python
def build_person(first_name, last_name):
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# 출력:
# {'first': 'jimi', 'last': 'hendrix'}
```

이 함수는 중간 이름, 나이, 직업 등 그 사람에 대해 저장할 수 있는 다른 정보를 받게끔 쉽게 확장할 수 있다.
```python
def build_person(first_name, last_name, age=None):
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 출력:
# {'first': 'jimi', 'last': 'hendrix', 'age': 27}
```
None은 일종의 플레이스홀더로, 조건 테스트에서 False로 평가된다.

### while 루프와 함수
```python
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 무한 루프입니다!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
```


## 함수에 리스트 전달하기
리스트를 함수에 전달하면 함수는 리스트의 내용에 직접 접근할 수 있다.
```python
def greet_users(names):
    """리스트의 사용자에게 단순한 인사말을 출력합니다"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 출력:
# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!
```

### 함수 내부에서 리스트 수정하기
리스트를 함수에 전달하면 함수는 전달받은 리스트를 수정할 수 있다. 함수 바디 내부에서 리스트를 변경한 내용은 모두 영구적이므로 데이터가 방대하더라도 효율적으로 동작한다.
```python
def print_models(unprinted_designs, completed_models):
    """
    남은게 없을 때까지 디자인을 출력합니다
    출력이 끝난 디자인을 completed_models 리스트로 이동합니다
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력된 모델을 모두 표시합니다"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```
- 이 프로그램은 함수가 없는 버전보다 확장, 유지 관리가 더 쉽다.
- 이 예제의 모든 함수가 한 가지 목적을 수행한다는 원칙도 잘 보여 준다.
    - 함수 하나가 너무 많은 작업을 수행한다면 되도록 여러 함수로 나눠 작업을 분활하기.


### 함수가 리스트를 수정하지 못하게 하기
함수에 원본이 아니라 사본을 전달하는 방식으로 해결할 수 있다.
```python
function_name(list_name[:]) # 슬라이스 문법
```
- 사본을 만드는 작업에도 시간과 메모리가 소모되므로, 특별한 이유가 없다면 원본 리스트를 함수에 효율적이다.
- 작업할 리스트가 클수록 시간과 메모리 소모가 커진다.


## 인수를 임의의 개수로 전달하기
파이썬에서는 함수에 전달된 인수를 하나로 모으는 기능이 있다.
```python
def make_pizza(*toppings):
    """요청받은 토핑 리스트를 출력합니다"""
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 출력:
# ('peperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')
```
파이썬은 *toppings 매개변수의 별( * )을 보고 이 함수가 전달받은 인수를 toppings *튜플* 에 모은다.

### 위치 인수와 임의의 인수 같이 쓰기
파이썬은 먼저 위치 인수와 키워드 인수를 할당한 다음, 남아 있는 인수를 마지막 매개변수에 모은다.

-> 임의의 인수를 모으는 매개변수는 반드시 마지막에 배치해야 한다!
```python
def make_pizza(size, *toppings):
    """주문 내용을 요약합니다"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
> 임의의 위치 인수를 수집하는 매개변수는 보통 *args라고 쓰기도 한다.

### 임의의 키워드 인수 사용하기
임의의 인수를 받아야 하는데 여러 가지 종료일 경우, 임의의 키-값 쌍을 받도록 함수를 정의한다.
```python
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

# 출력:
# {
#     'location': 'princeton', 
#     'field': 'physics', 
#     'first_name': 'albert', 
#     'last_name': 'einstein'
# }
```
파이썬은 **user_info의 별 두 개를 인식하고 이름-값 쌍 인수를 모두 user_info 딕셔너리에 저장한다.
> 임의의 키워드 인수를 수집하는 매개변수는 보통 **kwargs(keyword arguments) 라는 이름을 쓴다.


## 함수를 모듈에 저장하기
함수는 모듈이라는 별도의 파일에 저장하고, 이 모듈을 메인 프로그램으로 임포트하면
1) 함수를 별도의 파일에 저장하여 프로그램의 세부 사항을 가려 전체적인 흐름에 집중할 수 있다
2) 다양한 프로그램에서 함수를 활용할 수 있다
3) 함수를 별도의 파일에 저장하면 다른 프로그래머와 해당 파일만 공유할 수도 있다.

### 전체 모듈 임포트하기
```python
import module_name

# ex.
# import pizza
# pizza.make_pizza(16, 'peperoni')
```

### 특정 함수 임포트하기
```python
module_name import function_name

# ex.
# from piaaz import make_pizza
# make_pizza(16, 'peperoni')
```

### as로 함수에 별칭 부여하기
```python
module_name import function_name as fn

# ex.
# from piaaz import make_pizza as mp
# mp(16, 'peperoni')
```

### as로 모듈에 별칭 부여하기
```python
import module_name as mn

# ex.
# import pizza as p
# p.make_pizza(16, 'peperoni')
```

### 모듈의 함수를 모두 임포트하기
```python
from module_name import *
```
이 방법은 점 표기법을 사용하지 않고 함수 이름을 바로 호출하기 때문에 권장하지 않는다.

임포트한 모듈에 개인이 만든 함수 이름과 같은 함수가 있다면, 이름이 같은 함수와 변수를 별도로 임포트하는 대신 덮어쓴다.

## 함수 스타일
- 함수 이름은 뜻이 분명해야 하고, 소문자와 밑줄만 사용해야 한다.
- 모든 함수에는 함수가 하는 일을 간결하게 설명하는 주석이 있어야 한다. -> 독스트링 형태
- 매개변수의 개본 값을 지정할 때는 등호 주변에 공백이 없어야 한다.
- 함수 호출의 키워드 인수에도 공백을 사용하면 안된다.
- 프로그램이나 모듈에 함수가 둘 이상 있는 경우 두 함수를 두 개의 빈 줄로 구분해야 한다.
- 모든 import 문은 파일 처음에 써야 한다.

제일 좋은 건 코드 스타일 자동화 하는 것!!
- https://black.readthedocs.io/en/latest/