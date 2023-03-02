from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        https://leetcode.com/problems/string-compression/submissions/907777754/
        """
        # Dummy char to take care last char
        chars.append('')
        # Beginning of a series of same characters
        beginning = 0
        # i.e. Length of the answer
        compress_end = 0

        for i in range(len(chars)):
            if chars[i] == chars[beginning]:
                # Only take action when new char starts
                continue

            # Record previous unique char
            chars[compress_end] = chars[beginning]
            compress_end += 1

            # Count number of repeats and record
            count = i - beginning
            if count > 1:

                # Equivalent:

                # for j in str(count):
                #     chars[compress_end] = j
                #     compress_end += 1

                count_list = list(str(count))
                chars[compress_end:compress_end + len(count_list)] = count_list
                compress_end += len(count_list)

            beginning = i

        return compress_end
