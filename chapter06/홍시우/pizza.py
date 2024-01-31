# 주문받은 피자 정보를 저장합니다
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

# 주문 요약
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")