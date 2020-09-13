class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        start = len(s) - 1
        end = len(s)

        while start >= 0:
            if s[start] == t[start]:
                # print(start, end)
                end -= 1
                start -= 1
            else:
                while s[start] != t[end - 1]:
                    start -= 1
                    if start < 0:
                        return False

                # print(start, end, s[start:end], t[start:end])

                s = s[:start] + ''.join(sorted(s[start:end]))

                # print(s)

                if s[start:end] == t[start:end]:
                    end = start
                    start = end - 1
                else:
                    if s[end - 1] == t[end - 1]:
                        end -= 1
                        start = end - 1
                    else:
                        return False

        return True
