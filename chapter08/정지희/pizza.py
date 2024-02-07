def make_pizza(size, *toppings):
    """주문 내용을 요약합니다"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")