from Naive009 import Solution as naive

def test_naive():
    assert naive().isPalindrome(121) == True
    assert naive().isPalindrome(-121) == False
    assert naive().isPalindrome(10) == False
    assert naive().isPalindrome(123321) == True