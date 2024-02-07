# 8-1 메시지
def display_message() :
    print("Hello, Python")

display_message()

# 8-2 좋아하는 책
def favorite_book(book_title):
    print(f"내가 가장 좋아하는 책은 {book_title}입니다.")

favorite_book("이상한 나라의 앨리스")

# 8-6 도시 이름
def city_country(city_name, country_name):
    print(f"{city_name.title()}, {country_name.title()}")

city_country("santiago", "chile")