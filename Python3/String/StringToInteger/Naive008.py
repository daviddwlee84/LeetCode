class Solution:
    def myAtoi(self, s):
        """
        :type s: string
        :rtype: int
        """
        s += '\0'
        # Pretending writing in C
        # So i += 1 won't be out of range
        # Or we need to check if i < length

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        sign = 1
        base = 0
        i = 0
        while s[i] == ' ':
            i += 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while s[i] >= '0' and s[i] <= '9':
            print(i, s[i], base, INT_MAX/10)
            if (base > INT_MAX//10 or (base == INT_MAX//10 and int(s[i]) > 7)) and sign == 1:
                return INT_MAX
            elif (base > INT_MAX//10 or (base == INT_MAX//10 and int(s[i]) > 8)) and sign == -1:
                return INT_MIN
            else:
                base = 10 * base + int(s[i])
                i += 1
        return base * sign

