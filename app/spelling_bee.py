def load_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            words_list = file.read().split()
        return words_list
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def is_valid_subset(super_set, sub_set, center_letter):
    # check if center letter is included in the candidate word
    if center_letter not in sub_set:
        return False

    # check if the candidate word can be spelled with the given letters
    else:
        return sub_set.issubset(super_set)


def dict_parser(letters, center_letter):
    super_set = set(letters)
    words = load_words_from_file("alt_words.txt")
    candidates = []

    # loop through words and check our conditions, add to list if met
    for word in words:
        if (
            is_valid_subset(
                super_set=super_set, sub_set=set(word), center_letter=center_letter
            )
            and len(word) > 3
        ):
            candidates.append(word)

    return candidates


def api():
    letters = ""
    # prompt user to input today's letters
    for i in range(7):
        letters += input(f"Input Letter {i + 1}: ")

    # clarify which letter is today's letter
    center_letter = input("Center Letter: ")

    # add checks to user input
    if center_letter not in letters:
        raise ValueError("Invalid input: Center letter not included in letters.")

    if not isinstance(letters, str):
        raise ValueError('Invalid input: Not all letters are of type string.')

    if len(letters) != 7:
        raise ValueError(
            f'Invalid input: Incorrect number of letters input, {len(letters)}, correct length is 7.')

    return center_letter, letters


def main():
    center_letter, letters = api()
    candidates = sorted(dict_parser(
        letters=letters, center_letter=center_letter))

    for i, candidate in enumerate(candidates):
        print(f"{i}. {candidate}")

    return 0


if __name__ == "__main__":
    main()
