from name_function import get_formmate_name

def test_first_last_name():
    """Jains Joplin이름과 같은지 확인"""
    formatted_name = get_formmate_name('jains', 'joplin')
    assert formatted_name == "Jains Joplin"

def test_first_last_middle_name():
    """Wolfgang Amadeus Mozart같은 이름에 대한 테스트"""
    full_name = get_formmate_name('wolfgang', 'mozart', 'amadeus')
    assert full_name == 'Wolfgang Amadeus Mozart'