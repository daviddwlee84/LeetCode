from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        """
        backtracking
        """

        answer = []

        def backtrack(pos: int, str_list: List[str]):
            if pos == len(S):
                answer.append(''.join(str_list))
                return

            if ord('9') >= ord(S[pos]) >= ord('0'):
                backtrack(pos + 1, str_list + [S[pos]])
            else:
                backtrack(pos + 1, str_list + [S[pos].lower()])
                backtrack(pos + 1, str_list + [S[pos].upper()])

        backtrack(0, [])

        return answer

# Runtime: 120 ms, faster than 13.04% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 15 MB, less than 19.18% of Python3 online submissions for Letter Case Permutation.
