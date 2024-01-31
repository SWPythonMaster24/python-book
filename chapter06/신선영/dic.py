alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(f"You just earned {alien_0['points']} points!")

#

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#

del alien_0['points']
print(alien_0)

#

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages.get('jen', 'No favorite language set.'))
print(favorite_languages.get('jenny', 'No favorite language set.'))
print(favorite_languages.get('jenny'))

#


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f" Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
