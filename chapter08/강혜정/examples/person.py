def build_person(first_name, last_name, age=None):
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)