from pathlib import Path
import json

numbers = [2, 3, 5, 6, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)