# Chapter 6. 딕셔너리

## 딕셔너리 사용하기
파이썬 딕셔너리는 키-값 쌍(key-value pairs) 컬렉션이다. 각 키는 값에 연결되어 있고, 키를 사용해 그 값에 접근할 수 있다. 키의 값에는 숫자, 문자열, 리스트, 다른 딕셔너리 등을 쓸 수 있으며, 파이썬에서 생성할 수 있는 객체는 모두 딕셔너리의 값이 될 수 있다.

파이썬의 딕셔너리는 중괄호({})로 표현하고, 그 안에 일련의 키-값 쌍을 쓴다.
```python
alien_0 = { 'color': 'green', 'points': 5 }
```
키-값 쌍은 서로 연결된 세트로, 키를 제공하면 파이썬은 그 키에 할당된 값을 반환한다.

### 딕셔너리 값에 접근하기
```python
alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0['color']) # 값 접근 방법

# 출력:
# green
```
딕셔너리에 저장할 수 있는 키-값 쌍의 숫자는 제한이 없다. 

### 키-값 쌍 추가하기
딕셔너리는 동적 구조이며 언제든지 새 키-값 쌍을 추가할 수 있다.
```python
alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0)

alien_0['x_position'] = 0 # 추가 방법
alien_0['y_position'] = 25
print(alien_0)

# 출력:
# { 'color': 'green', 'points': 5 }
# { 'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25 }
```
딕셔너리는 정의된 순서를 유지하여, 딕셔너리 자체를 출력하거나 루프 안에서 요소를 출력하면 딕셔너리에 두가한 순서대로 출력된다.

### 빈 딕셔너리로 시작하기
빈 딕셔너리를 채울 때는 먼저 빈 딕셔너리를 정의한 다음 키-값 쌍을 한 행에 하나씩 추가한다.
```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```
빈 딕셔너리는 보통 사용자 제공 데이터를 저장하거나, 키-값 쌍을 자동으로 생성하는 코드에서 사용한다.

### 딕셔너리 값 수정하기
```python
alien_0 = { 'color': 'green' }
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# 출력:
# The alien is green.
# The alien is now yellow.
```

### 키-값 쌍 제거하기
딕셔너리에 저장한 정보가 필요 없어지면 del 문으로 키-값 쌍을 제거할 수 있다. 
del 문에는 딕셔너리 이름과 제거할 키만 제공하면 된다. 
```python
alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0)

del alien_0['points'] # 영구히 제거
print(alien_0)

# 출력: 
# { 'color': 'green', 'points': 5 }
# { 'color': 'green' }
```

### 비슷한 객체의 딕셔너리
딕셔너리 하나에 여러 객체에 공통인 정보를 저장할 수도 있다.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust'.
    'phill': 'python',
}
```
딕셔너리 정의에 여러 행이 필요하다면 여는 중괄호 다음에 Enter 키를 누른다. 그리고 다음 행을 공백 네 칸 들여 쓰고, 첫 번째 키-값 쌍을 쓴 다음 콤마를 쓴다. 이후에 Enter 키를 누르면 텍스트 에디터가 자동으로 다음 키-값 쌍을 모두 들여쓴다!


> 마지막 키-값 쌍 뒤에 콤마 하나를 남겨두는 것은 나중에 키-값 쌍을 추가할 때 실수를 방지하는 좋은 습관이다.

### get()으로 값을 접근하기
대괄호 안에 키를 써서 값을 가져오는 문법의 경우, 요청한 키가 존재하지 않으면 에러가 발생하는 문제가 있다.
```python
alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0['point'])

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 2, in <module>
    print(alien_0['point'])
          ~~~~~~~^^^^^^^^^
KeyError: 'point'
```

딕셔너리의 경우, get() 메서드를 사용하면 요청한 키가 존재하지 않을 때 반환될 기본 값을 정할 수 있다.
```python
alien_0 = { 'color': 'green', 'points': 5 }

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 출력:
# No point value assigned.
```
get()에 두 번째 인수를 지정하지 않고 해당 키도 없다면 파이썬은 None 값을 반환한다. (8장에서 계속...)


## 딕셔너리 순회하기
### 키-값 쌍 순회하기
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 출력:
# Key: username
# Value efermi
# 
# Key: first
# Value enrico
# 
# Key: last
# Value fermi
# 
```
변수 이름 다음에는 딕셔너리 이름을 쓰고, 그 뒤에 키-값 쌍을 반환하는 items() 메서드를 사용한다.

### 딕셔너리 키 순화하기
딕셔너리의 값이 필요하지 않을 때는 keys() 메서드를 사용한다.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust'.
    'phill': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Jen
# Sarah
# Edward
# Phill
```
딕셔너리 순회의 기본 값은 키만 순회하는 것이므로 두 코드의 결과는 똑같다.
```python
for name in favorite_languages:

for name in favorite_languages.keys():
```

### 딕셔너리 키를 순서에 따라 순회하기
for 루프에서 반환하는 키를 정렬하는 방법은 sorted() 함수를 써서 정렬하면 된다
```python
for language in sorted(favorite_languages.keys()):
    print(language.title())
```

### 딕셔너리의 값 순회하기
values() 메서드는 딕셔너리의 값을 반환한다
```python
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()): # set()을 통해 중복을 제거할 수 있다
    print(language.title())
```


## 중첩
리스트 안에 딕셔너리를, 딕셔너리 안에 리스트를, 딕셔너리 안에 딕셔너리를 중첩할 수 있다.

### 딕셔너리를 담은 리스트
```
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

### 리스트를 담은 딕셔너리
```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```