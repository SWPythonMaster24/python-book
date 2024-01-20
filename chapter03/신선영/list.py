bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-2])
print(f"My first bicycle was a {bicycles[0].title()}.")

#

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#

friends = ['김민수', '김철수', '홍길동']
friends.append('김영희')
print(friends)

friends.insert(1, '김영수')
print(friends)

del friends[2]
print(friends)

friends.pop()
print(friends)

friends.pop(0)
print(friends)

friends.remove('김영수')
print(friends)

print(f"마지막으로 남은 친구는 {friends[0]}입니다.")


#

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars.reverse()
print(cars)
print(len(cars))