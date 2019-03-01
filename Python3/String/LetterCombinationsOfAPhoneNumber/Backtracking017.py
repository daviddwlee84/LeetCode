from typing import List

NumberTable = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        self.combinations = []
        self.helper(digits, "")

        return self.combinations
    
    def helper(self, digits_left: str, combination: str):
        for digit in NumberTable[digits_left[0]]: # try every possible char for each number
            combination += digit
            if len(digits_left) == 1: # only one digit left
                self.combinations.append(combination)
            else:
                self.helper(digits_left[1:], combination) # recursive call to next number
            combination = combination[:-1] # pop out the last digit
