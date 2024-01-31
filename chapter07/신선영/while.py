current_number = 1
while current_number <= 10:

    if (current_number % 2 == 0):
        current_number += 1
        continue

    if current_number == 7:
        break

    print(current_number)
    current_number += 1
