---
marp: true
theme: uncover
---
# **챕터6 딕셔너리**
---
## **딕셔너리**
##### 딕셔너리(dictionary)는 <br>정보를 연결해 저장하는 역할을 하며,<br> 키-값 상 컬렉션으로 구성되어있습니다.
```python
# key-value
alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
```
---
## **딕셔너리 사용**
```python
alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# 값에 접근
print({alien_0['color']}) # green
# 쌍 추가하기
alien_0['x_position'] = 0
# 값 수정하기
alien_0['color'] = 'yellow'
# 쌍 제거하기
del alien_0['points']
# get()으로 값 접근(요청하는 키, 키가 존재하지 않을 경우 반환 값)
points_value = alien_0.get('points', 'No point value assigned.')
```
---
## **딕셔너리 순회**
```python
for k, v in dictionary.items()
```
items() 메서드를 통해 키-값 쌍을 반환 할 수 있습니다.
```python
for k, v in dictionary.items()
```
keys() 메서드를 통해 키를 반환 할 수 있습니다.<br>sorted를 통해 정렬된 키 사본을 가져올 수 있습니다.
```python
for k, v in dictionary.items()
```
values() 메서드를 통해 값을 반환 할 수 있습니다.<br>set()을 통해 중복을 제거할 수 있습니다.

---
## **중첩 딕셔너리,<br> 리스트를 담은 딕셔너리**
> 딕셔너리 안에 딕셔너리 혹은 리스트, <br>리스트 안에 딕셔너리 등 중첩도 가능합니다.
