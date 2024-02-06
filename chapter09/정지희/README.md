---
marp: true
theme: uncover
---
# **챕터9 클래스**
##### 객체 지향 프로그래밍(OOP)은 실제 사물과 상황을 표현하는 클래스를 만들고, 이를 기반으로 객체를 만든다. 클래스는 해당 객체 전체가 공유하는 일반적인 동작을 정의함.
>클래스에서 객체를 만드는 것을 인스턴스화라고 하며,<br> 실제로 다루는 건 클래스의 인스턴스이다.
---
## **클래스 만들고 사용하기**
```python
class Dog:
    """개를 표현하는 클래스"""

    def __init__(self, name, age):
        """name과 age 속성 초기화"""
        self.name = name
        self.age = age
```
###### 파이썬에서는 클래스명의 첫 글자를 대문자로 표기함. <br>클래스 정의 첫 행에 해당 클래스가 하는 일을 설명하는 독스트링을 작성한다.
---
## **1) __init__()메서드**
```python
...
    def __init__(self, name, age):
        """name과 age 속성 초기화"""
        self.name = name
        self.age = age
```
###### 클래스에 속한 함수를 메서드라고 부른다. <br>__init__메서드는 클래스를 기반으로 인스턴스를 만들 때마다 파이썬이 자동으로 실행하는 특별한 메서드이다.<br>self는 필수 매개변수이며 반드시 맨 앞에 있어야한다.<br> self.name = name 행은 name 매개변수의 인수를 가져와 name 변수에 할당하고 생성되는 인스턴스에 연결된다. <br>이렇게 인스턴스를 통해 접근할 수 있는 변수를 속성이라고 부른다.
---
## **2) 클래스에서 인스턴스 만들기**
```python
class Dog:
    ...
    my_dog = Dog('Willie', 6)
    print(f"My dog's name is {my_dog.name}")
```
###### 파이썬은 인수를 전달하여 Dog의 __init__() 메서드를 호출한다 <br> __init__() 메서드는 Dog를 표현하는 인스턴스를 생성 및 인수를 통해 속성을 설정한 다음 인스턴스를 반환한다.<br>점 표기법을 통해 인스턴스의 속성 값을 찾을 수 있다.
---
## **클래스와 인스턴스 사용**
```python
class Car:
    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year= year

my_new_car = Car('audi', 'a4', 2023)
```
###### 클래스는 여러 가지 상황을 표현할 수 있다 <br>일단 클래스를 만들면 클래스보다는 인스턴스를 더 자주 사용하는데, 보통은 인스턴스에 저장된 속성을 수정하는 경우가 가장 많다
---
## **1) 속성의 기본 값 설정**
```python
class Car:
    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year= year
        self.odometer_reading = 0

my_new_car = Car('audi', 'a4', 2023)
```
###### 인스턴스 속성도 기본 값을 가질 수 있다 <br>이런 기본 값은 __init__()메서드에서 할당한다
---
## **2) 속성 값 수정**
###### 속성 값은 세 가지 방법을 수정이 가능하다<br>인스턴스에서 직접 바꾸는 방법, 메서드를 통해 값을 설정하는 방법, 메서드를 통해 일정한 양을 더하는 방법이 있다
```python
class Car:
    ...
    def update_odometer(self, mileage): # 메서드를 통해 값을 설정
        self.odometer_reading = mileage
        
    def increment_odometer(self, miles): # 메서드를 통해 값을 더하는 방법
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2023)
my_new_car.odometer_reading = 23 # 직접 수정
```
---
## **상속**
###### 만들고자 하는 클래스가 다른 클래스의 변형이라면<br>상속을 사용해 쉽게 생성 가능하며, 상속 시 속성과 메서드를 가져온다.<br>이런 경우 원래 클래스를 부모 클래스, 새 클래스를 자식 클래스라 부른다.
---
## **자식 클래스의 __init__() 메서드**
```python
class ElectricCar(Car):
    """전기차에 해당하는 특징을 정의"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```
###### 자식 클래스는 반드시 부모 클래스와 같은 파일에 있어야하고, 자식 클래스보다 앞에 부모 클래스가 있어야 한다<br>자식 클래스인 ElectricCar() 정의 시 괄호 안에 부모 클래스명을 써야한다<br>super() 함수는 부모 클래스의 메서드를 호출하는 함수이다
---
## **부모 클래스의 메서드 오버라이드**
```python
class ElectricCar(Car):
    ...
    def full_gas_tank(self):
        """전기차에는 연료통이 없습니다"""
        print("This car doesn't have a tank!")
```
###### 부모 클래스의 메서드가 자식 클래스에 알맞지 않다면 오버라이드(재정의)할 수 있다<br>부모 클래스의 메서드와 이름이 같은 메서드를 자식 클래스에서 다시 정의하면, 부모 클래스 메서드를 무시하고 자식 클래스 메서드를 사용한다
---
## **인스턴스 속성**
###### 클래스 하나를 계속 길게 만들기보단,<br>일부분을 별도의 클래스로 분리하는게 좋다<br>거대한 클래스를 함께 동작하는 더 작은 클래스로 나누는 방식을<br>합성이라 부른다
```python
class Battery:
    """전기차의 배터리를 표현하는 클래스"""

    def __init__(self, battery_size=40):
        """배터리 속성을 초기화"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력"""
        print(f"This car has a {self.battery_size}-kWh battery.")
```