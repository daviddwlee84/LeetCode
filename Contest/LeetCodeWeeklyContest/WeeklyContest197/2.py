class Solution:
    def numSub(self, s: str) -> int:
        found = False
        count = 0
        modulo = 10**9 + 7
        collect = []
        for char in s:
            if not found:
                if char == '1':
                    # first meet 1
                    found = True
                    count += 1
            else:
                if char == '1':
                    count += 1
                else:
                    collect.append(count)
                    found = False
                    count = 0
        if count:
            collect.append(count)

        answer = 0
        for count in collect:
            answer += sum([i for i in range(1, count + 1)])
            answer %= modulo

        return answer
