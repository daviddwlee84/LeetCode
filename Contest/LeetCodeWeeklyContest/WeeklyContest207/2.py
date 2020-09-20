class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.answer_set = set()

        def helper(pos: int, curr_set: set):
            if pos == len(s) and len(curr_set) > len(self.answer_set):
                self.answer_set = curr_set.copy()
                return

            for i in range(pos + 1, len(s) + 1):
                if s[pos:i] not in curr_set:
                    # curr_set.add(s[pos:i])
                    # helper(i, curr_set)
                    # curr_set.remove(s[pos:i])

                    helper(i, curr_set | set([s[pos:i]]))

        helper(0, set())

        return len(self.answer_set)
