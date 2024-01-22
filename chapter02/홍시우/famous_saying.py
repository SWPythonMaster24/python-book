famous_person = "알베르트 아인슈타인"
print(f"{famous_person}, \"한번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.")

famous_person = "\t\n  알베르트 아인슈타인  "

print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))