# Chapter 11. 코드 테스트
테스트를 작성하면 더 많은 사람이 우리 프로그램을 사용해도 코드가 에러 없이 정확히 동작한다는 확신을 얻을 수 있다. 
새 코드를 추가할 때도 테스트를 거쳐서 이번에 바꾼 내용이 프로그램의 기존 동작 방식을 해치지는 않았는지 확인할 수 있다.

프로그래머는 항상 코드를 테스트해서 사용자보다 먼저 문제를 발견해야 한다! (별표x100만개)


## pip로 pytest 설치하기
**써드 파티 패키지** 란 파이썬 코어에 포함되지 않는 라이브러리를 의미한다.

### pip 업데이트하기
파이썬에는 써드 파티 패키지를 설치하는 pip라는 도구가 포함되어 있다.

pip는 외부 패키지를 설치하므로 잠재적인 보안 문제를 해결하기 위해 자주 업데이트 된다.
```shell
# pip 업데이트
$ python -m pip install --upgrade pip
```
- `python -m pip`: pip 모듈 실행하라는 의미
    - Q. '-m' 옵션을 추가하는 이유는??
        - '-m' 옵션은 파이썬 모듈을 살행하는 데 사용된다. 이를 사용하여 Python 모듈을 명령줄에서 직접 실행할 수 있다. '-m'을 사용하지 않고 모듈을 실행하려고 시도하면 시스템은 해당 모듈을 찾지 못한다는 오류가 발생한다.
- `install --upgrade`: 이미 설치된 패키지를 업데이트 하라는 뜻
```shell
# 써드 파티 패키지 업데이트
$ python -m pip install --upgrade package_name
```
### pytest 설치하기
```shell
$ python -m pip install --user pytest
```
- '--user' 옵션을 사용하면 사용자의 홈 디렉토리(~/.local) 내에 설치된다.
- pytest가 의존하는 다른 패키지도 같이 설치된다.


## 함수 테스트
이름과 성을 받아 실제 이름을 반환하는 간단한 함수이다.
```python
# 파일: name_function.py
def get_formatted_name(first, last, middle=''):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```
```python
# 파일: names.py
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")
```
코드가 변경될 때마다 파일을 실행하여 테스트할 수도 있지만, pytest를 통해 함수의 반환 값을 효율적으로 자동화 할 수 있다.

### 단위 테스트와 테스트 케이스
- **단위 테스트** 는 함수의 동작 방식 하나를 확인
- **테스트 케이스** 는 함수가 처리해야 하는 상황 전체 중에서 테스트가 완료된 단위 테스트를 모은 것
- **테스트가 전체 커버리지를 달성했다** 는 함수를 사용하면서 일어날 수 있는 모든 상황이 단위 테스트로 통과했다는 의미.

### 통과하는 테스트
```python
from name_function import get_formatted_name

def test_first_last_name():
    """Jamis Joplin 같은 이름에서 동작하는지 테스트"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Wolfgang Amadeus Mozart 같은 이름에서 동작하는지 테스트"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```
- ptest는 `test_`로 시작하는 모든 파일에서 발견한 테스트를 모두 실행한다.
- 테스트 함수는 `test_`로 시작해야 테스트로 인식한다.
- `assert`는 조건에 대한 단언이다.

### 테스트 실행하기
```shell
$ pytest
========================= test session starts ==========================
platform darwin -- Python 3.9.7, pytest-4.6.2, py-1.10.0, pluggy-0.13.1
rootdir: /python-book/chapter11/강혜정/examples
plugins: anyio-2.2.0
collected 2 items                                                      

test_name_function.py ..                                         [100%]

======================= 2 passed in 0.01 seconds =======================
```
### 실패하는 테스트
```shell
$ ptest
========================= test session starts =========================
platform darwin -- Python 3.9.7, pytest-4.6.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/ovokhj/individual/python-book/chapter11/강혜정/examples
plugins: anyio-2.2.0
collected 2 items                                                     

test_name_function.py F.                                        [100%]

============================== FAILURES ===============================
________________________ test_first_last_name _________________________

    def test_first_last_name():
        """Jamis Joplin 같은 이름에서 동작하는지 테스트"""
        formatted_name = get_formatted_name('janis', 'joplins')
>       assert formatted_name == 'Janis Joplin'
E       AssertionError: assert 'Janis Joplins' == 'Janis Joplin'
E         - Janis Joplins
E         ?             -
E         + Janis Joplin

test_name_function.py:6: AssertionError
================= 1 failed, 1 passed in 0.05 seconds ==================
```


