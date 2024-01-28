# 외계인을 저장할 빈 리스트를 만든다.
aliens = []

# 녹색 외계인을 30명 만든다.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 처음 다섯 외계인을 표시한다.
for alien in aliens[:5]:
    print(alien)
print("...")

# 생성된 외계인이 얼마나 많은지 표시한다.
print(f"Total number of aliens: {len(aliens)}")
