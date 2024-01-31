# 확인해야 할 사용자가 담긴 리스트,
# 확인된 사용자를 저장할 빈 리스트
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 확인하지 않은 사용자가 남아있으면 계속 진행합니다.
# 확인된 사용자는 해당 리스트로 옮깁니다.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user : {current_user.title()}")
    confirmed_users.append(current_user)

# 확인된 사용자를 모두 표시합니다.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())