def load_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words_list = file.read().split()
        return words_list
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def is_valid_subset(super_set, sub_set, hinge):
    if hinge not in sub_set:
        return False
    else:
        return sub_set.issubset(super_set)


def dict_parser(letters, hinge):
    super_set = set(letters)
    words = load_words_from_file('alt_words.txt')
    
    candidates = []
    for word in words:
        if is_valid_subset(super_set = super_set, sub_set = set(word), hinge=hinge) and len(word) > 3:
            candidates.append(word)
    
    return candidates

def api():
    letters = ''
    for i in range(7):
        letters += input(f'Input Letter {i + 1}: ')
    
    hinge = input(f'Hinge Letter: ')

    return hinge, letters

def main():
    hinge, letters = api()
    candidates = sorted(dict_parser(letters=letters, hinge=hinge))

    for i, candidate in enumerate(candidates):
        print(f'{i}. {candidate}')

if __name__ == '__main__':
    main()