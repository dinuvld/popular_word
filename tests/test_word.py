from ..popular_word.word import Word

def test_evaluate_word_with_bad_char_at_beginning():
    """Test in order to see if the function successfully deletes
     illegal characters at the beginning of the word"""

    teststr = Word('""poop')
    teststr.evaluate_word()
    assert teststr.text == 'poop'

def test_evaluate_word_with_bad_char_at_end():
    """Test in order to see if the function successfully deletes
    illegal characters at the beginning of the word"""
    teststr = Word('poop"*#')
    teststr.evaluate_word()
    assert teststr.text == 'poop'

def test_evaluate_word_with_valid_character():
    """The Word.evaluate_word() func should not eliminate valid characters inside
    a word (for example ' in English or - in Romanian)"""

    testlist = list()
    word1 = Word('It\'s')
    word2 = Word('Mi-e')
    testlist.append(word1)
    testlist.append(word2)
    for item in testlist:
        item = item.evaluate_word()

    assert (testlist[0].text == 'It\'s' and testlist[1].text == 'Mi-e')

def test_check_for_sentence_end_with_entire_sentence():
    """The function should find that beautiful is the end of the sentence, not U.S.A."""

    testlist = [Word('She'), Word('said'), Word('U.S.A.'), Word('is'), Word('beautiful.')]
    for word in testlist:
        if word.check_for_sentence_end() is True:
            end_of_sentence = word.text
            break
    assert end_of_sentence == 'beautiful.'

def test_check_for_sentence_end_with_suspension_points():
    """"The function should return false for a word that contains suspension points"""

    teststr = Word("sooo...")
    test = teststr.check_for_sentence_end()
    assert test is False



