# 7-1 렌터카
car = input("어떤 렌터카를 원하나요?: ")

print(f"{car}를 찾아보겠습니다.")

# 7-2 레스토랑 좌석
num = input("저녁 식사에 몇명이 참여하나요?: ")
num = int(num)

if num <= 8:
    print("테이블이 있습니다.")
else:
    print("테이블이 부족합니다.")

# 7-3 10의 배수
num = input("숫자를 입력하세요: ")
num = int(num)

if num % 10 == 0:
    print("10의 배수입니다.")
else:
    print("10의 배수가 아닙니다.")

# 7-4 피자토핑
topping = input("어떤 토핑을 추가할건가요?: ")

print(f"{topping}을 피자에 추가하겠습니다.")

# 7-5 영화티켓
old = input("나이가 어떻게 되시나요?: ")
old = int(old)

if old < 3:
    print("무료")
elif old >= 3 and old < 12:
    print("10달라")
else:
    print("15달라")

# 7-8 샌드위치
sandwich_orders = ['참치', '계란', '고기']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"{sandwich} 샌드위치를 만들었습니다.")
    finished_sandwiches.append(sandwich)

for finised_sandwich in finished_sandwiches:
    print(finised_sandwich)