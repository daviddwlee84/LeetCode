class Solution:
    def minFlips(self, target: str) -> int:
        i = 0
        n = len(target)
        while i < n:
            if target[i] == "1":
                break
            i += 1

        count = 0
        curr = "1"
        while i < n:
            if target[i] == curr:
                count += 1
                if curr == "1":
                    curr = "0"
                elif curr == "0":
                    curr = "1"
            i += 1

        return count
