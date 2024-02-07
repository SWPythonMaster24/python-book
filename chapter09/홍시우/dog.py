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
        
my_dog      = Dog('Willie', 6)
your_dog    = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()