## 클래스 테스트
### 여러 가지 어서션
| 어서션 | 설명 |
| ---- | --- |
| assert a == b | 두 값이 같다고 단언 |
| assert a != b | 두 같이 같지 않다고 단언 |
| assert a | a가 True로 평가된다고 단언 |
| assert not a | a가 False로 평가된다고 단언 |
| assert element in list | element가 list 안에 있다고 단언 |
| assert element not in list | element가 list 안에 없다고 단언 |

### 테스트할 클래스
익명 설문조사에 관한 클래스와 그 클래스(AnonymousSurvey)를 사용하는 프로그램이 있다.

```python
# 파일: survey.py
class AnonymousSurvey:
    """설문조사의 익명 응답 수집"""

    def __init__(self, question):
        """질문을 저장하고 응답 저장을 준비합니다"""
        self.question = question
        self.responses = []

    def show_question(self):
        """설문을 표시합니다"""
        print(self.question)

    def store_response(self, new_response):
        """응답을 저장합니다"""
        self.responses.append(new_response)

    def show_results(self):
        """수집된 응답을 표시합니다"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```
```python
# 파일: language_survey.py
from survey import AnonymousSurvey

# 설문의 정의하고 설문조사를 만듭니다
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# 설문을 표시하고 응답을 저장합니다
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# 설문조사 결과를 표시합니다
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
```

클래스와 모듈을 더 개선하다 보면, 현재 동작을 망칠 위험이 있다. 그런 일이 없게 하려면 클래스 테스트를 작성해야 한다.

### AnonymousSurvey 클래스 테스트
```python
# 파일: test_survey.py
from survey import AnonymousSurvey

def test_store_single_response():
    """단일 응답이 제대로 저장되는지 테스트"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_store_three_responses():
    """세 가지 개별 응답이 제대로 저장되는지 테스트"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

인수 없이 `pytest` 명령을 실행하면 기본적으로 현재 폴더의 테스트를 모두 실핸한다.

파일 하나의 테스트에 집중하려면 테스트할 파일 이름을 인수로 쓰면 된다!

```shell
$ pytest test_survey.py
================ test session starts =================
platform darwin -- Python 3.9.7, pytest-4.6.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/ovokhj/individual/python-book/chapter11/강혜정/examples
plugins: anyio-2.2.0
collected 2 items                                    

test_survey.py ..                              [100%]

============== 2 passed in 0.01 seconds ==============
```

### 픽스처 기능 사용하기
픽스처는 테스트 환경을 만드는 데 도움이 되는 기능으로, 대개는 둘 이상의 테스트에서 리소스 하나를 공유하는 걸 말한다.

@pytest.fixture 데코레이터를 사용해 함수를 정의하면 pytest에서 픽스처를 생성한다.

*데코레이터* 는 함수 정의 바로 앞에 있는 지시자를 말하며, 함수를 실행하기 전에 지시자를 적용해 함수의 행동 방식을 수정한다.

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """모든 테스트에서 사용할 수 있는 설문조사 인스턴스"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """단일 응답이 제대로 저장되는지 테스트"""
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_store_three_responses(language_survey):
    """세 가지 개별 응답이 제대로 저장되는지 테스트"""
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

새로운 함수 language_survey()에 @pytest.fixture 데코레이터를 적용하고, 테스트 함수는 모두 language_survey 매개변수를 받도록 수정했다. <u>테스트 함수의 매개변수 이름과 @pytest.fixture 데코레이터가 적용된 함수 이름이 일치하면 자동으로 픽스처를 실행하고 반환 값을 테스트 함수에 전달한다.</u>

픽스처를 당장 활용해야 하는 것은 아니며, 충분히 연습하고 중복이 슬슬 거슬리게 느껴질 때 사용하면 된다.


## 번외
1. 테스트 작성 잘하는 법?
2. 나의 경우 만들어진 __pycache__와 .pytest_cache는 무엇일지?