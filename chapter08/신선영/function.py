def greet_user():
    """단순한 인사말을 출력합니다."""
    print("Hello!")


greet_user()


#

def describe_pet(animal_type, pet_name='willie'):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog')


#

def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#

def get_formatted_name(first_name, last_name, middle_name=''):
    """읽기 쉬운 전체 이름을 반환합니다."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#

def build_person(first_name, last_name, age=None):
    """사람에 관한 정보 딕셔너리를 반환합니다."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


#

def greet_users(names):
    """리스트의 각 사용자에게 단순한 인사말을 출력합니다."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#

# 출력할 디자인을 저장합니다.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 게 없을 때까지 디자인을 출력합니다
# 출력한 디자인을 completed_models로 옮깁니다
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 완료된 디자인을 표시합니다
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


#


def make_pizza(*toppings):
    """만들고자 하는 피자를 요약합니다."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#

def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
