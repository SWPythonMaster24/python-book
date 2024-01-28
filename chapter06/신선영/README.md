# 6. 딕셔너리

사람을 표현하는 딕셔너리를 만들면 그 안에 정보를 원하는 만큼 저장할 수 있다.

# 1. 단순한 딕셔너리

**키-값 쌍 컬렉션**입니다. 각 **키**는 **값**에 연결되어 있고, 키를 사용해 그 값에 접근할 수 있다.

```python
# dic.py
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(f"You just earned {alien_0['points']} points!")
```

저장할 땐 `:` 를 구분자로 저장하고, 출력할 땐 `[]` 사이에 key를 넣어 출력한다.

코드를 실행하면 아래와 같이 출력된다.

```
green
5
You just earned 5 points!
```

# 2. 딕셔너리 사용하기

딕너리는 동적 구조이기 때문에 언제든지 새 키-값 쌍을 출가할 수 있다.

1장의 예제 코드에서 이어 아래 코드를 추가로 작성해보자!

```python
# dic.py
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

코드를 실행하면 아래와 같이 출력된다.

```
{
'color': 'green', 
'points': 5, 
'x_position': 0, 
'y_position': 25
}
```

빈 딕셔너리로 시작하고 싶으면 단순히 `{}` 로 대입하면 된다.

만약 키-값 쌍을 제거하고 싶으면 `del` 문을 이용한다.

```python
# dic.py
del alien_0['points']
print(alien_0) 
```

코드를 실행하면 아래와 같이 출력된다.

```
{
'color': 'green', 
'x_position': 0, 
'y_position': 25
}
```

보통 딕셔너리를 정의에 여러 행이 필요하다면, 

- 여는 중괄호 다음에 엔터
- 다음 행은 공백 네칸
- 첫 번째 키-값 쌍을 쓴 다음 콤마
- 이후에 엔터를 누르면 자동으로 들여쓰기가 된다.

```python
# dic.py

# 이렇게~!
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python'
}
```

> 🤔 만약 존재하지 않는 키에 접근하면 어떻게 될까?
> 

아래와 같은 에러가 발생한다

```python
Traceback (most recent call last):
  File "/Users/~/PycharmProjects/book/dic.py", line 15, in <module>
    del alien_0['키 값']
KeyError: '키 값'
```

그래서 키가 있는지 먼저 확인하고, 가져오게 하려면 아래와 같이 코드를 작성하면 된다.

```python
# dic.py
print(favorite_languages.get('jen', 'No favorite language set.'))
print(favorite_languages.get('jenny', 'No favorite language set.'))
print(favorite_languages.get('jenny'))
```

코드를 실행하면 아래와 같이 출력된다.

```
python
No favorite language set.
None # 아무것도 없다는 의미! 에러가 아님
```

# 3. 딕셔너리 순회하기

이렇게 사용하면 된다.

```python
for k, v in #{딕셔너리 이름}.items()
```

예를 들면 이렇게 작성한다.

```python
#dic.py
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

코드를 실행하면 아래와 같이 출력된다.

```python
Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```

key, value 라는 이름 대신 다른 이름을 써도 된다.

예를 들어 `name`, `language` 같은 이름을 써도 알아서 `key`, `value` 값이 들어간다.

`keys()`를 사용할 수도 있다.

```python
# dic.py
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f" Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
```

코드를 실행하면 아래와 같이 출력된다.

```python
Sarah
 Hi Sarah, I see your favorite language is C!
Edward
Phil
 Hi Phil, I see your favorite language is Python!
```

물론 딕셔너리에서도 사용이 가능하다. 딕셔너리에서 `keys()`를 호출하면 key 값만 순회하면서 출력된다.

만약 값만 순회하고 싶다면 `values()` 메서드 이용하기

`set()` 으로 감싸면 중복 없이 출력된다.

```python
set(values()) # 딕셔너리의 값만 중복 없이
```

# 4. 중첩

- 리스트 안에 딕셔너리를 저장
- 딕셔너리 안에 리스트를 저장
- 딕셔너리 안에 딕셔너리를 저장

모~두 가능하다. 이걸 중첩이라고 한다.

### 딕셔너리를 담은 리스트

```python
# aliens.py
# 외계인을 저장할 빈 리스트를 만든다.
aliens = []

# 녹색 외계인을 30명 만든다.
for alien_number in range(30): # 숫자만큼 루프를 반복
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # 리스트에 추가
 
# 처음 다섯 외계인을 표시한다.
for alien in aliens[:5]: # 처음 5명의 외계인을 출력
    print(alien)
print("...")

# 생성된 외계인이 얼마나 많은지 표시한다.
print(f"Total number of aliens: {len(aliens)}") # 개수 출력
```

코드를 실행하면 아래와 같이 출력된다.

```
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number of aliens: 30
```

여기에 if문을 적절히 섞어서 값을 변경할 수도 있다.

### 리스트를 담은 딕셔너리

```python
# pizza.py
# 주문받은 피자 정보를 저장한다.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 요약된 주문 정보를 출력한다.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```

코드를 실행하면 아래와 같이 출력된다.

```
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese
```

### 딕셔너리 속의 딕셔너리

도 할 수는 있지만 너무 복잡하다.

가급적이면 지양하는게 좋을 것 같다.

```python
# users.py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

```
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris
```