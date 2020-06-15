import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            # assume IP v4
            nums = IP.split('.')
            if len(nums) != 4:
                return 'Neither'
            
            for num in nums:
                try:
                    num_int = int(num)
                except:
                    return 'Neither'

                if str(num_int) != num:
                    return 'Neither'
                
                if num_int > 255 or num_int < 0:
                    return 'Neither'
            
            return 'IPv4'
            
        else:

            single_IPv6 = re.compile(r'^[0-9a-fA-F]{1,4}$')
            
            nums = IP.split(':')
            if len(nums) != 8:
                return 'Neither'
            
            for num in nums:
                if not single_IPv6.search(num):
                    return 'Neither'
                
            return 'IPv6'

# Runtime: 28 ms, faster than 69.38% of Python3 online submissions for Validate IP Address.
# Memory Usage: 13.9 MB, less than 32.24% of Python3 online submissions for Validate IP Address.
