def build_profile(first, last, **user_info):
    """사용자에 관해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)