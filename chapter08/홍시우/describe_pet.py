def describe_pet(animal_type, pet_name = 'harry'):
    print(f"\nI have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster')
describe_pet('dog', pet_name = 'willie')
describe_pet(pet_name = "willie", animal_type="dog")