'''Get the frequency of unique letters in an iterable of characters.'''


def analyze_frequencies(characters):
    '''
    characters: Iterable of characters.
    Return: Dictionary of form {letter: frequency}.
    '''
    freqs = dict()

    characters = characters.upper()

    for char in characters:
        if _is_letter(char):
            freqs[char] = characters.count(char)

    return freqs


def _cli_main():
    print()
    characters = _prompt_for_characters()
    frequencies = analyze_frequencies(characters)

    print(); print()
    _report_frequencies(frequencies)
    print()

def _is_letter(character):
    if len(character) == 1:
        return character.isalpha()
    else:
        return False

def _prompt_for_characters():
    print('Characters:\n')
    chars = input()

    return chars

def _report_frequencies(frequencies):
    num_letters = len(frequencies)
    sorted_freqs = dict(sorted(
        frequencies.items(),
        key = lambda freqs: freqs[1],
        reverse=True
    ))

    print(f"Frequencies for {num_letters} letters:\n")

    for char, freq in sorted_freqs.items():
        print(f'{char}: {freq}')


if __name__ == '__main__':
    _cli_main()

