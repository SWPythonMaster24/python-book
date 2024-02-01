---
marp: true
theme: uncover
---
# **챕터 4 리스트 다루기**
---
## **리스트의 순회(루프)**
##### 리스트의 모든 요소에 같은 행동을 반복할 때는 <br>for 루프를 사용합니다.
```python
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone.")

Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
Thank you, everyone.
```
---
## **들여쓰기 에러 피하기**
##### 파이썬은 들여쓰기를 사용해 프로그램의 <br>각 부분을 구분합니다. 앞의 리스트도 들여 썼던 부분은 <br>for 루프의 일부로 인식됩니다. 밑의 항목을 조심하시면 에러를 피할 수 있습니다.

1. 들여쓰기 잊기
2. 일부 행 들여쓰지 않기
3. 불필요한 들여쓰기
4. 루프 다음 불필요한 들여쓰기
5. 콜론 잊기

---
## **숫자 리스트**
##### `range()` 함수 이용 시 일련의 숫자를 쉽게 생성 가능합니다.
```python
# 함수 사용
for num in range(1, 5):
    print(num)

# 리스트 생성
num = list(range(1, 5)):
print(num)

# 건너뛰기
num = list(range(2, 11, 2)):
print(num)
```
---
## **리스트 일부분 다루기**
##### 리스트의 일부분만 다루는 부분집합을 슬라이스라 부릅니다.
```python
# 슬라이스 사용
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f"리스트의 첫 세 항목은: {my_foods[:3]}")
# 슬라이스 순회
for food in my_foods:
    print(food)
# 리스트 복사
friend_foods = my_foods[:]
# 얕은 복사
friend_foods = my_foods
friend_foods.append('ice cream')
print(f"My favorite foods are: \n{my_foods}")
print(f"\nMy friend's favorite foods are: \n{friend_foods}")
```
---

## **튜플**
##### 변하지 않는 불변의 리스트를 튜플이라 합니다.
```python
dimensions = (200, 5)
```
###### 튜플은 괄호를 사용한다는 점을 제외하면 리스트와 똑같습니다.<br>변경하는 건 불가능하지만, 새 값을 할당하는 것은 가능합니다.
```python
dimensions = (200, 5)

dimensions = (400, 100)
```
