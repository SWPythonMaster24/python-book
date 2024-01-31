responses = {}

# 설문조사를 제어할 플래그
polling_active = True

while polling_active:
    # 참가자 이름과 응답을 받습니다.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장합니다.
    responses[name] = response

    # 설문조사에 참가할 사람이 더 있는지 확인합니다.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 설문조사가 끝났으므로 결과를 출력합니다.
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")