from ..popular_word.string import String

def test_insert_at_the_beggining_of_the_string():
    teststr = String('poop')
    teststr.insert_char(0, 'c')
    assert teststr.text == 'cpoop'

def test_insert_at_the_end_of_the_string():
    teststr = String('poop')
    teststr.insert_char(4, 'c')
    assert teststr.text == 'poopc'

def test_insert_in_the_string():
    teststr = String('poop')
    teststr.insert_char(2, 'c')
    assert teststr.text == 'pocop'

def test_delete_at_the_beggining_of_the_string():
    teststr = String('poop')
    teststr.delete_char(0)
    assert teststr.text == 'oop'

def test_delete_at_the_end_of_the_string():
    teststr = String('poop')
    teststr.delete_char(3)
    assert teststr.text == 'poo'

def test_delete_in_the_string():
    teststr = String('pocp')
    teststr.delete_char(2)
    assert teststr.text == 'pop'

def test_replace_at_the_beggining_and_end_of_the_string():
    teststr = String('poop')
    teststr.replace_char('p', 'l')
    assert teststr.text == 'lool'

def test_replace_at_the_middle_of_the_string():
    teststr = String('poop')
    teststr.replace_char('o', 'a')
    assert teststr.text == 'paap'
    
def test_searching_for_characters_at_the_beggining_and_end_of_the_string():
    teststr = String('poop')
    position_list = teststr.search_for_char('p')
    assert position_list == [0, 3]

def test_searching_for_character_in_the_string():
    teststr = String('poop')
    position_list = teststr.search_for_char('o')
    assert position_list == [1, 2]