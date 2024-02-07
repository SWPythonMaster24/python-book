from name_function import get_formatted_name

def test_first_last_name():
    """Jamis Joplin 같은 이름에서 동작하는지 테스트"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Wolfgang Amadeus Mozart 같은 이름에서 동작하는지 테스트"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'