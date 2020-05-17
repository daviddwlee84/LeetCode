from collections import defaultdict


class Solution:
    def arrangeWords(self, text: str) -> str:
        buffer = defaultdict(list)
        words = text.lower().split()

        for word in words:
            buffer[len(word)].append(word)

        arranged_words = [value for key, value in sorted(
            list(buffer.items()), key=lambda x: x[0])]

        firstWord = True
        answer = []
        for words_with_same_len in arranged_words:
            for word in words_with_same_len:
                if firstWord:
                    answer.append(word.capitalize())
                    firstWord = False
                else:
                    answer.append(word)

        return ' '.join(answer)
