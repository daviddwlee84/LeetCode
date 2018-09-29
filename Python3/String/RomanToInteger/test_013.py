from Naive013 import Solution as naive

Romans = []
Romans.append("III")
Romans.append("IV")
Romans.append("IX")
Romans.append("LVIII")
Romans.append("MCMXCIV")

Answers = []
Answers.append(3)
Answers.append(4)
Answers.append(9)
Answers.append(58)
Answers.append(1994)

def test_naive():
    for i, roman, in enumerate(Romans):
        assert naive().romanToInt(roman) == Answers[i]