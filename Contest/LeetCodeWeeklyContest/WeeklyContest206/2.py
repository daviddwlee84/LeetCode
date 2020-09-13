from typing import List
from itertools import combinations


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref_dicts = [
            {person: i for i, person in enumerate(pref)}
            for pref in preferences
        ]

        def unhappy(x: int, y: int, u: int, v: int) -> bool:
            if pref_dicts[x][u] < pref_dicts[x][y] and pref_dicts[u][x] < pref_dicts[u][v]:
                print(x, y, u, v)
                return True
            return False

        pair_dict = {}
        for x, y in pairs:
            pair_dict[x] = y
            pair_dict[y] = x

        unhappy_friend = set()
        for x in range(n):
            y = pair_dict[x]
            happy = True
            for u in pair_dict:
                if u != x and u != y:
                    v = pair_dict[u]
                    if unhappy(x, y, u, v):
                        happy = False
                        break
            if not happy:
                unhappy_friend.add(x)

        return len(unhappy_friend)
