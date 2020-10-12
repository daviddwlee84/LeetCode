class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        
        exist = set()
        duplicate_char = False
        different = {}
        for i in range(len(A)):
            if A[i] != B[i]:
                different[i] = (A[i], B[i])
            else:
                if A[i] in exist:
                    duplicate_char = True
                exist.add(A[i])
            
            if len(different) > 2:
                return False
        
        if len(different) == 1:
            return False
        
        if len(different) == 0:
            return duplicate_char
        
        diff = list(different.values())
        return diff[0][1] == diff[1][0] and diff[0][0] == diff[1][1]

# Runtime: 28 ms, faster than 92.07% of Python3 online submissions for Buddy Strings.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
