class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                char_count = [0] * 10  # a ~ j
                for char in word[i:j + 1]:
                    index = ord(char) - ord('a')
                    char_count[index] += 1

                # print(word[i:j + 1])
                # print(char_count)

                if sum(count % 2 == 1 for count in char_count) <= 1:
                    ans += 1
        return ans

# TLE
# "bibacdfehgbchbjicccecacbdeiggideciijgbahifjjhdeddeabbfihbegbagcgbidefijigabfjhbdjfiihggdbjacgjccidedajgaabdibcdfjfjfeifefdeachbcbdadggiagbdfigjadeaadfbadhfjgifeeaagiabddicdejcgaejcdgffggdddffideijchchaffgjhfeaffhbfahieggdahdbeijfjbeaciagfjjbcjdbjgdfeefbgjfhcbajbdghgeieiahadebeiabjedjhbfbhfhajcieibaejefbfeihebbjgciceibbabddcaeehdfdhbeeeffdijfghdfeedfcccfchjhdjddfgehiccdggbdjjghicagdhceiaebfhjhbefghjjcbjbjbfbbdhhdbdbceejaffbdbidaefihcjagaibhihbebhjfggbddhedfcacagegfaiiaeheiggjhfaegffdicgebabceaahjeegafgjgfejfeheafidabjbgafjcdgffdafcgecjdjefcbhefbfghgegfegdabjiicihfdbjjiehjfbjfhgaeacjgfbggggjegffgbabafdhbbiadgfcbfcicjagceeibhagieiddjjhcjdidccgjfbgihadhhjihgdaheibigihefacfbdgfiefehgjbbcggccfcibhbhhjjagjhehciejafbhjeicaieagjagdaaaddfgiibgicgjghdjiddaeihbcbccbfjigdjcachhdcgfheaacfhfajefbccgjcdcaahjaaedcibbjgggajaceijababjafbaccfiffcbedjc"
