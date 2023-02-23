class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = version1.split('.'), version2.split('.')

        # Assume ver2 is the longer one
        ver1_ver2_swapped = 1
        if len(ver1) > len(ver2):
            ver1_ver2_swapped = -1
            ver1, ver2 = ver2, ver1
        
        for i in range(len(ver1)):
            # Python's int can deal with leading zero natively
            v1, v2 = int(ver1[i]), int(ver2[i])
            if v1 > v2:
                return 1 * ver1_ver2_swapped
            elif v2 > v1:
                return -1 * ver1_ver2_swapped
        
        for j in range(i + 1, len(ver2)):
            if int(ver2[j]) != 0:
                return -1 * ver1_ver2_swapped
        
        return 0
