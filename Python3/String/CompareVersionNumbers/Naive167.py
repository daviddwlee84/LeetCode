class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def remove_leading_zero_and_convert_to_int(num: str) -> int:
            for i, c in enumerate(num):
                if c != '0':
                    break
            return int(num[i:])
        
        ver1 = [remove_leading_zero_and_convert_to_int(num) for num in version1.split('.')]
        ver2 = [remove_leading_zero_and_convert_to_int(num) for num in version2.split('.')]
        if len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))
        elif len(ver2) < len(ver1):
            ver2 += [0] * (len(ver1) - len(ver2))

        for v1, v2 in zip(ver1, ver2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
