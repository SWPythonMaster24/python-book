# 2-3 개별메세지
to_name = "Miranda"
print(f"안녕하세요. {to_name}, 오늘 파이썬 배워 보는 게 어떨까요?")
# 2-4 이름의 대소문자
print(to_name.title())
print(to_name.upper())
print(to_name.lower())
# 2-5,6 명언
famouse_person = "Conan O'Brien"
print(f"Pelease do not be cynical. If you work really hard and you're kind, amazing things will happen. \n-{famouse_person}");
# 2-7 이름에서 공백 제거
name = " Jay "
print(f"\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}")
# 2-8 파일 확장자
file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))
# 2-9 숫자
print(2+6)
print(9-1)
print(2*4)
print(24/3)
# 2-10 좋아하는 숫자
LIKE_NUM = 7
print(f"가장 좋아하는 숫자는 {LIKE_NUM}.")