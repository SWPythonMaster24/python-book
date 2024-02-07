# Chapter 9. 클래스

## 클래스를 만들고 사용하기
```python
class Dog:  # 클래스 이름의 첫글자를 대문자로 표기
    """개를 표현하는 클래스"""

    def __init__(self, name, age):
        """name과 age 속성 초기화"""
        self.name = name
        self.age = age

    def sit(self):
        """앉기"""
        print(f"{self.name} is not sitting.")

    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over!")
```

### __init__() 메서드
- `__init__()` 메서드는 클래스를 기반으로 인스턴스를 만들 때마다 파이썬이 자동으로 실행하는 메서드이다.
- 클래스의 메서드는 모두 self가 붙은 변수를 사용할 수 있으며, 이 클래스에서 생성한 인스턴스를 통해 이 변수에 접근할 수 있다. (= 속성(attribute))

### 클래스에서 인스턴스 만들기
```python
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# 출력:
# My dog's name is Willie.
# My dog is 6 years old.
```
똑같은 이름, 나이를 설정하더라도 별도의 인스턴스를 생선한다.


## 클래스와 인스턴스 사용하기
```python
class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
```

### 속성의 기본 값 설정하기
인스턴스 속성도 기본 값을 가질 수 있다. 기본 값은 `__init__()` 메서드에서 할당한다.
```python
def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # <<< 기본값
```

### 속성 값 수정하기
1. 인스턴스에서 직접 바꾸는 방법
```python
class Car:
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()  # 23 출력
```
2. 메서드를 통해 값을 설정하는 방법
```python
class Car:
    -- 생략 --

    def update_odometer(self, mileage):
        """거리계를 주어진 값으로 설정합니다"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```


## 상속
클래스가 다른 클래스를 상속할 때는 속성과 메서드를 가지고 오는데, 원래 클래스를 *부모 클래스*, 새 클래스를 *자식 클래스* 라 부른다.

자식 클래스는 부모 클래스의 속성과 메서드를 일부, 또는 모두 상속할 수 있고 자신만의 속성과 메서드를 새로 정의할 수도 있다.

```python
class ElectricCar(Car):
    """전기차에만 해당하는 특징을 정의합니다"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다"""
        super().__init__(make, model, year)
    

my_leaf = ElectricCar('missan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# 출력:
# 2024 Missan Leaf
```
`super()` 함수는 부모 클래스의 메서드를 호출한다.

```python
class ElectricCar(Car):
    """전기차에만 해당하는 특징을 정의합니다"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    

my_leaf = ElectricCar('missan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# 출력:
# 2024 Missan Leaf
# This car has a 40-kWh battery.
```
자식 클래스에만 해당하는 속성과 메서드를 추가할 수 있다.

부모 클래스의 메서드와 이름이 같은 메서드를 자식 클래스에서 다시 정의하면 오버라이드 된다.

### 인스턴스 속성
클래스가 커지면 클래스 하나를 계속 방대하게 만들기보다는, 그 일부분을 별도의 클래스로 분리하는 게 좋다. 거대한 클래스를 함께 동작하는 더 작은 클래스로 나누는 방식을 **합성(composition)** 이라고 한다.
```python
class Battery:
    """전기차의 배터리를 표현하는 클래스"""

    def __init__(self, battery_size=40):
        """배터리 속성을 초기화합니다"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    -- 생략 --

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다"""
        super().__init__(make, model, year)
        self.battery = Battery()    # 합성

    

my_leaf = ElectricCar('missan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
```


## 클래스 임포트
클래스에 기능을 추가하다 보면 파일이 길어질 수 있다 -> 클래스를 모듈에 저장하고 임포트하기
### 단일 클래스 임포트하기
```python
from car import Car
```

### 모듈에서 여러 클래스 임포트하기
```python
from car import Car, ElectricCar
```

### 전체 모듈 임포트하기
```python
improt car
```

### 모듈에서 모든 클래스 임포트하기
```python
from module_name import *
```
권장하지 않는 방법이다. 이유는 1) 이름 충돌이 생길 수 있음  2) 찾기 어려운 에러가 일어날 수 있음

모듈 하나에서 여러 가지 클래스를 임포트할 때는 모듈 전체를 임포트해서 `module_name.ClassName` 문법을 쓰자.

### 모듈에서 모듈 임포트하기
가능하다 👍

### 별칭 사용하기
```python
from electric_car improt ElectricCar as EC
```


## 클래스 스타일
- 클래스 이름은 **카멜 표기법**
- 인스턴스와 모듈 이름은 소문자 + 스네이크 표기법
- 클래스 정의 다음에는 독스트링
- 클래스 내부의 메서드 사이에는 빈 줄 하나 삽입, 모듈 내부의 클래스들은 빈 줄 두 개로 구분
- 표준 라이브러리 모듈을 먼저 임포트하고, 빈 줄을 하나 삽입하고, 개인이 만든 모듈을 임포트 해야 한다.