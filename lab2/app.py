import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'index.txt')


def create_posting_list(file_path):
    posting_list = dict()
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.strip().split(' ')
            term = tokens[0]
            postings = list(map(int, tokens[1:]))
            posting_list[term] = postings
    return posting_list


def merge_and(l1: list, l2: list):
    result_set = set()
    result_set.update(l1)
    result_set.intersection_update(l2)
    result_list = list(result_set)
    result_list.sort()
    return result_list


def merge_or(l1: list, l2: list):
    result_set = set()
    result_set.update(l1)
    result_set.update(l2)
    result_list = list(result_set)
    result_list.sort()
    return result_list


def merge_not(l1: list, l2: list):
    result_set = set()
    result_set.update(l1)
    result_set.difference_update(l2)
    result_list = list(result_set)
    result_list.sort()
    return result_list


if __name__ == '__main__':
    posting_list = create_posting_list(file_path)
    prompt = input('QUERY: ')
    tokens = prompt.lower().strip().split(' ')
    op = tokens[1]
    term1 = tokens[0]
    term2 = tokens[2]
    if (op == 'and'):
        print(
            merge_and(posting_list[term1], posting_list[term2])
        )
    elif (op == 'or'):
        print(
            merge_or(posting_list[term1], posting_list[term2])
        )
    elif (op == 'not'):
        print(
            merge_not(posting_list[term1], posting_list[term2])
        )
    else:
        print('Invalid Query')
