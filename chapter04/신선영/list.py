
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ", that was a great trick!\n")

print("Thank you, everyone. That was a great magic show!")

#

for value in range(1,5):
    print(value)

#

numbers = list(range(2, 11, 2))
print(numbers)

#

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

#

squares = [value**2 for value in range(1, 11)]
print(squares)

#

playes = ['charles', 'martina', 'michael', 'florence', 'eli']
print(playes[0:3])

#

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)