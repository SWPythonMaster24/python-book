---
marp: true
theme: uncover
---
# **챕터10 파일과 예외**
---
## **파일 읽기**
```python
from pathlib import Path

path = Path('C:/workspace/python-book/chapter10/정지희/pi_digits.txt')
contents = path.read_text()
print(contents)
```
###### 파일작업을 위해서는 경로를 알아야한다. <br>경로는 시스템에 있는 파일 또는 폴더의 정확한 위치이다.<br>경로는 현재 실행 중인 프로그램 파일 기준으로경로를 지정하는 상대 경로가 있으며, 실행중인 파일 위치와 관계없이 지정하는 절대 경로가 있다.<br>
###### 파이썬은 파일과 폴더 작업을 더 쉽게 만드는 pathlib 모듈을 제공하는데 이런 기능을 제공하는 모듈을 라이브러리라고 부른다.
---
## **한 행씩 다루기**
```python
from pathlib import Path

path = Path('C:/workspace/python-book/chapter10/정지희/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
```
###### splitlines() 메서드를 사용하면 긴 문자열을 행 리스트로 변환한다.
```python
3.1415926535
  8979323846
  2643383279
```
---
## **파일 저장**
```python
from pathlib import Path

path = Path('C:/workspace/python-book/chapter10/정지희/programming.txt')
path.write_text('I love programming')
```
###### 경로를 지정한 다음 write_text() 메서드를 통해 파일에 작성이 가능하다. 지정한 경로에 해당 파일이 없으면 생성이 된다.
---
## **예외 처리**
###### 파이썬은 예외라는 특별 객체를 사용해 <br>프로그램 실행 중 일어난 에러를 관리한다.<br>예외를 처리하지 못하면 프로그램이 중단되고, 일어난 예외는 트레이스백에 포함된다. 예외는 try-except문으로 처리한다.

```python
while True:
    ...
    if name == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        pass
    else:
        print(answer)
```
---
## **리팩터링**
###### 특정 목적을 가진 코드를 함수로 분리해 프로그램을 개선할 수 있는데 이를 리팩터링이라고 한다 <br>리팩터링은 코드를 더 깔끔하고 이해하기 쉽게 만들며, 확장하기에 편하다