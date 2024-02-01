# Chapter 7. 사용자 입력과 while 루프

대부분의 프로그램은 사용자의 문제를 해결하기 위해 작성합니다. 이를 위해서는 사용자로부터 정보를 얻어야 합니다. 프로그램에 사용자 정보가 필요하면 사용자에게 정보를 묻는 프롬프트를 표시해야 합니다. input() 함수는 바로 이럴 때 사용합니다.

input()과 while 루프를 배워 사용자 입력을 처리하는 기능, 동작 실행 시간을 제어하는 기능을 다루면 대화형 프로그램을 작성할 수 있습니다.

## input() 함수의 동작 방식

input() 함수는 프로그램을 일시 중지하고 사용자가 텍스트를 입력할 때까지 기다립니다. 그리고 사용자의 입력을 받으면 이를 변수에 할당합니다.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

input() 함수의 인수는 사용자가 어떤 정보를 입력해야 할지 알리는 프롬프트입니다.

## 명확한 프롬프트 작성하기

input() 함수를 사용할 때는 사용자가 프롬프트만 봐도 어떤 정보를 입력해야 하는지 정확히 알 수 있어야 합니다. 따라 하기 쉽게 만들면 더 좋습니다. 그리고 사용자가 입력한 정보는 정확히 처리해야 합니다.

```python
name = input("\nWhat is your first name? ")
print(f"\nHello, {name}")
```

프롬프트 뒤에는 항상 공백을 넣어서 프롬프트와 사용자 입력이 구분되기 해야 합니다.

```python
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}")
```

프롬프트가 한 행 이상일 경우, 프롬프트를 변수에 저장하고 이 변수를 input() 함수의 인수로 써도 됩니다. 이렇게 하면 프롬프트를 여러 행에 나눠 쓸 수 있고, input() 함수도 깔끔해집니다.

## int()를 사용해서 숫자 입력 받기

input() 함수를 사용하면 파이썬은 사용자가 입력하는 내용을 전부 문자열로 간주합니다.

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

사용자는 숫자 21을 입력했지만, 파이썬에서 age 값을 확인하면 ‘21’이 문자열로 저장되어 있습니다. 이 값이 따옴표로 감싸여 있다는 건 파이썬이 문자열로 해석했다는 뜻입니다.

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
```

하지만 숫자로 사용하려 하면 에러가 일어납니다. 파이썬은 문자열과 정수를 비교할 수 없으므로 에러를 일으킵니다.

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)
>>> age >= 18
True
```

프롬프트에 21을 입력하면 파이썬은 이를 문자열로 해석하지만, int()로 감쌌으므로 숫자로 변환됩니다.

> [궁금증] 사용자가 input을 원하는대로 입력하지 않은 경우? number인데 문자열…
> 

## 나머지 연산자

나머지 연산자(%)는 숫자를 다른 숫자로 나눈 나머지를 반환하는 연산자입니다.

```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

이 연산자는 몫이 몇인지는 알려주지 않습니다. 나머지가 몇인지가 알려줍니다.

숫자가 다른 숫자의 배수라면 나머지는 0이므로, 이런 경우 나머지 연산자는 항상 0을 반환합니다. 이를 통해 숫자가 짝수인지 홀수인지 판단할 수 있습니다.


## while 루프 소개

for 루프는 컬렉션의 요소를 가져와 각 요소마다 코드 블록을 실행합니다. 반면 while 루프는 특정 조건을 통과하는 한 계속 실행됩니다.

## while 루프 사용하기

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

파이썬은 current_number ≤ 5 조건을 통과하는 한 루프를 계속 반복합니다. current_number가 5를 초과하면 루프를 중지하고 프로그램이 끝납니다.

## 사용자가 종료 시점을 선택할 수 있도록 만들기

```python
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)
    print(message)
```

프로그램을 while 루프 안에 넣어서 사용자가 종료하지 않는 한 원하는 만큼 실행하게 만들 수 있습니다. 종료 값을 정의하고, 사용자가 종료 값을 입력하지 않는 한 프로그램을 계속 실행하면 됩니다.

```python
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)
    
    if message != 'quit':
        print(message)
