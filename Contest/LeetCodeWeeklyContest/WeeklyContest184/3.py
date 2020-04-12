import re


class Solution:
    def entityParser(self, text: str) -> str:
        special_characters = {
            '&quor;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }
        found_possible = re.findall(r'&\w+;', text)

        for pattern in found_possible:
            if pattern in special_characters:
                text.replace(pattern, special_characters[pattern])

        return text
