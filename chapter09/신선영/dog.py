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


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
