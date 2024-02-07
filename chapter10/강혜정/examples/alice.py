from pathlib import Path

def count_words(path):
    """파일에 포함된 단어 개수를 대략적으로 셉니다"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)