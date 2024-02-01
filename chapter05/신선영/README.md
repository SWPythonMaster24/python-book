# 5. if 문

# 1. 간단한 예제

```python
# if.py
cars = [ 'audi', 'bmw', 'subaru', 'toyota' ]

for car in cars:
    if car == 'bmw': # car의 값이 'bmw'와 같으면
        print(car.upper())
    else:
        print(car.title())
```

`if`를 써 현재 값이 bmw 인지 확인하고 맞으면 대문자로 출력한다.

코드를 실행하면 아래와 같은 결과가 나온다.

```python
Audi
BMW
Subaru
Toyota
```

# 2. 조건 테스트

- 동등 연산자(`=`)는 연산자의 왼쪽, 오른쪽 값이 같으면 True를, 아니면 False를 반환한다.
- 대소문자도 구분한다. (그렇기 때문에 대소문자 구분이 중요하지 않으면 변수의 값을 소문자로 변환하면 된다.)
- 불일치 연산자(`≠`)는 두 값이 다른지 확인할 때 사용한다.
- 숫자 비교도 가능한다
    - 이때 and, or도 함께 사용할 수 있다.
- 값이 리스트에 있는지 확인하려면 `in` 키워드를 사용한다.
- 값이 리스트에 없는지 확인하려면 `not in` 키워드를 사용한다.
- 불리언 표현식 (True, False)를 사용하면 상태나 조건을 효율적으로 관리할 수 있다.

```python
# if.py
car = 'audi'
print(car == 'audi') # True
print(car == 'bmw') # False
print(car == 'Audi') # False
print(car != 'Audi') # True

age = 19
print(age == 19)  # True
print(age < 21)  # True
print(age > 21)  # False
print(age <= 23 and age >= 18)  # True
print(age <= 23 or age >= 18)  # True

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False
print('pepperoni' not in requested_toppings)  # True
```

# 3. if문

`if` 뒤에 조건을 넣고, 들여 쓴 블록에는 거의 모든 코드를 쓸 수 있다. 

```python
if conditional_test
	do somthing
```

예를 들어 나이를 확인해 투표 가능 여부를 판단하는 코드는 아래와 같이 작성한다.

```python
# if.py
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

코드를 실행하면 아래와 같은 결과가 나온다.

```
You are old enough to vote!
Have you registered to vote yet?
```

- if-else: if문에 걸리지 않은 경우에는 `else`로 들어간다.
- if-elif-else: if문 이외에 다른 조건을 추가하고 싶을 때 `elif`를 추가한다. (else 블록을 생략할 수도 있다.)

```python
if age < 4:  # 4세 미만이면
    price = 0
elif age < 18: # 4세 이상 18세 미만이면
    price = 5
else: # 18세 이상이면
    price = 10

print(f"Your admission cost is ${price}.")
```

코드를 실행하면 아래와 같은 결과가 나온다.

```
Your admission cost is $5.
```

if문을 연속해서 사용해서 여러 조건을 테스트할 수도 있다.

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")
```

코드를 실행하면 아래와 같은 결과가 나온다.

```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

→ 이 코드를 if-elif-else를 사용한다면 하나 걸렸을 때 바로 멈춘다.

# 4. 리스트와 if문

- for문 안에 If문을 넣을 수 있다.
- 리스트가 비어 있는지 확인하려면 아래 코드와 같이 작성한다.

```python
# with_list.py
request_toppings = []
 
if request_toppings:
    for request_topping in request_toppings:
        print(f"Adding {request_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

코드를 실행하면 아래와 같은 결과가 나온다.

```
Are you sure you want a plain pizza?
```

# 5. if문 스타일

비교 연산자 주위에 공백 한칸을 써라!

```python
# Good!
if age > 4:

# Bad...
if age>4:
```