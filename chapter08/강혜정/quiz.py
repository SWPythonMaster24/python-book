# 8-2. 좋아하는 책
# title 매게변수를 받는 favorite_book() 함수를 만드세요.
# 이 함수는 '내가 가장 좋아하는 책은 이상한 나라의 앨리스입니다.' 같은 메시지를 출력해야 합니다.
# 함수를 호출할 때는 책 제목을 인수로 전달하는 걸 잊지 마세요.
def favorite_book(title):
    print(f"내가 가장 좋아하는 책은 {title.title()}입니다.")

favorite_book('이상한 나라의 앨리스')


# 8-3. 티셔츠
# 셔츠 크기와 셔츠에 인쇄할 메시지를 받는 make_shirt() 함수를 만드세요.
# 이 함수를 실행하면 셔츠 크기, 인쇄될 메시지를 요약하는 문장이 출력되어야 합니다.
# 위치 인수를 사용해 함수를 호출하세요. 키워드 인수를 사용해서도 호출해 보세요.
def make_shirt(size, message):
    print(f"Shirt size: {size.title()}")
    print(f"Shirt message: {message.title()}")

make_shirt('L', 'Happy')


# 8-4. 라지 셔츠
# 기본적으로 "I love Python" 메시지가 인쇄된 라지 사이즈 셔츠를 만드는 make_shirt() 함수를 만드세요.
# 메시지 기본 값으로 라지와 미디엄 사이즈의 셔츠를 만들고, 임의의 메시지가 인쇄된 임의의 사이즈 셔츠를 만드세요.
def make_shirt(size, message='I love Python'):
    print(f"Shirt size: {size.title()}")
    print(f"Shirt message: {message.title()}")

make_shirt('M')
make_shirt('L')
make_shirt('S', 'I love Korea')


# 8-5. 도시
# 도시와 나라 이름을 받는 describe_city() 함수를 만드세요.
# 이 함수를 "레아캬비크는 아이슬랜드에 있습니다." 같은 단순한 문장을 출력해야 합니다.
# 나라 이름 매개변수에 기본 값을 사용하세요.
# 세 가지 도시에 대해 이 함수를 호출하되, 적어도 하나는 기본 값이 아닌 다른 나라를 사용하세요.
def describe_city(city_name, country_name="한국"):
    print(f"\n{city_name}은(는) {country_name}에 있습니다.")

describe_city('서울')
describe_city('부산')
describe_city('뉴욕', '미국')


# 8-6. 도시 이름
# 도시와 나라 이름을 받는 city_country() 함수를 만드세요.
# 이 함수는 다음과 같은 문자열을 반환해야 합니다.
# "Santiago, Chile"
# 세 개 이상의 도시-나라 쌍으로 함수를 호출하고 반환 값을 출력하세요
def city_country(city_name, country_name):
    return f"{city_name}, {country_name}".title()

city = city_country('서울', '한국')
print(city)
city = city_country('부산', '한국')
print(city)
city = city_country('뉴욕', '미국')
print(city)


# 8-7. 앨범
# 음악 앨범을 설명하는 딕셔너리를 만드는 함수 make_album()을 만드세요.
# 이 함수는 음악가 이름과 앨범 제목을 가져와서 이 정보가 포함된 딕셔너리를 반환해야 합니다.
# 함수를 사용해 세 가지 앨범을 표현하는 세 개의 딕셔너리를 만드세요.
# 각 반환 값을 출력해 딕셔너리에 앨범 정보가 정확히 저장됐는지 확인하세요.

# None으로 make_album()에 옵션 매개변수를 추가해 수록곡 숫자를 저장할 수 있습니다.
# 함수를 호출할 때 수록곡 숫자가 포함된 경우 이 값도 딕셔너리에 추가하세요.
# 수록곡이 저장된 딕셔너리가 최소 한 개는 있어야 합니다.
def make_album(musician, album, songs_number=None):
    album = { 'musician_name': musician, 'album_name': album }
    if songs_number:
        album['songs_number'] = songs_number
    return album

album = make_album("(여자)아이들", "2")
print(album)
album = make_album("올티 및 론", "OLLONE AT ALLONE")
print(album)
album = make_album("주영", "Sphere", 15)
print(album)


# 8-8. 사용자 앨범
# [연습문제 8-7]의 프로그램으로 시작합니다. 
# 사용자가 앨범 음악가와 타이틀을 입력할 수 있는 while 루프를 만드세요.
# 사용자 입력으로 make_album()을 호출한 다음 반환된 딕셔너리를 출력하세요.
# while 루프에 종료 값을 만드는 걸 잊지 마세요.
while True:
    print("\nPlease tell me album information:")
    print("(enter 'q' at any time to quit)")

    musician_name = input("musician name: ")
    if musician_name == 'q':
        break

    album_name = input("album name: ")
    if album_name == 'q':
        break

    album = make_album(musician_name, album_name)
    print(album)