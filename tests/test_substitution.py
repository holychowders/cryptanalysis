from cryptanalysis.substitution import substitute


def test_substitute_1():
    characters = 'ABCD'
    replacements = {'A':'D', 'D':'B'}
    expected = list('DBCB')
    
    result = substitute(characters, replacements)

    assert result == expected

def test_substitute_2():
    characters = 'abcd'
    replacements = {'a':'d', 'd':'b'}
    expected = list('DBCB')
    
    result = substitute(characters, replacements)

    assert result == expected

def test_substitute_3():
    characters = 'aBcD'
    replacements = {'A':'d', 'd':'B'}
    expected = list('DBCB')
    
    result = substitute(characters, replacements)

    assert result == expected

def test_substitute_4():
    characters = 'abcd abcd\nabcd'
    replacements = {'A':'d', 'd':'B'}
    expected = list('DBCB DBCB\nDBCB')
    
    result = substitute(characters, replacements)

    assert result == expected

def test_substitute_5():
    characters = 'abcd abcd abcd'
    replacements = {'A':'d', 'd':'B'}
    expected = list('DBCB DBCB DBCB')
    
    result = substitute(characters, replacements)

    assert result == expected

def test_substitute_6():
    characters = 'abcd'
    replacements = {'A':'d', 'd':'B'}
    expected = list('DBCB')
    
    result = substitute(characters, replacements, should_color_substitutions=True)

    assert result[0].string == expected[0]
    assert result[1] == expected[1]
    assert result[2] == expected[2]
    assert result[3].string == expected[3]

