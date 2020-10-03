from typing import List
from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_time = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            name_time[name].append(t)

        answer = []
        for name, times in name_time.items():
            times.sort()
            for i in range(2, len(times)):
                H, M = times[i].split(':')
                preH, preM = times[i - 2].split(':')

                if H == preH or (int(H) - int(preH) == 1 and int(M) <= int(preM)):
                    answer.append(name)
                    break

        return sorted(answer)

# WA (solved)
# ["a","a","a","a","a","b","b","b","b","b","b"]
# ["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"]
# ["a"]

# WA (solved)
# ["a","a","a","a","b","b","b","b","b","b","c","c","c","c"]
# ["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]
# []
