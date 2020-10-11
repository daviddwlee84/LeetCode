class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        a_palidrome = True
        b_palidrome = True
        a_comb_palidrome = True
        a_b_comb_palidrome = True
        a_a_comb_palidrome = True

        b_comb_palidrome = True
        b_a_comb_palidrome = True
        b_b_comb_palidrome = True

        n = len(a)
        # print(n)
        for i in range(n // 2):
            # print(a[i], a[n - i - 1], b[i], b[n - i - 1])
            if a[i] != a[n - i - 1]:
                a_palidrome = False
            if b[i] != b[n - i - 1]:
                b_palidrome = False
            if a[i] != b[n - i - 1] or not a_comb_palidrome:
                a_comb_palidrome = False
                if b[i] != b[n - i - 1]:
                    a_b_comb_palidrome = False
                if a[i] != a[n - i - 1]:
                    a_a_comb_palidrome = False
            if b[i] != a[n - i - 1] or not b_comb_palidrome:
                b_comb_palidrome = False
                if a[i] != a[n - i - 1]:
                    b_a_comb_palidrome = False
                if b[i] != b[n - i - 1]:
                    b_b_comb_palidrome = False

        return a_palidrome or b_palidrome or a_b_comb_palidrome or b_a_comb_palidrome or a_a_comb_palidrome or b_b_comb_palidrome

# WA (solved)
# "pvhmupgqeltozftlmfjjde"
# "yjgpzbezspnnpszebzmhvp"
# true

# WA (solved)
# "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
# "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
# true


if __name__ == "__main__":
    print(Solution().checkPalindromeFormation(
        "pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"))
    print(Solution().checkPalindromeFormation(
        "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))
