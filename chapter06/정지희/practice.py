# 6-1 사람
user = {
    'first_name': 'Lee',
    'last_name': 'Youngji',
    'city': 'Busan',
    'age': 25
}

# 6-2 좋아하는 숫자
favorite_num = {
    'Lee': 4,
    'Park': 7,
    'Jung': 21
}

for key, value in favorite_num.items():
    print(f"{key.title()}'s favorite number is {value}")

# 6-3 사전
chapter5 = {
    'if문': '핵심은 true or false. 조건 테스트라고도 한다.',
    '동등연산자': '연산자의 왼쪽, 오른쪽 값이 일치하면 true, 불일치 시 false를 반환',
    '불일치연산자': '두 값이 다른지 확인할 때 사용',
    'and': '두 조건 모두 만족',
    'or': '두 조건 중 하나만 만족'
}
for key, value in chapter5.items():
    print(f"{key}: {value}")