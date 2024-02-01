# 리스트 다루기
루프를 통해 리스트의 길이에 관계없이 리스트 전체를 순회하는 방법을 배운다.

## 전체 리스트 순회하기

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")

print("end loop")
```

**for 루프**<br>
1. **magicians** 리스트의 첫번째 값을 읽고 이를 **magician** 변수에 할당
2. **for 루프** 내에 있는 코드를 실행합니다.
3. 1부터 반복 (리스트의 끝까지)

**루프 블록**
1. **for in** 다음에 들여쓴 행은 모두 루프 블록으로 간주하여 실행합니다.

## 숫자 리스트 만들기
```python
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6)) 
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for vaule in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michel', 'florence', 'eli']
print(players[0:3])

for player in players[:3]
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
firend_foods = my_foods[:]

print(my_foods)
print(friend_foods)
```

**range()** 함수를 사용하면 일련의 숫자를 만들 수 있습니다. (단, 2 번째 인수는 포함하지 않음)<br>
**range()** 와 **list()** 함수를 조합하여, 숫자 리스트를 만들 수 있습니다.<br>
**range()** 함수에 3번째 인수를 넣어주면, 1 번째 인수부터 시작하고, 그 값에 3번째 인수를 더합니다.<br>
**min()** 함수는 숫자 리스트의 최소 값을 구합니다.<br>
**max()** 함수는 숫자 리스트의 최대 값을 구합니다.<br>
**sum()** 함수는 숫자 리스트의 합계를 구합니다.<br>
**슬라이스**는 인덱스의 범위를 지정할 수 있습니다.<br>
1. [0:3]   : 0부터 2까지<br>
2. [:4]    : 0부터 3까지<br>
3. [2:]    : 3부터 마지막까지<br>
4. **for 루프** 에서도 슬라이스로 순회할 수 있습니다.<br>

**[:]** 문법으로 리스트를 복사 할 수 있습니다.

## 튜플
```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
```
**튜플**은 정의할 때 대괄호 대신 괄호를 사용합니다. (그 외에는 리스트와 같음)<br>
**튜플**은 불변 객체이기 때문에 값을 할당할 수 없습니다.<br>
**튜플**을 가르키는 변수에 튜플을 재정의하여 값을 할당할 수 있습니다.<br>





