def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_complete_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []

print_models(unprinted_designs[:], complete_models)
show_complete_models(complete_models)

print(unprinted_designs)

complete_models = []
print_models(unprinted_designs, complete_models)

print(unprinted_designs)