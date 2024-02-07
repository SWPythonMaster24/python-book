from pathlib import Path 

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)