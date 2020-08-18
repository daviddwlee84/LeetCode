class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        to_cover = set(range(1, n + 1))
        we_have = set()
        for i in range(1, 2**len(nums)):
            j = 0
            temp = 0
            while i > 0:
                if i & 1:
                    temp += nums[j]
                i >>= 1
                j += 1
            we_have.add(temp)

        answer = 0
        still_need = to_cover - we_have

        while still_need:
            to_add = min(still_need)
            still_need.remove(to_add)

            answer += 1
            for item in we_have.copy():
                we_have.add(to_add + item)
                try:
                    still_need.remove(to_add + item)
                except:
                    pass
            we_have.add(to_add)
        return answer


# TLE
