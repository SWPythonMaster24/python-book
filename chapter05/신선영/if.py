cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # car의 값이 'bmw'와 같으면
        print(car.upper())
    else:
        print(car.title())

#

car = 'audi'
print(car == 'audi')  # True
print(car == 'bmw')  # False
print(car == 'Audi')  # False
print(car == 'Audi'.lower())  # True

age = 19
print(age == 19)  # True
print(age < 21)  # True
print(age > 21)  # False
print(age <= 23 and age >= 18)  # True
print(age <= 23 or age >= 18)  # True

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False
print('pepperoni' not in requested_toppings)  # True

#
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#

if age < 4:  # 4세 미만이면
    price = 0
elif age < 18:  # 4세 이상 18세 미만이면
    price = 5
else:  # 18세 이상이면
    price = 10

print(f"Your admission cost is ${price}.")

#

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
