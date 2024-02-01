request_toppings = []
 
if request_toppings:
    for request_topping in request_toppings:
        print(f"Adding {request_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
