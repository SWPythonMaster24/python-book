# 9-1 레스토랑
class Restaurant:
    def __init__(self, name, cui_sine_type):
        self.name = name
        self.cui_sine_type = cui_sine_type

    def describ_restaurant(self):
        print(f"레스토랑 이름은 {self.name}입니다.\n{self.cui_sine_type}입니다.")

    def open_restaurant(self):
        print("\n레스토랑이 문을 열었습니다")


fav_restraurant = Restaurant('coco', "choco")
fav_restraurant.describ_restaurant()
fav_restraurant.open_restaurant()