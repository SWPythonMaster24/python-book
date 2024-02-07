# 8장. 함수

별도의 이름을 가졌고, 특정 작업만 하도록 설계된 **코드 블록**

함수를 호출하게 되면 함수에 정의된 작업이 수행된다.

**모듈**이라는 별도의 파일에 함수를 저장해 메인 프로그램을 간결하게 정리하기도 함 

# 1. 함수 정의하기

```python
# function.py
def greet_user():
    """단순한 인사말을 출력합니다."""
    print("Hello!")

greet_user()
```

- `def` 키워드로 함수를 정의한다.
- `def greet_user()` 다음에 들여 쓴 행은 모두 함수 바디(body)로 취급한다.
- 두 번째 행의 텍스트는 함수가 수행하는 작업을 설명하는 **독스트링(docstring)**이다. (실제로 실행되진 X)
    - 세 개의 따옴표로 감싸고, 여러 행에 걸쳐 쓴다.
- 함수 호출(function call)은 파이썬에게 함수의 코드를 실행하도록 지시함

코드를 실행하면 아래와 같이 출력된다.

```python
Hello!
```

`()` 안에 필요한 값을 전달할 수도 있다. ex) `def greet_user (username)` (여기에서 username을 **매개변수**라고 함)

`greet_user('jesse')`  jesse는 **인수**라고 함

# 2. 인수 전달하기

- 매개변수와 똑같은 순서로 전달하는 **위치 인수**
- 변수 이름과 값을 함께 전달하는 인수를 **키워드 인수**

## 1. 위치 인수

간단한 방법은 인수의 순서, 매개변수 순서와 맞추는 것

```python
# function.py
def describe_pet(animal_type, pet_name):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
```

코드를 실행하면 아래와 같이 출력된다.

```
I have a hamster.
My hamster's name is Harry.
```

단, 위치 인수의 순서가 틀리면 예상하지 못한 문제가 생길 수도 있으니 조심해야 한다.

## 2. 키워드 인수

이름-값 쌍을 표시해서 넘겨주는 방식

```python
# function.py 
describe_pet(animal_type='hamster', pet_name='harry')
```

잘못 할당되는 일이 없음. 순서는 중요하지 않다.

## 3. 기본 값

기본 값을 설정할 수 있다. 그렇기 때문에 함수를 호출할 때 인수가 없어도 된다.

```python
# function.py 
def describe_pet(animal_type, pet_name='willie'):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='dog')
```

코드를 실행하면 아래와 같이 출력된다.

```python
I have a dog.
My dog's name is Willie.
```

인수를 명시적으로 전달하면 파이썬은 매개변수 기본 값을 무시한다.

**(기본 값이 있는 매개변수는 반드시 기본 값이 없는 매개변수보다 뒤에 정의해야 한다.)**

- 위치 인수
- 키워드 인수
- 기본 값

이것들을 모두 섞어 쓸 수 있으므로 함수를 여러 가지 방식으로 호출해도 결과가 같다.

편한대로!

## 5. 인수 에러 피하기

- 트레이스백이 찾을 수도 있고
- 잘못된 함수 호출이 있을 수도 있고
- 함수를 호출할 때 인수 두 개를 누락했음을 보여 주고, 어떤 인수를 누락했는지도 알려준다.

# 3. 반환 값

## 1. 단순한 값 반환하기

`return` 키워드와 함께 쓰면 된다.

```python
# function.py
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

반환 값을 `return` 키워드와 함께 사용하면 됨

```python
Jimi Hendrix
```

## 2. 인수를 옵션으로 만들기

이런 식으로 기본값을 넣어 옵션으로 만들 수 있다.

```python
# function.py
def get_formatted_name(first_name, last_name, middle_name=''):
    """읽기 쉬운 전체 이름을 반환합니다."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

코드를 실행하면 아래와 같이 출력된다.

```python
John Lee Hooker
Jimi Hendrix
```

## 3. 딕셔너리 반환하기

리스트, 딕셔너리 같은 복잡한 데이터 구조도 반환할 수 있다.

```python
# function.py
def build_person(first_name, last_name, age=None):
    """사람에 관한 정보 딕셔너리를 반환합니다."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

코드를 실행하면 아래와 같이 출력된다.

