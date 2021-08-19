'''Replace occurrences of characters in an iterable of characters.'''

from stringcolor import cs as _ColorString
from stringcolor.ops import Color as _Color


def substitute(characters, replacements, should_color_substitutions=False):
    '''
    characters: Iterable of characters.
    replacements: Dictionary of form {original: replacement}.
    Return: List of original characters with replacements.
    '''
    substitution = list(characters.upper())
    replacements = _uppercase_all_strings_in_dict(replacements)

    for old,new in replacements.items():
        new = new.lower()
 
        if should_color_substitutions:
            new = _ColorString(string=new, color='Green')

        substitution = [new if(char == old) else char for char in substitution]


    return _uppercase_all_characters(substitution)

def _uppercase_all_strings_in_dict(dictionary):
    uppercased_dict = dict()

    for k,v in dictionary.items():
        if type(k) is str:
            k = k.upper()
        if type(v) is str:
            v = v.upper()

        uppercased_dict[k] = v

    return uppercased_dict

def _uppercase_all_characters(characters):
    result = list()

    for char in characters:
        if type(char) == _Color:
            char = _ColorString(string=char.string.upper(), color=char.color)
            result.append(char)
        else:
            result.append(char.upper())

    return result


def _cli_main():
    should_color_substitutions = True

    print()
    characters = _prompt_for_characters()
    print(end='\n\n')
    replacements = _prompt_for_replacements()
    replacements = _uppercase_all_strings_in_dict(replacements)

    substitution = substitute(characters, replacements, should_color_substitutions)

    print()
    _report_results(substitution, replacements)
    print()

def _prompt_for_characters():
    print('Characters:\n')
    chars = input()

    return chars

def _prompt_for_replacements():
    replacements = dict()

    while True:
        print('Replace this character: ', end='')
        original = answer1 = input()

        print('With this character: ', end='')
        replacement = answer2 = input()

        answers = (answer1, answer2)
        if ('' in answers) or (' ' in answers):
            break

        print()

        replacements[original] = replacement

    return replacements

def _report_results(substitution, replacements):
    if not replacements:
        print('\nNo replacements')
        return

    print()

    print('Replacements:\n');
    for o,r in replacements.items():
        o = _ColorString(string=o, color='Red')
        r = _ColorString(string=r, color='Green')

        print(f'{o} -> {r}')

    print()

    print('Result:\n');
    for char in substitution:
        print(char, end='')

    print()


if __name__ == '__main__':
    _cli_main()