```

이 프로그램은 종료 값인 quit을 마치 메시지처럼 출력한다는 흠이 있습니다. 단순한 if문을 추가해 수정할 수 있습니다.

## 플래그 사용하기

더 복잡한 프로그램에서 프로그램 종료를 위한 조건이 여러 개일 때는 어떻게 해야 할까요?
프로그램을 중지하는 조건이 여러 가지라면, while문 하나 안에서 이 조건들을 모두 테스트하긴 복잡하고 어렵습니다.

여러 가지 조건을 통과해야만 프로그램 실행을 계속하는 경우, 전체 프로그램의 실행 여부를 결정하는 변수를 정의할 수 있습니다. 이런 변수를 플래그라고 하며, 프로그램에 대한 일종의 신호 역할을 합니다.

```python
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
```

프로그램이 시작하자마자 종료되지 않도록 먼저 active 변수를 True로 설정합니다. 이렇게 하면 while 문 안에서 조건을 비교하지 않으므로 while 문이 더 단순해집니다.

## break 문으로 루프 빠져나가기

break 문은 조건 테스트 결과와 관계없이 while 루프를 즉시 종료합니다. break 문은 프로그램의 흐름을 제어합니다. break 문을 써서 코드의 실행 여부를 결정할 수 있으므로 원하는 순간에 원하는 코드를 실행할 수 있습니다.

```python
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

++ break 문은 파이썬의 모든 루프에서 사용할 수 있습니다. 예를 들어 리스트나 딕셔너리에서 사용한 for 루프에도 break를 쓸 수 있습니다.

## 루프에서 continue 문 사용하기

continue 문은 조건 테스트 결과에 따라 루프의 처음으로 돌아갑니다.

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

## 무한 루프 피하기

while 루프를 사용할 때는 무한 루프에 주의해야 합니다.

```python
# 영원히...
x = 1
while x <= 5:
	print(x)
```

종종 프로그래머는 실수로 무한한 while 루프를 만들고, 특히 종료 조건이 모호하면 이런 실수를 하기 더 쉽습니다. 프로그램이 무한 루프에 빠지면 ctrl + C를 누르거나 터미널을 닫으세요.

무한 루프를 피하려면 while 루프를 항상 테스트하고, 원하는 시점에 루프에서 빠져나가는지 확인해야 합니다. 사용자가 특정 값을 입력할 때 프로그램을 종료하고 싶다면 프로그램에 해당 값을 입력해서 테스트하세요. 프로그램이 종료되지 않으면 종료 값을 처리하는 방식을 다시 확인하세요. 최소한 프로그램의 한 부분은 종료 조건을 만들거나 break 문을 포함해야 합니다.


# 리스트, 딕셔너리와 함께 while 루프 사용하기

처리해야 할 정보가 많을 때는 while 루프를 리스트나 딕셔너리와 함께 사용하는 게 좋습니다.

for 루프는 리스트를 효율적으로 순회하지만, for 루프 안에서 리스트를 수정하면 큰 문제가 생길 수 있습니다. 작업 중인 리스트를 수정할 때는 되도록 while 루프를 써야 합니다. 리스트, 딕셔너리를 while 루프와 함께 사용하면 대량의 입력을 취합, 저장, 정리할 수 있습니다.

## 리스트에서 다른 리스트로 요소 옮기기

웹사이트에 등록했지만 아직 확인되지 않은 사용자 리스트(unconfirmed_users)가 있다고 합시다. 이들을 확인한 뒤 확인된 사용자 리스트(confirmed_users)로 이동하는 방법은 뭘까요? while 루프 안에서 확인되지 않은 사용자 리스트에서 사용자를 가져온 다음, 확인이 끝나면 별도의 확인된 사용자 리스트에 추가하는 방법이 있습니다.

```python
# 확인해야 할 사용자가 담긴 리스트,
# 확인된 사용자를 저장할 빈 리스트
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 확인하지 않은 사용자가 남아있으면 계속 진행합니다
# 확인된 사용자는 해당 리스트로 옮깁니다
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 확인된 사용자를 모두 표시합니다
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

확인되지 않은 사용자 리스트가 줄어들수록 확인된 사용자 리스트는 늘어납니다. 확인되지 않은 사용자 리스트가 비어 있으면 루프를 중지하고 확인된 사용자 리스트를 출력합니다.

## 리스트에서 특정 값 모두 제거하기

리스트에서 원하는 값을 모두 제거하려면 어떻게 해야 할까요? 바로 while 루프를 사용하면 됩니다.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

## 사용자가 입력한 값으로 딕셔너리 채우기

while 루프를 통해 필요한 만큼 입력을 받을 수 있습니다. 참가자의 이름을 묻고 응답을 받는 프로그램을 만들어 봅시다. 응답과 사용자를 연결해야 하므로 이 데이터는 딕셔너리에 저장합니다.

```python
responses = {}
# 설문조사를 제어할 플래그입니다
polling_active = True

while polling_active:
    # 참가자 이름과 응답을 받습니다
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장합니다
    responses[name] = response

    # 설문조사에 참가할 사람이 더 있는지 확인합니다
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 설문조사가 끝났으므로 결과를 출력합니다
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```