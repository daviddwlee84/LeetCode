class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        if len(words) < 1:
            return text
        elif len(words) == 1:
            # "  hello"
            return words[0] + spaces * ' '
        max_space = spaces // (len(words) - 1)
        space_left = spaces % (len(words) - 1)

        return (' ' * max_space).join(words) + space_left * ' '
