---
title: Chapter_09 클래스
author: rain_poem
date: 2024-02-05 22:00:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## 파일 읽기
```
3.1415926535
  8979323846
  2643383279
```

```python
# file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
```

파이썬에서 **'pathlib'** 모듈을 사용하여, 특정 경로 내의 파일을 읽을 수 있습니다.<br>
pi_digits.txt를 가르키는 **Path 객체**를 생성하여, **read_text()** 메서드를 통해, 파일을 읽을 수 있습니다.<br>


```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
```

**splitlines()** 메서드를 통해 파일을 행 단위로 읽을 수 있습니다.<br>

## 파일에 저장하기
```python
from pathlib import Path

contents    = "I love programming.\n"
contents   += "I love creating new games.\n"
contents   += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```
**write_text()** 메서드를 통해, 파일이 없다면 파일을 생성하여, 파일에 데이터를 씁니다.<br>
변수를 통해 파일에 여러 행에 파일을 쓸 수 있습니다.<br>

## 예외 처리
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else
    print("End divide")
```
**try-except 문**을 통해, 예외가 발생할 수 있는 코드에서 예외가 발생하면, **except** 블록이 실행됩니다.<br>
예외가 발생하지 않은 경우 **else**블럭(생략가능)의 코드가 실행됩니다.<br>
혹은 예외가 발생했을때 **pass**를 통해, 아무 일 없이 블럭을 건너 뛸 수 있습니다.<br>

## 데이터 저장하기
```python
from pathlib import Path
import json

numbers = [2, 3, 5, 6, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
```
json 모듈을 임포트하여, JSON 형식의 파일을 작성하는 예제입니다.<br>
```dumps()``` 메서드를 통해 리스트를 JSON 문자열로 변환하여 파일에 작성하였습니다.<br>
<br>
결과는 아래와 같습니다
```
[2, 3, 5, 6, 11, 13]
```

반대로 JSON 형식의 파일을 읽을 수 있습니다.<br>
```python
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
```
```load()``` 메서드를 통해, 파일로부터 JSON 데이터를 읽어올 수 있습니다.<br>