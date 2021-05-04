from typing import List
import collections


class WordFilter:

    def __init__(self, words: List[str]):
        self.pref = collections.defaultdict(set)
        self.suff = collections.defaultdict(set)
        seen = set()
        for i in range(len(words) - 1, -1, -1):
            w = words[i]
            if w in seen:
                continue
            seen.add(w)
            for j in range(len(w) + 1):
                self.pref[w[:j]].add(i)
                self.suff[w[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pref[prefix]
        b = self.suff[suffix]
        x = a & b
        return max(x) if x else -1

# class WordFilter:
#
#     def __init__(self, words: List[str]):
#         self.suffix=collections.defaultdict(set)
#         self.prefix=collections.defaultdict(set)
#         self.index={}
#         for j in range(len(words)):
#             for i in range(len(words[j])):
#                 self.suffix[words[j][i:]].add(words[j])
#                 self.prefix[words[j][:i+1]].add(words[j])
#             self.index[words[j]]=j
#
#     def f(self, prefix: str, suffix: str) -> int:
#
#         prefix_set=set()
#         suffix_set=set()
#         if prefix in self.prefix:
#             prefix_set=self.prefix[prefix]
#
#         if suffix in self.suffix:
#             suffix_set=self.suffix[suffix]
#
#         intersection=prefix_set.intersection(suffix_set)
#
#         maximum=-1
#         for word in intersection:
#
#             if self.index[word] > maximum:
#                 maximum=self.index[word]
#
#         return maximum
