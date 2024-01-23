# 대소문자 변경
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 문자열 안에서 변수 사용하기
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# 탭과 줄바꿈
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

# 공백 없애기
favorite_language = '  I like python    '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# 접두사 제거하기
url = "https://www.naver.com"
print(url.removeprefix("https://"))
print(url.removeprefix("naver"))
