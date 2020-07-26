import heapq


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        prev = None
        count = []  # [[count, char], ...]
        for char in s:
            if prev == char:
                count[-1][0] += 1
            else:
                count.append([1, char])
            prev = char

        heapq.heapify(count)

        while count and k >= count[0][0]:
            cnt, _ = heapq.heappop(count)
            k -= cnt

        answer = 0
        for cnt, _ in count:
            if cnt == 1:
                answer += 1
            else:
                answer += 2

        return answer

# Not a greedy problem
# WA
# "aabbaa"
# [[2, 'a'], [2, 'b']] => 4
# delete "bb" => "a4" => 2
