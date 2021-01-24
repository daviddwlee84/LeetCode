from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        max_a_char = max(a, key=ord)
        min_a_char = min(a, key=ord)
        max_b_char = max(b, key=ord)
        min_b_char = min(b, key=ord)

        ops_to_satisfy_one = min(
            sum(bc <= max_a_char for bc in b), sum(ac >= min_b_char for ac in a))
        ops_to_satisfy_two = min(
            sum(ac <= max_b_char for ac in a), sum(bc >= min_a_char for bc in b))

        ops_to_satisfy_three = len(
            a) - Counter(a).most_common(1)[0][1] + len(b) - Counter(b).most_common(1)[0][1]

        print(ops_to_satisfy_one)
        print(ops_to_satisfy_two)
        print(ops_to_satisfy_three)

        return min(ops_to_satisfy_one, ops_to_satisfy_two, ops_to_satisfy_three)

# "aba"
# "caa"
# "dabadd"
# "cda"
# "da"
# "cced"

# WA
# "ace"
# "abe"
# 2
