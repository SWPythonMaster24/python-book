# Chapter 5. if 문

## 조건 테스트
if 문의 핵심은 True 또는 Flase로 평가되는 표현식이며, 이를 *조건 테스트* 라고도 부른다.

조건 테스트가 True로 평가되면 if 문 다음에 있는 코드를 실행하고, False로 평가되면 if문 다음의 코드를 무시한다.

### 동일성 확인하기
```python
>>> car = 'bmw' # 할당
>>> car == 'bmw' # 동등연산자
True
```
동등 연산자는 연산자의 왼쪽과 오른쪽 값이 일치하면 True를 반환하고, 그렇지 않으면 False를 반환한다.

### 동일성을 체크할 때 대소문자 무시하기
파이썬은 동일성을 체크할 때 대소문자를 구분하므로, 철자가 같아도 대소문가 구성이 다른 값은 일치하지 않는다고 판단한다.

하지만 대소문자 구분이 중요하지 않은 경우에는 lower()를 사용하여 변수의 값을 소문자로 변환하여 구분할 수 있다.
```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
```

### 불일치 확인하기
두 값이 다른지 확인할 때는 *불일치 연산자* 인 !=를 사용한다.

두 값이 일치하지 않으면 True로 평가하고 if 문 다음의 코드를 실행한다. 두 값이 일치하면 False로 평가하고 if 문 다음의 코드를 무시한다.

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# 출력:
# Hold the anchovies!
```

### 숫자 비교하기
숫자 또한 비교할 수 있으며, 이상, 이하, 미만, 초과 같은 조건도 테스트할 수 있다.
```python
>>> answer = 17
>>> answer != 42
True

>>> age = 19
>>> age < 21 # 미만
True
>>> age <= 21 # 이하
True
>>> age > 21 # 초과
False
>>> age >= 21 # 이상
False
```

### 여러 조건 확인하기
#### 모두 만족해야 하는 and
두 조건이 모두 통과하면 전체 표현식이 True로 평가된다. 두 조건 중 하나라도 실패하면 표현식은 False로 평가된다.
```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21 # False and True이므로 False로 평가
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21 # True and True이므로 True로 평가
True
```

#### 하나만 만족해도 되는 or
개별 테스트 중 하나만 통과해도 전체 테스트가 통과한다. or 표현식은 두 테스트가 모두 실패할 때만 실패한다.
```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21 # True or False
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21 # False or False
False
```

### 값이 리스트에 있는지 확인하기
in 키워드를 사용한다.
```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 값이 리스트에 없는지 확인하기
not 키워드를 사용한다.
```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Marie, you can post a response if you wish.
```

### 불리언 표현식
불리언 값은 조건 표현식의 평가 결과와 마찬가지로 True 또는 False 이다.
```python
game_active = True
can_edit = False
```
불리언 값을 활용하면 프로그램에서 중요한 상태나 조건을 효율적으로 관리할 수 있다.


## if 문
### 단순한 if 문
테스트가 통과하면 if 문 다음에 들여 쓴 행이 모두 실행되고, 테스트가 실패하면 들여 쓴 행을 모두 무시한다.
```python
if conditional_test:
    do something
```

### if-else 문
if-else 문은 단순한 if 문과 비슷하며, else 블록을 써서 조건 테스트가 실패했을 때 할 행동을 지정한다.
```python
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

# 출력:
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!
```

### if-elif-else 문
경우의 수가 셋 이상일 때는 if-elif-else 문을 사용한다.

파이썬은 각 조건 테스트를 순서대로 실행하며 통과하는 테스트가 있을 때까지 계속한다. 테스트가 통과하면 해당 테스트 다음의 코드를 실행하고 나머지 테스트는 건너뛴다.
```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("You admission cost is $25.")
else:
    print("Your admission cost is $40.")

# 출력:
# You admission cost is $25.
```

위에 예제 코드 같은 경우는 입장료를 출력하는 것보다는, if-elif-else 문 안에서는 입장료를 저장만 하고, 평가가 끝난 후 print()를 하나만 쓰는 편이 더 간결하다.
```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"You admission cost is ${price}.")
```
수정한 코드는 더 효율적일 뿐만 아니라, 원래 코드보다 수정하기도 더 쉽다 👍

### 여러 개의 elif 블록 쓰기
elif 블록은 원하는 만큼 사용할 수 있다.
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

print(f"You admission cost is ${price}.")
```

### else 블록 생략하기
if-elif 문 마지막에 꼭 else 블록을 써야 하는 건 아니다!

else 블록은 말하자면 폴백(catch-all) 문이다. 특정한 if나 elif 조건에 맞지 않는 모든 경우에 실행되는데, 이렇게 할 경우 요휴하지 않은 데이터가 들어오거나 악의적인 데이터가 들어올 수도 있다.

### 여러 조건 테스트하기
여러 조건을 모두 체크해야 할 때는 if 문을 연속해서 사용할 수 있습니다. 이 방식은 둘 이상의 조건이 통과할 수 있고, 통과하는 모든 조건에 맞게 행동하려는 경우에 적합하다.
```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 출력:
# Adding mushrooms.
# Adding extra cheese.
#
# Finished making your pizza!
```


## 리스트와 if 문
### 특별한 요소 확인하기
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza!")
```

### 리스트가 비어 있지 않은지 확인하기
사용자가 제공하는 정보를 사용하는 경우 리스트에 반드시 어떤 요소에 존재한다고 확신할 수 없다. 이런 상황에서는 for 루프를 실행하기 전에 빈 리스트인지 먼저 확인하는 게 좋다.
```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("\nFinished making your pizza!")
else:
        print("Are you sure you want a plain pizza?")

# 출력:
# Are you sure you want a plain pizza?
```

### 여러 개의 리스트 다루기
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sory, we don't have {requested_toppings}.")

print("\nFinished making your pizza!")

# 출력:
# Adding mushrooms
# Sory, we don't have french fries
# Adding extra cheese
#
# Finished making your pizza!
```