# 딕셔너리 사용하기
alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])         # green

new_points = alien_0['points']  # 5
print(f"You just erned {new_points} points!")

# 키-값 쌍 추가하기
alien_0['x_position'] = 0
alien_0['y position'] = 25

print(alien_0)                  # {'color': 'green', 'points': 5, 'x_position': 0, 'y position': 25}

# 빈 딕셔너리로 시작하기
alien_0 = {}

alien_0['color']    = 'green'
alien_0['points']   = 5

print(alien_0)                  # {'color': 'green', 'points': 5}

# 딕셔너리 값 수정하기
alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")  # The alien is green.
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  # The alien is now yellow.

# 활용
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original position : {alien_0['x_position']}")

# 외계인을 오른쪽으로 이동합니다.
# 외계인의 현재 속도에 따라 얼마나 멀리 이동할 수 있는지 파악합니다.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 빠른 외계인 입니다.
    x_increment = 3

# 새 위치는 기존 위치 + 증가값(increment) 입니다.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position : {alien_0['x_position']}")

# 키-값 쌍 제거하기
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)  # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)  # {'color': 'green'}