# 10. 파일과 예외

# 1. 파일 읽기

파일을 메모리로 읽고 → 파일 콘텐츠를 조작한다.

`pi.digits.txt` 파일을 저장하고 아래와 같이 코드를 작성한다.

```python
# file_reader.py
from pathlib import Path

# Path to the file
path = Path("pi.digits.txt")
content = path.read_text().rstrip() # 메서드 체인을 사용해서 빈줄 제거
print(content)
```

경로(Path)는 시스템에 있는 파일의 위치이고, pathlib 라이브러리 모듈을 사용한다.

코드를 실행하면 아래와 같이 출력된다.

```python
3.1415926535
  8979323846
  2643383279
```

- 상대 경로
    - 현재 실행 중인 프로그램 파일 기준으로 지정
- 절대 경로
    - 실행 중인 프로그램 파일 위치와 관계없이 지정
    

행단위로 접근하고 싶으면 아래와 같이 사용한다.

```python
# file_reader.py
path = Path("pi.digits.txt")
content = path.read_text()

lines = content.splitlines()
for line in lines:
    print(line)
```

이렇게 하면 개별적으로 조작할 수 있다.

파일 콘텐츠를 다루고 싶으면 `for`문 안에서 조작하면 된다.

출력하고 싶은 길이가 있다면 아래와 같이 사용하면 된다.

```python
print(line[:5])
```

# 2. 파일에 저장하기

`write_text()`를 사용하면 된다.

```python
# file_saver.py
from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming!")
```

이걸 실행하면 `programming.txt` 이라는 텍스트 파일이 생기게 된다.

```python
# programming.txt
I love programming!
```

여러 줄을 저장하고 싶으면 `\n`를 붙인다.

# 3. 예외

프로그램 실행 중 발생한 에러를 관리한다.

일어난 예외는 트레이스백에 포함된다. 이 예외는 `try-except` 문으로 저리가 가능하다.

- ZeroDivisionError
    - 0으로 나눌 때 발생하는 에러

```python
# exception.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

이런식으로 처리하면 된다.

`except` 이후에 `else`를 사용하면 예외가 일어나지 않았을 때 실행된다.

- FileNotFoundError
    - 파일이 없을 때 나는 에러
    

만약 조용히 실패하고 싶을 때는 `pass`를 사용한다. `pass` 문을 사용하면 블록을 건너뛰게 한다.

→ 사용자에게 알릴 필요 없을 때 사용하기!

```python
# words_count.py
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # 건너뜀
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
```

# 4. 데이터 저장하기

- `json.dumps()` : JSON으로 저장
- `json.load()` JSON으로 불러오기

```python
# number_writer.py
import json
from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

# number_reader.py
import json
from pathlib import Path

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
```

writer → reader 를 순서대로 실행하면 저장하고, 읽을 수 있다.

JSON 형태로 저장하는 것이 좋다.

```python
# remember_me.py
import json
from pathlib import Path

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# greet_user.py
from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
```

이번에도 remember_me → greet_user 파일을 순서대로 실행해보면 된다.