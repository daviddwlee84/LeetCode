class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer approach
        """
        front = 0
        end = len(s) - 1

        empty_string = True

        while front <= end:
            # https://www.studytonight.com/post/python-string-methods-isdigit-isnumeric-and-isdecimal
            while front < len(s) and not s[front].isalpha() and not s[front].isdecimal():
                front += 1

            while end >= 0 and not s[end].isalpha() and not s[end].isdecimal():
                end -= 1

            if front > end:

                if empty_string:
                    # don't forget this
                    return True

                return False

            if s[front].lower() != s[end].lower():
                empty_string = False
                return False

            front += 1
            end -= 1

        return True
