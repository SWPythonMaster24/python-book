from pathlib import Path

# Path to the file
# path = Path("pi.digits.txt")
# content = path.read_text()
# print(content)


path = Path("pi.digits.txt")
content = path.read_text()

lines = content.splitlines()
for line in lines:
    print(line[:5])
