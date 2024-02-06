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
my_leaf.describe_battery()
