from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        if len(s) == 4:
            return [".".join(s)]
        
        self.ans = []
        self.backtrack("", s, 4)
        
        return self.ans
        
    def backtrack(self, currentIp: str, leftStr: str, leftCount: int):
        if leftCount == 0 and len(leftStr) == 0:
            self.ans.append(currentIp)
        if leftCount == 0 and len(leftStr) > 0:
            return
        
        if len(currentIp) > 0:
            currentIp += "."
            
        for i in range(1, 4):
            print(leftStr[:i])
            if i <= len(leftStr) and int(leftStr[:i]) <= 255:
                if i > 1 and leftStr[0] == "0":
                    # must deal with leading zero (it is invalid in IP addresses)
                    continue
                self.backtrack(currentIp + leftStr[:i], leftStr[i:], leftCount - 1)

# Runtime: 36 ms, faster than 73.06% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Restore IP Addresses.
