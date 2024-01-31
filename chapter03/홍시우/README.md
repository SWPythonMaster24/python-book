# 3. 리스트 소개
리스트를 설명합니다.

## 리스트의 개념
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

**리스트(list)** 는 일종의 요소들을 순서에 따라 모은 컬렉션입니다.<br>
문자, 정수 등 여러 요소들을 사용할 수 있다.<br>
리스트는 **대괄호 []** 로 표현하며, 요소는 **콤마 ,** 로 구분합니다.<br>

## 리스트 요소 접근하기
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```
원하는 요소에 **인덱스**로 접근할 수 있습니다.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```
마지막 요소부터 접근하는 경우에는, **마이너스 인덱스**를 쓴다.

```python
bicycles    = ['trek', 'cannondale', 'redline', 'specialized']
message     = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

f-문자열과 리스트 요소를 함께 사용할 수 있습니다.

## 요소 수정, 추가, 제거
리스트는 동적인 컬렉션이기 때문에, 프로그램 안에서 리스트에 요소를 추가하거나 제거할 수 있다.

## 리스트 요소 수정하기
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

## 리스트 요소 추가하기
```python
motorcycles = ['yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
motorcycles.insert(0, 'honda')

print(motorcycles)
```

**append()** 메서드는 마지막 인덱스에 추가합니다.<br>
**insert()** 메서드는 원하는 위치에 요소를 삽입합니다.<br>

## 리스트 요소 제거하기
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.pop(0)
motorcycles.remove('yamaha')
```

**del문**으로 인덱스를 통해 리스트 요소를 제거합니다.<br>
**pop()** 메서드를 사용하여 마지막 인덱스의 요소를 제거함과 동시에 반환합니다.<br>
또한, **pop()** 메서드는 원하는 인덱스의 요소를 제거할 수 있습니다.<br>
**remove()** 메서드를 통해 요소의 값으로 삭제를 할 수 있습니다.<br>

## 리스트 정리하기
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

['audi', 'bmw', 'subaru', 'toyota']
['toyota', 'subaru', 'bmw', 'audi']
```

**sort()** 메서드는 리스트의 순서를 영구히 변경합니다.<br>
메서드에 **reverse=True** 인자를 넘기면 역순으로 정렬합니다.<br>
**sorted()** 함수는 반환되는 값만 순서를 변경합니다.<br>

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```
**reverse()** 메서드를 통해 리스트를 역순으로 바꿀 수 있습니다.

## 리스트의 길이 확인하기
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
```
**len()** 함수는 리스트의 길이를 반환합니다.<br>
인덱스와 달리 길이이기 때문에 1부터 시작합니다.<br>