# 10-1 파이썬 학습
from pathlib import Path

path = Path('C:/workspace/python-book/chapter10/정지희/learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)

# 10-2 c언어
for line in lines:
    if 'Python' in line:
        print(line.replace('Python', 'C'))
    else:
        print(line)

# 10-4 손님
names = ''

while True:
    name = input('사용자 이름? ')
    if name == 'q':
        break
    else:
        names += (f"{name}\n")

guest = Path('C:/workspace/python-book/chapter10/정지희/guest.txt')
guest.write_text(names)

# 10-6 덧셈
number1, number2 = input('숫자 두개를 입력하세요(공백기준): ').split()
try:
    number1 = int(number1)
    try:
        number2 = int(number2)
        print(number1+number2)
    except ValueError:
        pass
except ValueError:
    print("숫자를 입력하지 않으셨습니다.")
