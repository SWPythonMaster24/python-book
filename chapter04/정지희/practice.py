# 4-10 슬라이스
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f"리스트의 첫 세 항목은: {my_foods[:3]}")
print(f"리스트의 중간 세 항목은: {my_foods[1:4]}")
print(f"리스트의 마지막 세 항목은: {my_foods[-3:]}")

# 4-11 피자

# 4-12 루프 연습
friend_foods = my_foods[:]
for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)

# 4-13 뷔페
store_food = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
for food in store_food:
    print(food)

store_food = ('pizza', 'pasta', 'choco cake', 'cannoli', 'ice cream')
for food in store_food:
    print(food)
