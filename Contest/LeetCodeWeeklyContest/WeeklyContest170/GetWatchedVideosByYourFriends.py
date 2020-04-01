from collections import deque, Counter, defaultdict
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set([id])
        queue = deque([(id, 0)])
        count = defaultdict(int)
        while queue:
            i, lvl = queue.pop()
            if lvl > level:
                break
            elif lvl == level:
                for video in watchedVideos[i]:
                    count[video] += 1
            else:
                for friend in friends[i]:
                    if friend not in visited:
                        queue.appendleft((friend, lvl + 1))
                        visited.add(friend)

        # sorted the result
        temp = defaultdict(list)
        cntSet = set()
        for video, cnt in count.items():
            cntSet.add(cnt)
            temp[cnt].append(video)
        ans = []
        for cnt in sorted(list(cntSet)):
            ans.extend(sorted(temp[cnt]))
        return ans
