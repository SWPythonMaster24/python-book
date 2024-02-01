alien_color = "green"

if alien_color.lower() == "green":
    print("The player has 5 points.")
elif alien_color.lower() == "yellow":
    print("The player has 10 points.")
elif alien_color.lower() == "red":
    print("The player has 15 points.")

age = 18

if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("elder")

favorite_fruits = ["apple", "strawberry", "grape"]

if 'strawberry' in favorite_fruits:
    print("You really like strawberries")

if 'apple' in favorite_fruits:
    print("You really like apples")

if 'banana' in favorite_fruits:
    print("You really like bananas")

if 'grape' in favorite_fruits:
    print("You really like grapes")