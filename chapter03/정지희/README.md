---
marp: true
theme: uncover
---
# **챕터 3 리스트 소개**
---
## **리스트의 개념**

`bicycles = ['trek','redline','cannodale']
`
###### 리스트는 요소들을 순서에 따라 모은 컬렉션입니다.<br>파이썬 리스트는 대괄호`[]`로 표현하며, 각 요소는 콤마로 구분합니다.
---
## **리스트 접근**

```python
bicycles = ['trek','redline','cannodale']
print(bicycles[0])

trek
```
###### 리스트는 순서가 있어 위치를 통해 접근이 가능합니다. <br>요소에 접근 시 `[]` 안에 위치를 씁니다. 위치(인덱스)는 0부터 시작합니다.<br>(`len()`을 통해 길이를 확인합니다. 길이는 1에서 시작됩니다.)

---
## **리스트 수정, 추가, 제거**
###### 리스트는 동적인 컬렉션입니다.<br> 즉, 리스트에 요소를 수정, 추가, 삭제가 가능하는 의미입니다.
```python
# 수정
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
# 추가
motorcycles.append('honda')
motorcycles.insert(2, 'triumph')
# 삭제
del motorcycles[1]
motorcycles.pop()
motorcycles.remove('yamaha')
```

---
## **리스트 정리**
##### 영구히 정리하는 sort()
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# reverse 역순
cars.sort(reverse=1)
```
##### 임시로 정리하는 sort()
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here is the sorted list:\n{sorted(cars)}")
# reverse 역순
print(f"Here is the reserve sorted list:\n{sorted(cars, reverse=1)}")
```

