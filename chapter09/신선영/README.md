# 9. 클래스

객체 지향 프로그래밍은 실제 사물, 상황을 표현하는 **클래스(Class)**를 만들고, 이 클래스를 기반으로 **객체(Object)**를 만든다. 클래스에는 해당 객체 전체가 공유하는 일반적인 동작을 정의한다.

클래스에서 객체를 만드는 것 → **인스턴스화**

즉, 우리가 다루는 것은 클래스의 **인스턴스**

# 1. 클래스를 만들고 사용하기

```python
# dog.py
class Dog:
    """개를 표현하는 클래스"""
    
    def __init__(self, name, age):
        """인스턴스 변수 초기화"""
        self.name = name
        self.age = age

    def sit(self):
        """명령에 따라 앉는다"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """명령에 따라 구른다"""
        print(f"{self.name} rolled over!")
```

- 클래스 이름의 첫 글자는 대문자로!
- `__init()__` 메서드는 생성자 역할을 함
    - 메서드 바디에서 정의하는 self 는 이 클래스에서 생성한 인스턴스의 변수를 의미함
    - 이렇게 인스턴스를 통해 접근할 수 있는 변수를 속성이라고 부름

실제로 호출할 땐 이렇게 한다.

```python
# dog.py
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

코드를 실행하면 아래와 같이 출력된다.

```
My dog's name is Willie.
My dog is 6 years old.
```

물론 여러 개를 만들수도 있다.

각 개는 속성이 서로 다른 인스턴스이며, 행동은 고유하다.

# 2. 클래스와 인스턴스 사용하기

```python
# car.py
class Car:
    """자동차를 나타내는 클래스"""
    
    def __init__(self, make, model, year):
        """자동차의 기본 정보를 초기화"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """알아보기 쉬운 이름을 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
```

`get_descriptive_name()` 를 사용하면 각 속성을 개별적으로 호출하지 않아도 된다.

속성의 기본값을 설정할 수도 있다. 예를 들면 `self.odometer_reading = 0` 으로 설정하는 것 처럼!

수정하는 방법은 두 가지가 있다.

- 인스턴스 값에 직접 접근
    - ex. `my_car.dometer_reading = 23`
- 메서드를 통해 수정
    - ex. `my_car.update_odometer(23)`
    - 이렇게 수정해야 적합한 값인지 확인할 수 있는 로직을 추가로 넣거나 할 수 있다.
    - 마찬가지로 메서드를 부르면 값을 증가시키게도 구현할 수 있다.

# 3. 상속

상속을 사용하면 자식 클래스가 부모 클래스를 상속받을 수 있다.

```python
# car.py
class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다."""
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2020)
print(my_leaf.get_descriptive_name())
```

위의 Car를 상속받으려면 클래스 선언문 뒤에 부모 클래스의 이름을 쓴다.

`super()` 을 쓰게 되면 부모 클래스의 메서드를 호출할 수 있다.

코드를 실행하면 아래와 같이 출력된다.

```
2020 Nissan Leaf
```

```python
# car.py
class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다."""
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2020)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery() # This car has a 75-kWh battery.
```

이렇게 하면 자식 클래스에만 메서드를 추가하게 된다.

메서드 이름을 부모 클래스와 똑같이 쓰면 오버라이드 한다.

Q. 만약 여기서 배터리 부분만 빼고 싶으면?

A. 배터리를 별도의 객체로 만들고 `self.battery = Battery()` 이런식으로초기화하면 된다. 이걸 합성이라고 한다.

# 4. 클래스 임포트

상속, 합성을 잘 사용하더라도 파일이 길어질 수 있다.

이럴 때는 import를 사용하면 된다.

```python
# my_car.py
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name()) # 2019 Audi A4
```

이렇게 하면 import 문을 읽고 car 모듈에서 Car 클래스를 임포트한다.

- 모듈에 여러 클래스를 저장할 수도 있다.
    - 실제로 import 할 때는 `from car import ElectricCar` 이렇게 하면 됨!
- 모듈에 여러 클래스를 임포트할 수도 있다.
    - 실제로 import 할 때는 `from car import Car, ElectricCar` 이렇게 하면 됨!
- 전체 모듈을 임포트할 수도 있다.
    - 이렇게! `import Car`
- 모듈에서 모든 클래스를 임포트할 수도 있다.
    - 이렇게! `from module_name import *`
    - 하지만 이 방법은 권장하지 않는다. 이름 충돌이 생길 수도 있고 찾기 어려운 에러가 발생할 수도 있기 때문
    - 차라리 모듈 전체를 임포트하고 `module_name.ClassName` 사용하기
- 모듈에서 모듈 임포트하기도 가능하다.

# 5. 파이썬 표준 라이브러리

- random 모듈
    - randint(1, 6): 1~6 사이의 난수 생성
    - choice([’a’, ‘b’, ‘c’]): 랜덤으로 선택

# 6. 클래스 스타일

- 클래스 정의 바로 다음에는 독스트링이 있어야 한다.
- 카멜 표기법을 쓰라
- 표준 라이브러리, 커스텀 모듈을 임포트하는 경우 표준 라이브러리 먼저, 그 다음에 빈줄, 그 다음에 커스텀 모듈