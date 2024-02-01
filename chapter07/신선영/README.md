# 7. 사용자 입력과 while 루프

`input()`을 사용하면 사용자의 입력을 받을 수 있다.

# 1. input() 함수의 동작 방식

```python
# input.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
```

여기에서 `input()`  메서드의 전달 인자는 사용자에게 어떤 값을 입력해야 할지에 대한 프롬프트이다. 뒤에 항상 공백을 넣어 사용자 입력이 구분되게 하는 것이 좋다. 또한 한 행 이상일 수도 있다.

코드를 실행하면 아래와 같이 출력된다.

```
If you tell us who you are, we can personalize the messages you see.
What is your first name? fresh

Hello, fresh!
```

입력 받은 값은 항상 문자열이기 때문에 숫자로 변환하고 싶다면 `int()` 함수로 감싸면 된다.

# 2. while 루프 소개

특정 조건을 통과하는 한 계속 실행된다. 아래 코드의 경우에는 cuuent_number ≤ 조건을 통과하는 한 루프를 계속 반복한다.

```python
# while.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

코드를 실행하면 아래와 같이 출력된다.

```
1
2
3
4
5
```

만약 사용자가 종료 시점을 선택할 수록 있게 하려면, `input()`과 `if`를 적절히 활용하면 된다.

또한 테스트 결과와 관계 없이 while 문을 즉시 종료하고 싶으면 `break`를,

루프의 처음으로 돌아가고 싶다면 `contiue`를 사용하면 된다.

```python
# while.py
current_number = 1
while current_number <= 10:

    if (current_number % 2 == 0):
        current_number += 1
        continue

    if current_number == 7:
        break

    print(current_number)
    current_number += 1
```

코드를 실행하면 아래와 같이 출력된다.

```
1
3
5
```

무한 루프가 걸렸으면 `ctrl` + `C`를 눌러 종료한다. 항상 테스트를 하는 것이 중요하다.

# 3. 리스트, 딕셔너리와 함께 while 루프 사용하기

리스트에서 특정 값을 모두 제거할 수 있다.

```python
# pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)
```

코드를 실행하면 아래와 같이 출력된다.

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

또한 사용자가 입력한 값으로 딕셔너리를 채울 수도 있다.

```python
# mountain_poll.py
responses = {}

# 설문조사를 제어할 플래그
polling_active = True
while polling_active:
    # 이름과 응답을 저장한다.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장한다.
    responses[name] = response

    # 누군가 더 설문에 참여할 것인지 묻는다.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 설문결과를 출력한다.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```

코드를 실행하면 아래와 같이 출력된다.

```
What is your name? fresh
Which mountain would you like to climb someday? I hate climb ...
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
fresh would like to climb I hate climb ....
```