from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(scores, ages))

        def backtrack(i: int, chosen: List[int], total_score: int):
            if i == len(players):
                # print(chosen, total_score)
                return total_score

            conflict = False
            for player in chosen:
                # print(players[i], player)
                if players[i][0] > player[0] and players[i][1] < player[1]:
                    conflict = True
                    break
                if players[i][0] < player[0] and players[i][1] > player[1]:
                    conflict = True
                    break

            score1 = backtrack(i + 1, chosen, total_score)
            score2 = 0
            if not conflict:
                score2 = backtrack(
                    i + 1, chosen + [players[i]], total_score + players[i][0])
            return max(score1, score2)

        return backtrack(0, [], 0)

# WA: (2, 5) got picked?! (solved)
#
# [9,2,8,8,2]
# [4,1,3,3,5]
#
# 27

# TLE
#
# [764,364,527,589,88,297,96,991,778,54,536,785,257,923,184,436,847,36,793,881,589,545,986,851,585,693,150,602,356,617,672,513,687,558,682,635,696,726,944,639,709,580,35,237,425,763,775,182,820,408,532,59,660,731,712,130,323,398,366,620]
# [68,49,76,93,15,24,50,31,78,98,36,26,7,31,56,49,21,43,93,34,58,54,32,43,32,15,6,96,12,49,90,93,31,66,46,6,70,79,43,95,47,37,43,95,20,43,67,53,9,41,34,47,53,57,96,27,41,91,91,18]
