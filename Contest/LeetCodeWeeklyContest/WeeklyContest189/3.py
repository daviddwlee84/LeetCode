from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companySets = [set(companies) for companies in favoriteCompanies]
        answer = [i for i, cmpSet in enumerate(companySets) if not any(
            [cmpSet.issubset(otherCmpSet) for otherCmpSet in companySets[:i] + companySets[i+1:]])]

        return answer
