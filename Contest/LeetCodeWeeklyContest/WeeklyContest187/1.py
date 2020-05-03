from typing import List

# https://campus.datacamp.com/courses/python-data-science-toolbox-part-2/using-iterators-in-pythonland?ex=9


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        in_set, out_set = list(map(lambda x: set(x), zip(*paths)))
        answer = out_set - in_set
        return answer.pop()
