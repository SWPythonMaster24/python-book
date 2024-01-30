alien_0 = {'color' : 'green',   'points' : 5}
alien_1 = {'color' : 'yellow',  'points' : 10}
alien_2 = {'color' : 'red',     'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 외계인을 저장할 빈 리스트를 만듭니다.
aliens = []

# 녹색 외계인을 30명 만듭니다.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 처음 다섯명의 외계인을 표시합니다.
for alien in aliens[:5]:
    print(alien)
print("...")

# 외계인을 얼마나 만들었는지 표시합니다.
print(f"Total number of aliens {len(aliens)}.")