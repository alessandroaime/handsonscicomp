from fizzbuzz import fizzbuzz
def test_fizzbuzz():
    assert fizzbuzz(0) == 'fizzbuzz'
    assert fizzbuzz(1) == 1
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'
