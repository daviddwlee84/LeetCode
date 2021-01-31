from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def get_box_number(ball_number: int):
            """
            Equivalent to sum(map(int, str(ball_number)))
            """
            box_number = 0

            while ball_number:
                box_number += ball_number % 10
                ball_number //= 10

            return box_number

        boxes = Counter()
        for i in range(lowLimit, highLimit + 1):
            boxes[get_box_number(i)] += 1

        return boxes.most_common(1)[0][1]
