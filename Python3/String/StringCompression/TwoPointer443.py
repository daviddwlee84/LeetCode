from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        https://leetcode.com/problems/string-compression/solutions/3245597/day-61-two-pointer-o-1-space-and-o-n-time-easiest-beginner-friendly-sol/
        """
        read = 0
        write = 0
        
        while read < len(chars):
            # Current char
            count = 1

            # Keep track of same chars
            while read < len(chars) - 1 and chars[read] == chars[read + 1]:
                count += 1
                read += 1
            
            # Write answer
            chars[write] = chars[read]
            write += 1
            
            if count > 1:
                for char in str(count):
                    chars[write] = char
                    write += 1
            
            read += 1
        
        # The answer don't care the values that indices are "> write"
        return write
