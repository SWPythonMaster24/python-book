pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets) # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets) # ['dog', 'dog', 'goldfish', 'rabbit']