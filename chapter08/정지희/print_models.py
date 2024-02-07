def print_models(unprinted_designs, completed_models):
    """"
    남은게 없을 때까지 디자인을 출력합니다.
    출력이 끝난 디자인을 completed_models 리스트로 이동합니다.
    """
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        print(f"Printing model: {current_desing}")
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    """출력된 모델을 모두 표시합니다."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)