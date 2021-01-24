class Solution:
    def maximumTime(self, time: str) -> str:
        # hour_ten = int(time[0]) * 10 if time[0] != '?' else 0
        # hour_one = int(time[1]) * 10 if time[1] != '?' else 0
        # minute_ten = int(time[3]) * 10 if time[3] != '?' else 0
        # minute_ten = int(time[4]) * 10 if time[4] != '?' else 0

        # "2?:?0"
        # "0?:3?"
        # "1?:22"
        # "??:3?"
        answer = ''
        if time[0] == '?':
            if time[1] != '?' and int(time[1]) >= 4:
                answer += '1'
            else:
                answer += '2'
        else:
            answer += time[0]

        if time[1] == '?':
            if int(answer[0]) > 1:
                answer += '3'
            else:
                answer += '9'
        else:
            answer += time[1]

        answer += ':'

        if time[3] == '?':
            answer += '5'
        else:
            answer += time[3]

        if time[4] == '?':
            answer += '9'
        else:
            answer += time[4]

        return answer
