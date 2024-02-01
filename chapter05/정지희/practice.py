# 5-1 조건테스트(3개만 함)
car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')


print("\nIs car == 'bmw'? I predict Fasle.")
print(car == 'bmw')

car = 'bmw'
print("\nIs car == 'toyota'? I predict False.")
print(car == 'toyota')


print("\nIs car == 'bmw'? I predict True.")
print(car == 'bmw')

car = 'subaru'
print("\nIs car == 'subaru'? I predict False.")
print(car == 'subaru')


print("\nIs car == 'bmw'? I predict True.")
print(car == 'bmw')

# 5-2 더 많은 조건 테스트
banned_users = ['andrew', 'carolina', 'david']
user1 = 'carolina'
user2 = 'marie'

print(user2 == 'marie')

print(user1 == user2)

print(22 > 0 and 1 < 4)

print(22 > 0 or 1 > 4)

if user1 in banned_users: 
    print(f"{user1.title()}, you can't post a response if you wish")

if user2 not in banned_users: 
    print(f"{user2.title()}, you can post a response if you wish")

# 5-3 외계인 색깔1
align = 'yellow'

if 'green' == align:
    print("5점 획득")

align = 'green'

if 'green' == align:
    print("5점 획득")

# 5-4 외계인 색깔2
if 'yellow' == align:
    print("5점 획득")
else:
    print("10점 획득")

# 5-5 외계인 색깔3
if 'yellow' == align:
    print("5점 획득")
elif 'green' == align:
    print("10점 획득")
elif 'red' == align:
    print("15점 획득")

# 5-6 삶의 단계
age = 14

if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenage")
elif age >= 20 and age < 35:
    print("adult")
elif age >= 65:
    print("elder")


# 5-8 관리자
users = ['admin', 'andrew', 'carolina', 'david', 'Jj']
for user in users:
    if user == 'admin':
        print("관리자님 안녕하세요. 상태 보고서를 보시겠습니까?")
    else:
        print(f"{user.title()}님 안녕하세요. 다시 로그인해 주셔서 감사합니다.")

# 5-9 사용자 없음
users = []

if users:
    print("user 존재")
else:
    print("사용자가 있어야 합니다.")

# 5-11 서수
nums = list(range(1, 10))

for num in nums:
    if(num == 1):
        print(f"{num}st")
    elif(num == 2):
        print(f"{num}nd")
    elif(num == 3):
        print(f"{num}rd")
    else:
        print(f"{num}th")