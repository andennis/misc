from text_words_histogram import calc_words


def test_calc_words():
    txt = 'Hello , hello: my   world !'
    result = calc_words(txt)
    assert len(result) == 3
    assert result['hello'] == 2
    assert result['my'] == 1
    assert result['world'] == 1
