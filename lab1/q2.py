import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'words.txt')


def add_parentheses(w):
    return f'({w})'


with open(file_path, 'r') as file:
    for line in file:
        words = line.rstrip().split(' ')
        words_with_parentheses = map(add_parentheses, words)
        print(''.join(words_with_parentheses))
