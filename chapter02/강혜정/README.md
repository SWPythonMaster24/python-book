# Chapter 2. 변수와 단순한 데이터 타입

# 1. hello_world.py를 실행할 때 일어나는 일
1. 에디터가 파이썬 인터프리터를 실행함
2. 파이썬 인터프리터가 프로그램을 읽고 프로그램의 각 단어가 어떤 의미인지 파악함
```python
print("Hello Python World!")
```


# 2. 변수
```python
message = "Hello Python World!"
print(message)

# 출력:
# Hello Python World!
```

## 변수 이름 짓기 및 사용하기
- 문자, 숫자, 밑줄만 사용 가능.
- 변수 이름 맨 앞에는 문자나 밑줄만 쓸 수 있고 숫자는 쓸 수 없음.
- 변수 이름에는 공백 금지.
- 파이썬 키워드나 내장 함수 이름을 변수 이름으로 사용 금지.
- 변수 이름은 짧으면서 의미가 분명해야 함.

## 에러가 발생했을 때
- traceback을 통해 에러 파악을 쉽게 해줌.
    - 트레이스백이란 인터프리터가 코드를 싱행하다가 어디서 문제가 생겼는지 기록한 보고서를 의미함.
```
Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 2, in <module>
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```


# 3. 문자열
- 문자열은 연속적인 문자. 파이썬에서 따옴표로 둘러썬 건 모두 문자열을 의미.
```python
name = "ada lovelace"

# 각 단어 첫 글자를 대문자로 변경 - title()
print(name.title())

# 대문자로 변경 - upper()
print(name.upper())

# 소문자로 변경 - lower()
print(name.lower())
```

- 문자열 안에서 변수 사용하기
    - 따옴표 바로 앞에 `f`를 쓰고(format) 변수를 사용할 때는 `{}`로 묶음.<br>
    이것을 f-문자열(f-strings)이라고 함. 
```python
first_name = "hyejeong"
last_name = "kang"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# 출력:
# Hello, Hyejeong Kang
```
- 탭이나 줄바꿈으로 문자열에 공백 추가하기
```python
# 탭 추가: \t
# 줄바꿈: \n

print('Languages:\n\tPython\n\tJavascript')
# 출력:
# Languages:
# 	Python
# 	Javascript
```
- 공백 없애기
```python
name = " I    learn  python    ! "

# 문자열 오른쪽에 있는 공백 제거 - rstrip()
print(name.rstrip()) # ' I    learn  python    !'

# 문자열 왼쪽 있는 공백 제거 - lstrip()
print(name.lstrip()) # 'I    learn  python    ! '

# 양쪽에 있는 모든 공백 제거 - strip()
print(name.strip()) # 'I    learn  python    !'
```
- 접두어 없애기
```python
# string.py
url = "https://www.naver.com"
print(url.removeprefix("https://"))
print(url.removeprefix("naver"))

# 출력:
# www.naver.com
```


# 4. 숫자
- 정수
```python
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print((2 + 3) * 4) # 필요한 경우에는 괄호를 사용.
print(2**2) # 거듭제곱
```

- 정수와 부동 소수점 숫자
    - 나누기를 하게 되면 분모, 분자가 모두 정수여도 결과는*항상 부동 소수점 숫자로 나옴.
```python
print(4 / 2)
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2) 

# 출력:
# 2.0
# 3.0 
# 6.0
# 9.0
```
- 숫자의 밑줄
    - 큰 숫자를 사용할 때 밑줄을 써서 읽기 쉽게 만들 수 있음.
```python
price = 14_000_000_000
```
- 다중 할당
```python
x, y, z = 1, 2, 3 # (x=1, y=2, z=3)
```
- 상수
    - 변하지 않는 숫자. 파이썬에서 공식적으로 지원하지는 않음.
    - 모두 대문자로 작성함.


# 5. 주석
- `#` 로 사용.
- 코드가 어떤 일을 하는지, 어떻게 하는지 설명.
- 협업을 위해서 반드시 좋은 주석을 다는 습관을 만드는 게 좋음.
- 의미가 명확하게 주석을 다는게 좋음.
- 처음에 조금 더 자세하게 작성했다가 나중에 불필요한 주석을 제거하는 편이 훨씬 쉽고 좋음.
```python
# 주석입니다.
```


# 6. 파이썬의 선
- Explicit is better than implicit. 명확함이 함축된 것보다 낫다.
- Simple is better than complex. 단순함이 복잡한 것보다 낫다.
- Readability counts. 가독성은 중요하다.
- Special cases aren't special enough to break the rules. 규칙을 깨야할 정도로 특별한 경우란 없다. Although practicality beats purity. 비록 실용성이 이상을 능가한다 하더라도.
- Errors should never pass silently. 오류는 결코 조용히 지나가지 않는다. Unless explicitly silenced. 알고도 침묵하지 않는 한.
- If the implementation is hard to explain, it's a bad idea. 설명하기 어려운 구현이라면 좋은 아이디어가 아니다.


# 그 외
- 파이썬 타입 어노테이션
    - 파이썬 3.5 버전부터 지원.
    - 적극적인 타입 체크가 아니라, 타입에 대한 힌트를 알려주는 정도임.
```python
num: int = 1

def add(a: int, b: int) -> int: 
    return a+b
```