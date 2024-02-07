class Dog:
    """개를 표현하는 클래스"""

    def __init__(self, name, age):
        """name과 age 속성 초기화"""
        self.name = name
        self.age = age

    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()