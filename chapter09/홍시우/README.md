---
title: Chapter_09 클래스
author: rain_poem
date: 2024-02-03 10:00:00 +0800
categories: [Development, Python]
tags: [python, study]
pin: false
math: true
mermaid: true
---

## 클래스를 만들고 사용하기
```python
# 개를 표현하는 클래스
class Dog:

    # name과 age 속성 초기화
    def __init__(self, name, age):
        self.name   = name
        self.age    = age

    # 앉기
    def sit(self):
        print(f"{self.name} is now sitting.")

    # 구르기    
    def roll_over(self):
        print(f"{self.name} rolled over!")
```

**Dog 클래스**를 정의하였습니다.<br>
```__init__()``` 메서드는, 클래스로 객체를 만들 때마다 자동으로 실행되는 메서드입니다.<br>
```self``` 인수는 인스턴스 자체를 나타내며,<br>
이 인수는 메서드를 호출할 때 자동으로 전달되므로, 항상 정의에 포함되있어야 합니다.<br>
```self``` 매개변수를 통해 해당 인스턴스의 **속성(변수)** 이나 **메서드**에 접근할 수 있습니다.<br>

```python
class Dog:
    --생략--

my_dog      = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

your_dog    = Dog('Lucy', 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```
파이썬은 첫번째 행을 읽고 **Dog 클래스**의 ```__ init__()``` 메서드를 호출합니다.<br>
여기서 ```__init__()``` 메서드는 해당 **클래스**의 인스턴스를 만들어서 반환합니다.<br>
반환된 인스턴스는 my_dog 변수에 할당하여, 예제와 같이 인스턴스 **속성**에 접근할 수 있습니다.<br>
마찬가지로 **메서드**를 호출할 수 있습니다.<br>

## 클래스와 인스턴스 사용하기
```python
class Car:
    # 자동차를 표현하는 클래스

    def __init__(self, make, model, year):
        self.make   = make
        self.model  = model
        self.year   = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
```
```__init__()``` 메서드에서 인스턴스 속성의 기본값을 설정할 수 있습니다.<br>
인스턴스를 통해 속성값을 수정할 수 있습니다.<br>
메서드를 통해 속성값을 수정할 수 있습니다.<br>

## 상속
```python
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self)
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")
```

기본 클래스를 바탕으로 새 클래스를 만들 수 있습니다.<br>
이때 부모 클래스의 ```__init__()``` 메서드를 호출해야 될 때가 있는데,<br>
```super()``` 함수를 통해 부모 클래스의 메서드를 호출할 수 있습니다.<br>
또한, 자식 클래스에서만 해당하는 속성과 메서드를 추가할 수 있습니다.<br>
<br>
```메서드 오버라이드(재정의)```를 통해 부모 클래스의 **메서드**를 자식클래스에 맞게 수정할 수 있습니다.<br>
자식 클래스에서 동일한 이름의 **메서드**를 재정의하게 되면, 자식 클래스의 **메서드**를 실행합니다.<br>

```python
class Battery:

    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")
```
**클래스** 하나를 방대하게 만들기 보다는 별도의 클래스로 분리하는 것이 좋습니다.<br>
이를 ```합성```이라 부릅니다.<br>
예제에서는, 전기차에대해, 배터리라는 클래스를 정의하여 사용하고 있습니다.<br>

## 클래스 임포트
```python
# 단일 클래스 임포트
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# 모듈에서 여러 클래스 임포트하기
from car import Car, ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_new_car.get_descriptive_name())

# 전체 모듈 임포트 하기
improt car

# 별칭 사용하기
from electric_car improt ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
```

함수와 마찬가지로 모듈로부터 임포트하여 사용할 수 있습니다.<br>

## 클래스 스타일

- 클래스 이름은 **카멜 표기법**을 사용합니다.<br>
- 반면 인스턴스와 모듈 이름은 소문자와 밑줄로 만들어야합니다.<br>
- 클래스 정의 다음에는 독스트링이 있어야합니다.<br>
- 클래스 내부의 메서드 사이에는 빈 줄을 하나 삽입합니다.<br>
- 모듈 내부의 클래스들은 빈 줄 두개로 구분합니다.<br>