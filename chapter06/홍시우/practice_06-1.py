address_book_0 = {
    'first_name'    : 'enrico',
    'last_name'     : 'fermi',
    'age'           : 24,
    'city'          : 'Seoul'
}

print(address_book_0)

favoirte_number_0 = {
    'Mr.A' : 5,
    'Mr.B' : 13,
    'Mr.C' : 8,
    'Mr.D' : 1,
    'Mr.E' : 7
}

number = favoirte_number_0.get('Mr.A', 0)
print(f"Mr.A favorite number is {number}.")