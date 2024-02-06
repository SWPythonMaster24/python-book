from pathlib import Path
import json

numbers = [2, 3, 5, 9, 11]

path = Path('C:/workspace/python-book/chapter10/정지희/numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)
if path.exists():
    contents = path.read_text()
    numbers = json.loads(contents)
    print(numbers)
else:
    numbers = input("What's your favorite number? ")
    contents = json.dumps(numbers)
    path.write_text(contents)
    print(f"We'll remember your fav number, {numbers}")