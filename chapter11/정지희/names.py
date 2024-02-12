from name_function import get_formmate_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Pelase give me a first name: ")
    if first == 'q':
        break
    last = input("Pelase give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formmate_name(first, last)
    print(f"\tNeatly formatted name {formatted_name}")