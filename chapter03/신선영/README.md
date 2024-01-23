# 3. 리스트 소개

# 1. 리스트의 개념

- 요소들을 순서에 따라 모은 컬렉션
- 뭐든 들어갈 수 있음 (문자열, 숫자 …)
- 복수형으로 네이밍함 (ex. `letters`, `digits`)
- 대괄호(`[]`)로 표현하며, 콤마(`,`)로 구분함

```python
# list.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

위 메서드를 실행하면 나오는 결과는 아래와 같다.

```python
['trek', 'cannondale', 'redline', 'specialized'] # 대괄호 포함된 형태로 출력
```

## 요소에 접근하기

위치를 통해 접근할 수 있다. 예를 들어 `bicycles`에서 trek을 가져오고 싶다면 `[0]`으로 가져오면 된다.

```python
# list.py
print(bicycles[0]) # trek
print(bicycles[0].title()) # Trek
```

당연한 말이지만 컴퓨터 메모리 주소는 0부터 시작하기 때문에 첫 번째 요소는 1이 아니라 0이다.

만약 마지막 요소를 가져오고 싶다면 `[-1]` 으로 가져오면 된다. 뒤에서 두번째는 `[-2]`

```python
# list.py
print(bicycles[-1]) # specialized
print(bicycles[-2]) # redline
print(f"My first bicycle was a {bicycles[0].title()}.") # My first bicycle was a Trek.
```

📌 **연습 문제!**

```python
# quiz.py
# 3-1 이름
friends = ['김민수', '김철수', '김영희', '김영수']
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3]) # 또는 print(friends[-1])

# 3-2 인사말
print(f"{friends[0]}님 안녕하세요.")
print(f"{friends[1]}님 안녕하세요.")
print(f"{friends[2]}님 안녕하세요.")
print(f"{friends[3]}님 안녕하세요.")

# 3-3 나만의 리스트
transportations = ['car', 'bus', 'train', 'airplane']
print(f"I would like to own a {transportations[2]}.")
```

# 2. 요소 수정, 추가, 제거

리스트는 동적인 컬렉션이기 때문에 리스트에서 요소를 **추가**하거나 **제거**할 수 있다.

```python
# list.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

위 메서드를 실행하면 나오는 결과는 아래와 같다.

```python
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki'] # 요소가 바뀜
```

**이 외에도 요소를 변경하는 메서드**

`append()` : 마지막에 특정 요소를 추가

`insert()` : 원하는 위치에 요소를 추가

`del` : 특정 위치의 요소를 삭제

`pop()` : 맨 마지막 위치의 요소를 삭제. 특정 위치의 요소를 삭제할 수도 있음

`remove()` : 내용에 해당하는 요소를 삭제

```python
# list.py
friends = ['김민수', '김철수', '홍길동']
friends.append('김영희')
print(friends)

friends.insert(1, '김영수')
print(friends)

del friends[2]
print(friends)

friends.pop()
print(friends)

friends.pop(0)
print(friends)

friends.remove('김영수')
print(friends)

print(f"마지막으로 남은 친구는 {friends[0]}입니다.")
```

위 메서드를 실행하면 나오는 결과는 아래와 같다.

```python
['김민수', '김철수', '홍길동', '김영희']
['김민수', '김영수', '김철수', '홍길동', '김영희']
['김민수', '김영수', '홍길동', '김영희']
['김민수', '김영수', '홍길동']
['김영수', '홍길동']
['홍길동']
마지막으로 남은 친구는 홍길동입니다.
```

📌 위 예제로 연습문제를 커버했으니 연습문제는 별도로 진행하지 않고 skip

# 3. 리스트 정리하기

**리스트를 정리하는 메서드**

`sort()` : 알파벳 순으로 **영구히 정렬**

`sort(reverse=True)` : 알파벳 역순으로 **영구히 정렬**

`sorted()` : 리스트의 원래 순서를 유지하며 **임시로** 알파벳 순으로 **정렬**

`sorted(reverse=True)` : 리스트의 원래 순서를 유지하며 알파벳 역순으로 **임시로 정렬**

`reverse()` : 역순으로 정렬 (알파벳 순이 아니라 그냥 배열 자체의 위치를 역순으로 바꾸는 것!)

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars.reverse()
print(cars)
print(len(cars))
```

위 메서드를 실행하면 나오는 결과는 아래와 같다.

```python
['audi', 'bmw', 'subaru', 'toyota']
['toyota', 'subaru', 'bmw', 'audi']
['audi', 'bmw', 'subaru', 'toyota']
['toyota', 'subaru', 'bmw', 'audi'] # 임시로 정렬했었기 때문에 다시 돌아옴
['audi', 'bmw', 'subaru', 'toyota']
4
```

📌 위 예제로 연습문제를 커버했으니 연습문제는 별도로 진행하지 않고 skip

# 4. 인덱스 에러 피하기

마지막 요소에 접근할 때는 -1을 쓰기

원인을 모르겠으면 리스트 전체나 길이를 출력해보기