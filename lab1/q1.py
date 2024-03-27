import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'words.txt')

with open(file_path, 'r') as file:
    for line in file:
        print(line, end='')
