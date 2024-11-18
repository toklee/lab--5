import re

PATH = 'task1-ru.txt'
PATH_OUT = 'modified_task1-ru.txt'


def find_words(text):
    words = re.findall(r"\b\w{3,5}\b", text)
    return words


def find_numbers(text):
    numbers = re.findall(r"\b\d{4,}\b", text)
    return numbers


with open(PATH, encoding='utf-8') as text, open(PATH_OUT, 'w', encoding='utf-8') as out:
    for line in text:
        words = find_words(line)
        numbers = find_numbers(line)
        res = words + numbers

        if res:
            out.write(' '.join(res) + '\n')
        print(res)