```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

기본값을 `None` 으로 지정할 수 있다.

이러면 조건 테스트에서 False로 평가된다.

함수 안에 `while`문을 사용할 수도 있다. 이 때는 **무한 루프를 타지 않게** 조심해야 한다.

# 4. 함수에 리스트 전달하기

```python
# function.py
def greet_users(names):
    """리스트의 각 사용자에게 단순한 인사말을 출력합니다."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

이름, 숫자, 딕셔너리 등의 리스트를 함수에 전달할 수도 있습니다. 

```
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

## 1. 함수 내부에서 리스트 수정하기

리스트를 함수에 전달하면 함수는 전달받은 리스트를 수정할 수 있다.

리스트 변경은 영구적이므로 데이터가 방대하더라도 효율적으로 동작합니다.

```python
# function.py
# 출력할 디자인을 저장합니다.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 게 없을 때까지 디자인을 출력합니다
# 출력한 디자인을 completed_models로 옮깁니다
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 완료된 디자인을 표시합니다
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

먼저 출력할 디자인 리스트인 `unprinted_designs`,

출력이 끝난 디자인을 옮길 `completed_models`,

`unprinted_designs` 에 저장하고 현재 디자인을 출력하고 있다는 메시지를 표시합니다.

`completed_model` 리스트로 디자인을 옮긴다.

코드를 실행하면 아래와 같이 출력된다.

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case
```

## 2. 함수가 리스트를 수정하지 못하게 하기

리스트 사본을 만들어서 전달하는 방식으로 문제를 해결할 수 있다.

```python
function_name(list_name[:])
```

근데 특별한 이유가 없으면 원본 리스트를 함수에 전달하는게 좋다.

시간, 메모리 소모가 커지기 때문이다.

# 5. 인수를 임의의 개수로 전달하기

```python
# function.py
def make_pizza(*toppings):
    """만들고자 하는 피자를 요약합니다."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

`*`을 사용하면 임의의 개수 인수를 받을 수 있다.

코드를 실행하면 아래와 같이 출력된다.

```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

## 1. 위치 인수와 임의의 인수 같이 쓰기

**임의의 인수를 모으는 매개변수는 반드시 마지막에 배치해야 한다!!**

## 2. 임의의 키워드 인수 사용하기

임의의 인수를 받아야 하는데 여러 가지 종류일 때는 아래와 같이 `**` 을 사용하면 된다.

```python
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')

print(user_profile)
```

`**`을 사용하면 사용자에 관한 정보를 이름-값 쌍으로 제한 없이 받는다.

보통 임의의 키워드 인수를 수집하는 매개변수는 보통 ****kwargs(keyword arguments)**라는 이름을 쓴다.

# 6. 함수를 모듈에 저장하기

함수를 모듈이라는 별도의 파일에 저장하고, `import` 하면 된다.

```python
# pizza.py
def make_pizza(size, *toppings):
    """만들고자 하는 피자를 요약합니다."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

이렇게 사용하면 된다.

이 파일을 읽고 import pizza 행에서 [pizza.py](http://pizza.py) 파일을 열어 모든 함수를 프로그램에 복사한다.

실제로 함수를 복사하는 코드는 없지만, 파이썬이 프로그램을 실행하기 직전에 내부적으로 함수를 복사한다.

임포트한 모듈에서 함수를 호출하려면 `.` 을 찍고 함수 이름을 호출하면 된다.

코드를 실행하면 아래와 같이 출력된다.

```
 Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

## 2. 특정 함수 임포트하기

```python
from module_name import function_name
```

이렇게 해서 원하는 함수만 임포트할 수도 있습니다.

```python
# making_pizzas.py
from pizza import make_pizza  

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

as로 별칭을 부여할 수도 있다.

```python
# making_pizzas.py
from pizza import make_pizza as mp # 함수 이름에 별칭 부여

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# making_pizzas.py
from pizza as p # 모듈에 별칭 부여

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# making_pizzas.py
from pizza import * # 모듈의 함수를 모두 임포트한다.

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

# 7. 함수 스타일

- 함수의 이름은 뜻이 분명해야 하고
- 소문자와 밑줄만 사용해야 함
- 뜻이 분명한 이름을 써야 함
- 모든 함수에는 함수가 하는 일을 간결하게 설명하는 주석이 있어야 함
    - 독스트링 형식
- 매개변수 기본 값을 지정할 때는 등호 주위에 공백이 없어야 한다.
- 함수 호출 키워드 인수에도 공백을 사용하면안 됨
- 각 행의 코드를 79자로 제한 함
- 프로그램이나 모듈에 함수가 둘 이상 있는 경우 두 함수를 두 개의 빈 줄로 구분해야 함
- 모든 import 문은 파일 처음에 써야 한다.