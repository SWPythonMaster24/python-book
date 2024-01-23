motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(2, 'triumph')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owne a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
