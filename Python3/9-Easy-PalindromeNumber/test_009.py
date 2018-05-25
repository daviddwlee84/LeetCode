from Naive009 import Solution as naive
from NotString009 import Solution as notString

def test_naive():
    assert naive().isPalindrome(121) == True
    assert naive().isPalindrome(-121) == False
    assert naive().isPalindrome(10) == False
    assert naive().isPalindrome(123321) == True

def test_notString():
    assert notString().isPalindrome(121) == True
    assert notString().isPalindrome(-121) == False
    assert notString().isPalindrome(10) == False
    assert notString().isPalindrome(123321) == True