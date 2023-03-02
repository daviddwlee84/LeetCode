from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = None
        count = 0
        answer = ''
        for char in chars:
            if prev is None:
                prev = char
                count = 1
                continue

            if char == prev:
                count += 1
            else:
                if count == 1:
                    answer += f'{prev}'
                else:
                    answer += f'{prev}{count}'
                count = 1

            prev = char

        if count > 0:
            if count == 1:
                answer += f'{prev}'
            else:
                answer += f'{prev}{count}'

        # modifying the input array
        chars.clear()
        for char in answer:
            chars.append(char)
        return len(answer)
