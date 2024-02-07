---
title: Chapter_11 코드 테스트
author: rain_poem
date: 2024-02-06 20:00:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## pytest 설치하기
```cmd
python -m pip install --user pytest
```
위와 같은 명령어를 통해 써드 파티 패키지를 설치할 수 있습니다.<br>
결과는 아래와 같습니다.<br>
```cmd
Collecting pytest
  Downloading pytest-8.0.0-py3-none-any.whl.metadata (7.8 kB)
Collecting iniconfig (from pytest)
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting packaging (from pytest)
  Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)
Collecting pluggy<2.0,>=1.3.0 (from pytest)
  Downloading pluggy-1.4.0-py3-none-any.whl.metadata (4.3 kB)
Collecting colorama (from pytest)
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading pytest-8.0.0-py3-none-any.whl (334 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 334.0/334.0 kB 10.4 MB/s eta 0:00:00
Downloading pluggy-1.4.0-py3-none-any.whl (20 kB)
Downloading packaging-23.2-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB ? eta 0:00:00
Installing collected packages: pluggy, packaging, iniconfig, colorama, pytest
Successfully installed colorama-0.4.6 iniconfig-2.0.0 packaging-23.2 pluggy-1.4.0 pytest-8.0.0
```
```--user``` 플래그를 통해 **pytest**가 의존하는 다른 패키지도 설치합니다.<br>

## 함수 테스트
```python
# name_function.py
def get_formatted_name(first, last, middle=''):
    # 실제 이름을 깔끔한 형식으로 반환합니다.
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
```

```python
# test_name_function.py
from name_function import get_formatted_name

def test_first_last_name():
    # Janis Joplin 같은 이름에서 동작하는지 테스트
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    # Wolfgan Amadeus Mozart 같은 이름에서 동작하는지 테스트
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```
테스트를 할 파일의 이름은 반드시 **test_** 로 시작해야합니다.<br>
**pytest**는 **test_**로 시작하는 파일을 모두 찾고, 해당 파일에서 발견한 테스트를 실행합니다.<br>
```assert``` **어서션**이라는 조건에 대한 단언을 만들어, 테스트를 확인합니다.<br>
<br>
테스트 수행결과는 아래와 같습니다.<br>
```cmd
python -m pytest
===================================================================================================== test session starts ====================================================================================================== 
platform win32 -- Python 3.12.1, pytest-8.0.0, pluggy-1.4.0
rootdir: D:\Source\03_python\파이썬 크래시 코스\Chapter_11
collected 2 items

test_name_function.py ..                                                                                                                                                                                                  [100%] 

====================================================================================================== 2 passed in 0.02s ======================================================================================================= 
```
테스트를 통해, 실패의 대응을 할 수 있고, 동작 방식을 바꿀 수 있습니다.<br>

## 여러가지 어서션
|어서션|설명|
|---|---|
|assert a == b|두 값이 같다고 단언합니다.|
|assert a != b|두 값이 같지 않다고 단언합니다.|
|assert a|a가 True로 평가된다고 단언합니다.|
|assert not a|a가 False로 평가된다고 단언합니다.|
|assert elemnt in list|element가 list 안에 있다고 단언합니다.|
|assert elemnt not in list|element가 list 안에 없다고 단언합니다.|

## 클래스 테스트
```python
# survey.py
class AnonymousSurvery:
    # 설문조사의 익명 응답 수집

    def __init__(self, question):
        # 질문을 저장하고 응답 저장을 준비합니다.
        self.question   = question
        self.responses  = []

    def show_question(self):
        # 설문을 표시합니다.
        print(self.question)

    def store_response(self, new_response):
        # 응답을 저장합니다.
        self.responses.append(new_response)

    def show_results(self):
        # 수집된 응답을 표시합니다.
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}") 
```

이 클래스를 두가지 방법으로 테스트를 진행해보겠습니다.<br>

```python
from survey import AnonymousSurvery

def test_store_single_response():
    # 단일 응답이 제대로 저장되는지 테스트
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```
예제에서는 **store_response()** 메서드를 통해 단일 응답인 **'English'**가 저장되었는지 확인합니다.<br>

```python
import pytest
from survey import AnonymousSurvery

@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    return language_survey

def test_store_single_response(language_survey):
    # 단일 응답이 제대로 저장되는지 테스트
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```
**pytest**를 임포트하여, ```픽스쳐 기능```을 이용합니다.<br>
```@pytest.fixture``` **데코레이터**를 통해, AnonymousSurvery 객체를 반환하는 함수를 정의합니다.<br>
이후 테스트 함수에서 인수로 데코레이터에 적용한 함수 이름과 동일한 **language_survey**를 매개변수로 받고 있습니다.<br>
이 때 매개변수의 이름과 데코레이터에 적용한 함수이름이 동일하면, 픽스쳐를 실행하고 반환 값을 테스트 함수에 전달합니다.<br>
