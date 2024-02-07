from pathlib import Path

path = Path('C:/workspace/python-book/chapter10/정지희/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
