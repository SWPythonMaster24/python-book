responses = {}

# 설문조사를 제어할 플래그
polling_active = True
while polling_active:
    # 이름과 응답을 저장한다.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장한다.
    responses[name] = response

    # 누군가 더 설문에 참여할 것인지 묻는다.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 설문결과를 출력한다.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
