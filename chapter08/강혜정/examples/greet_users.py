def greet_users(names):
    """리스트의 사용자에게 단순한 인사말을 출력합니다"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)