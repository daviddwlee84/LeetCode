class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        memory = {}  # if a subword is a wonderful substring
        for i in range(len(word)):
            for j in range(i, len(word)):
                char_count = [0] * 10  # a ~ j
                subword = word[i:j + 1]

                if subword not in memory:
                    for char in subword:
                        index = ord(char) - ord('a')
                        char_count[index] += 1

                    if sum(count % 2 == 1 for count in char_count) <= 1:
                        memory[subword] = True
                    else:
                        memory[subword] = False

                ans += memory[subword]

        return ans

# TLE
# "bibacdfehgbchbjicccecacbdeiggideciijgbahifjjhdeddeabbfihbegbagcgbidefijigabfjhbdjfiihggdbjacgjccidedajgaabdibcdfjfjfeifefdeachbcbdadggiagbdfigjadeaadfbadhfjgifeeaagiabddicdejcgaejcdgffggdddffideijchchaffgjhfeaffhbfahieggdahdbeijfjbeaciagfjjbcjdbjgdfeefbgjfhcbajbdghgeieiahadebeiabjedjhbfbhfhajcieibaejefbfeihebbjgciceibbabddcaeehdfdhbeeeffdijfghdfeedfcccfchjhdjddfgehiccdggbdjjghicagdhceiaebfhjhbefghjjcbjbjbfbbdhhdbdbceejaffbdbidaefihcjagaibhihbebhjfggbddhedfcacagegfaiiaeheiggjhfaegffdicgebabceaahjeegafgjgfejfeheafidabjbgafjcdgffdafcgecjdjefcbhefbfghgegfegdabjiicihfdbjjiehjfbjfhgaeacjgfbggggjegffgbabafdhbbiadgfcbfcicjagceeibhagieiddjjhcjdidccgjfbgihadhhjihgdaheibigihefacfbdgfiefehgjbbcggccfcibhbhhjjagjhehciejafbhjeicaieagjagdaaaddfgiibgicgjghdjiddaeihbcbccbfjigdjcachhdcgfheaacfhfajefbccgjcdcaahjaaedcibbjgggajaceijababjafbaccfiffcbedjc"
