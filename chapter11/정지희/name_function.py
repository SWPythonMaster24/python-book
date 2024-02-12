def get_formmate_name(first, last, middle=''):
    """실제 이름을 깔끔한 형식으로 반환한다"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()