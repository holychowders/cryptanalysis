from cryptanalysis.freq_analysis import analyze_frequencies


def test_analyze_frequencies_1():
    characters = 'ABBCCC'
    expected = {'A': 1, 'B': 2, 'C': 3}
    
    result = analyze_frequencies(characters)

    assert result == expected

def test_analyze_frequencies_2():
    characters = 'abbccc'
    expected = {'A': 1, 'B': 2, 'C': 3}
    
    result = analyze_frequencies(characters)

    assert result == expected

def test_analyze_frequencies_3():
    characters = 'bbccca'
    expected = {'A': 1, 'B': 2, 'C': 3}
    
    result = analyze_frequencies(characters)

    assert result == expected

def test_analyze_frequencies_4():
    characters = 'a bb !@#ccc '
    expected = {'A': 1, 'B': 2, 'C': 3}
    
    result = analyze_frequencies(characters)

    assert result == expected

