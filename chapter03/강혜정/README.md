# Chapter 3. 리스트 소개

## 1. 리스트의 개념
- 일종의 요소들을 순서에 따라 모은 컬렉션.
- 원하는 요소는 뭐든 리스트에 저장 가능하고, 요소 사이에 어떤 관계가 있을 필요도 없음.
- 보통 둘 이상의 요소가 포함되므로 복수형으로 짓는 걸 추천.
- 파이썬 리스트는 대괄호([])로 표현하며, 각 요소는 콤마로 구분.
- 파이썬에서 리스트 출력 시 대괄호가 포함된 형태로 출력.
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 출력:
# ['trek', 'cannondale', 'redline', 'specialized']
```

### 리스트 요소에 접근하기
- 리스트는 순서가 있으므로 원하는 요소의 **인덱스**를 통해 접근 가능.
- 리스트 요소에 접근할 때는 리스트 이름 뒤에 대괄호를 쓰고, 그 안에 인덱스를 쓰기.
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# 출력:
# trek
```

### 인덱스는 0에서 시작합니다
- 파이썬에서 리스트의 첫 번째 요소의 인덱스는 1이 아니라 0임.
- 두 번째 요소의 인덱스는 1으로, 원하는 위치에서 1을 뺀 결과가 인덱스임.
- 파이썬에는 인덱스 -1을 요청하면 리스트의 마지막 요소를 반환함.
    - 해당 문법을 확장해 인덱스 -2는 리스트의 마지막에서 두 번째 요소를, 인덱스 -3은 마지막에서 세 번째 요소를 반환하는 식임.
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# 출력:
# cannondale
# specialized

print(bicycles[-1])
# 출력:
# specialized
```


## 2. 요소 수정, 추가, 제거
- 리스트는 동적인 컬렉션이기 때문에 요소를 추가하거나 제거 가능

### 리스트 요소 수정하기
- 요소를 변경할 때는 리스트 이름 다음에 대괄호와 인덱스를 쓰고, 새 값을 할당하면 끝!
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 출력:
# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']
```

### 리스트에 요소 추가하기
- append()로 리스트 마지막에 요소 추가하기
    - 리스트의 다른 요소에는 영향을 주지 않고 마지막에 값을 추가함.
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# 출력:
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducati']
```
    
- insert()로 원하는 위치에 요소 삽입하기
    - 리스트 원하는 위치에 요소 삽입 가능.
    - insert()를 사용하면 다른 값들은 모두 오른쪽으로 하나씩 이동.
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 출력:
# ['ducati', 'honda', 'yamaha', 'suzuki']
```

### 리스트에서 요소 제거하기
- del 문으로 요소 제거하기
    - 제거할 요소의 인덱스를 알고 있는 경우 활용 가능.
    - del 문을 사용하면 리스트에서 제거된 값에 더는 접근할 수 없음.
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# 출력:
# ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']
```
    
- pop()으로 요소 제거하기
    - 리스트의 마지막 요소를 제거하는 동시에 해당 요소를 반환함.
    - pop 함수 인수에 인덱스를 넘기면 원하는 위치에서 요소를 제거 가능.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles1 = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles1)

popped_motorcycles2 = motorcycles.pop(0)
print(popped_motorcycles2)

# 출력:
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha']
# suzuki
# honda
```

- 값을 기준으로 요소 제거하기 remove() 메서드
    - 제거할 요소의 값으로 위치를 파악해 해당 요소를 제거.
    - 제거한 값을 반환함.
    - 지정한 값과 일치하는 첫 번째 요소만 제거함.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# 출력:
# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']
```


## 3. 리스트 정리하기

### 리스트를 영구히 정렬하는 sort() 메서드
- 리스트이 순서를 영구히 변경함.
- sort() 메서드에 reverse=True 인수를 넘기면 역순으로 정렬됨.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 출력:
# ['bmw', 'audi', 'toyota', 'subaru']
# ['toyota', 'subaru', 'bmw', 'audi']
```

### 임시로 정렬하는 sorted() 함수
- 리스트를 원하는 순서로 표시하지만, 실제 순서는 바뀌지 않음.
- sorted() 역시 reverse=True 인수를 넘기면 역순으로 정렬됨.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))

# 출력:
# ['bmw', 'audi', 'toyota', 'subaru']
# ['toyota', 'subaru', 'bmw', 'audi']
# ['bmw', 'audi', 'toyota', 'subaru']
# ['toyota', 'subaru', 'bmw', 'audi']
```

### 역순으로 리스트 출력하기 reverse() 함수
- 리스트의 현재 순서를 반대로 바꾸는 함수.
- 리스트의 순서를 역구히 바꾸지만, 다시 호출하면 원래 순서로 돌아갈 수 있음.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# 출력:
# ['bmw', 'audi', 'toyota', 'subaru']
# ['subaru', 'toyota', 'audi', 'bmw']
```

### 리스트의 길이 확인하기
- len() 함수는 리스트의 길이를 반환함.
- 리스트의 길이는 인덱스와 달리 1에서 시작함.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# 출력:
# 4
```


## 4. 인덱스 에러 피하기
- 존재하지 않는 인덱스에 접근하려고 할 때 발생.
- 만약 빈 리스트인 상태에서 인덱스 -1을 요청하면 `IndexError: list index out of range` 에러 발생
```shell
list = []
print(list[-1])

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 2, in <module>
    list[-1]
    ~~~~^^^^
IndexError: list index out of range

[Execution complete with exit code 1]
```