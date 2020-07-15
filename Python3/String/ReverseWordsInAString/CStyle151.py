from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/discuss/47840/C++-solution-in-place:-runtime-O(n)-memory-O(1)
        https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/discuss/172258/Python-or-Two-Pointers-+-No-Cheating-tm
        https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/discuss/47720/Clean-Java-two-pointers-solution-(no-trim(-)-no-split(-)-no-StringBuilder)

        https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/discuss/47740/In-place-simple-solution
        """
        s_arr = list(s)
        length = len(s)
        # word_end is the next char index after a word
        curr, word_start, word_end, word_count = 0, 0, 0, 0

        while True:
            while curr < length and s_arr[curr] == ' ':
                # skip spaces in front of the word
                curr += 1

            if curr == length:
                # end of loop
                break

            if word_count:
                s_arr[word_end] = ' '
                word_end += 1

            word_start = word_end

            while curr < length and s_arr[curr] != ' ':
                # move the word forward
                s_arr[word_end] = s_arr[curr]
                curr += 1
                word_end += 1

            self.reverseWord(s_arr, word_start, word_end - 1)
            word_count += 1

        # resize result string
        s_arr = s_arr[:word_end]
        # reverse whole string
        self.reverseWord(s_arr, 0, word_end - 1)

        return ''.join(s_arr)

    def reverseWord(self, s_arr: List[str], front: int, end: int):
        while front < end:
            s_arr[end], s_arr[front] = s_arr[front], s_arr[end]
            front += 1
            end -= 1


# Runtime: 68 ms, faster than 7.90 % of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.8 MB, less than 5.05 % of Python3 online submissions for Reverse Words in a String.
