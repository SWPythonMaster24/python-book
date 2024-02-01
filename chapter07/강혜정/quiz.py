# 7-1 렌터카
# 사용자에게 어떤 렌터카를 원하는지 묻는 프로그램을 작성하세요.
# 입력을 사용해 "스바루를 찾아보겠습니다." 같은 메시지를 출력하세요.
car = input("고객님 어떤 렌트카를 찾으시나요?: ")
print(f"{car}을(를) 찾아보겠습니다.")

# 7-2 레스토랑 좌석 
# 저녁 식사에 몇 명이 참여하는지 묻는 프로그램을 작성하세요.
# 입력이 9 이상이라면 대기해야 한다는 메시지를 출력하세요.
# 8 이하라면 테이블이 있다는 메시지를 출력하세요.
attendees = input("\n손님 몇 분이신가요?: ")
attendees = int(attendees)

if attendees >= 9:
    print(f"{attendees} 분이시면 20분 정도 대기하셔야 할 것 같습니다. 괜찮으신가요?")
else:
    print("안쪽으로 좌석 안내 도와드리겠습니다.")


# 7-3 10의 배수
# 사용자에게 숫자를 요청한 다음 그 숫자가 10의 배수인지 알리는 프로그램을 만드세요.
number = input("\n숫자를 입력해 주세요: ")

if number.isdigit():    # 문자열이 모두 숫자로 이루어져 있는지 판단함.
    number = int(number)
    if number % 10 == 0:
        print("입력한 값은 10의 배수입니다.")
    else:
        print("입력한 값은 10의 배수가 아닙니다.")
else:
    print("입력한 값은 정수가 아닙니다.")


# 7-4 피자 토핑
# 사용자가 quit를 입력할 때까지 계속해서 어떤 토핑을 추가할지 물어보는 루프를 만드세요.
# 사용자가 토핑을 입력하면 그 토핑을 피자에 추가하겠다는 메시지를 출력하세요.
while True:
    topping = input('\n피자에 어떤 토핑을 추가하시겠습니까?: ')
    print(f"{topping}이 추가되었습니다.")


# 7-5 영화 티켓
# 손님의 나이에 따라 입장료를 다르게 받는 극장이 있습니다.
# 3세 미만은 무료, 3세 이상 12세 미만은 10달러, 12세 이상은 15달러입니다.
# 사용자의 나이를 묻고 입장료를 알려주는 루프를 만드세요.
while True:
    age = input("\nOO영화관입니다. 몇 살이신가요? ")
    age = int(age)

    if age < 3:
        print("3세 미만은 무료입니다.")
    elif age < 12:
        print("3세 이상 12세 미만은 10달러입니다.")
    else:
        print("12세 이상은 15달러입니다.")


# 7-6 세 가지 종료 방법
# 연습문제 7-4 혹은 7-5를 다음과 같이 수정하세요.
# - while 문에서 조건 테스트를 사용해 루프를 중지하세요.
topping = ''
while topping != 'quit':
    topping = input("\n피자에 어떤 토핑을 추가하시겠습니까?\n(중지하지려면 'quit'를 입력해주세요): ")
    if topping != 'quit':
        print(f"{topping}이 추가되었습니다.")


# - active 변수를 사용해 루프를 종료하세요.
active = True
while active:
    age = input("\nOO영화관입니다. 몇 살이신가요?\n(종료하시려면 'quit'를 입력해주세요): ")
    
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("3세 미만은 무료입니다.")
        elif age < 12:
            print("3세 이상 12세 미만은 10달러입니다.")
        else:
            print("12세 이상은 15달러입니다.")

# - 사용자가 quit을 입력하면 break 문을 써서 루프를 중지하세요.
while True:
    topping = input("\n피자에 어떤 토핑을 추가하시겠습니까?\n(중지하지려면 'quit'를 입력해주세요): ")
    if topping == 'quit':
        break
    else:
        print(f"{topping}이 추가되었습니다.")


# 7-7 무한 루프
# 무한 루프를 만들어 실행하세요(ctrl+C를 눌러 루프를 종료하거나 터미널을 닫으세요.)
while True:
    print('Hello')


# 7-8 샌드위치
# sandwich_orders 리스트에 여러 가지 샌드위치 이름을 저장하세요.
# 그 다음 빈 리스트 finished_sandwiches를 만드세요.
# 주문된 샌드위치 리스트를 순회하면서 "참치 샌드위치를 만들었습니다." 같은 메세지를 출력하세요.
# 이 샌드위치를 finished_sandwiches 리스트로 이동하세요.
# 샌드위치를 모두 만들면 이들을 나열하는 메시지를 출력하세요.
sandwich_orders = ['햄 샌드위치', '치즈 샌드위치', '햄치즈 샌드위치', '캐찹 샌드위치']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"{current_order}를 만들었습니다.")
    finished_sandwiches.append(current_order)

# 확인된 사용자를 모두 표시합니다
print("\n완료된 샌드위치 목록: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())


# 7-9 훈제 샌드위치
# 7-8의 sandwich_orders 리스트를 사용하되, 훈제 샌드위치를 리스트 안에 최소 세 개 이상 넣으세요.
# 프로그램 시작 부분에서 훈제가 다 떨어졌다는 메시지를 출력하고, while 루프를 사용해 sandwich_orders에서 모두 제거하세요.
# finished_sandwiches에 훈제 샌드위치가 없는지 확인하세요.
sandwich_orders = ['햄 샌드위치', '치즈 샌드위치', '훈제 샌드위치', '캐찹 샌드위치', '훈제 샌드위치']

print("\n주문 목록입니다.", sandwich_orders)
print("앗! 훈제 샌드위치 재료가 떨어졌네요. 주문 취소를 해야겠네요.")
while '훈제 샌드위치' in sandwich_orders:
    sandwich_orders.remove('훈제 샌드위치')

print("\n주문 취소 후 만들어야 하는 샌드위치 목록: ")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())


# 7-10 환상의 휴가
# 사용자에게 가고 싶은 휴가지를 묻는 프로그램을 만드세요.
# "If you could visit one place in the world, where would you go?" 같은 프롬프트를 표시하고, 설문조사 결과를 출력하세요.
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to go {response}.")