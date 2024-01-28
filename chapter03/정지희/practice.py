# 3-1 이름
name = ["yeji", "hangyu", "jihyeon", "sohyeon"]
print(name[0].title())
print(name[-1].title())
# 3-2 인사말
print(f"Good night, {name[1].title()}")
# 3-3 나만의 리스트
car = ["Jeep", "mini", "KHAN"]
print(f"나는 {car[0].title()} 자동차를 갖고 싶습니다.")

# 3-4 손님 리스트
artists = ['Leonardo da Vinci', 'Vincent Van Gogh', 'Pablo Picasso']
print(f"You are invited for {artists} Exhibition. ")

# 3-5 손님 리스트 변경
pop_artist = artists.pop(1)
print(pop_artist)
artists.insert(1, 'Claude Monet')
print(f"You are invited for {artists} Exhibition. ")

# 3-6 더 많은 손님
artists.append('Johannes Vermeer')
print(f"You are invited for {artists} Exhibition. ")

# 3-7 배송 지연
print("We can invite only two artist.")
artists.pop()
print("Sorry")
artists.pop()
print("Sorry")
print(artists)
del artists[0]
del artists[0]
print(artists)

# 3-11 의도적 에러
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
print(motorcycles[-1])