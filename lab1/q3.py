import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'words.txt')


def add_parentheses(w):
    return f'({w})'


def to_lower(w: str):
    return w.lower()


with open(file_path, 'r') as file:
    for line in file:
        words = line.rstrip().split(' ')
        words_with_parentheses = map(add_parentheses, words)
        lowercase_words = map(to_lower, words_with_parentheses)
        print(''.join(lowercase_words))
