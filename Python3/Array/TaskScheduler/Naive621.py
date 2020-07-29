from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        My solution is similar with this: https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
        """
        if n == 0:
            return len(tasks)

        count = Counter(tasks)
        # heapq.nsmallest(n, heap)

        answer = 0
        while count:
            # print(count)
            nlarge_tasks = heapq.nlargest(n + 1, count, key=count.get)
            for task in nlarge_tasks:
                count[task] -= 1
                if count[task] == 0:
                    count.pop(task)
                answer += 1

            if count:
                # print((n + 1) - len(nlarge_tasks))
                answer += (n + 1) - len(nlarge_tasks)  # idle

        return answer


def test(tasks, n):
    count = Counter(tasks)
    # heap = [(-freq, task) for task, freq in count.items()]
    # print(heapq.nsmallest(n, heap))
    heap = [(freq, task) for task, freq in count.items()]
    print(heapq.nlargest(n, heap))
    print(heap[-1])
    print(heap.pop())


def test2(tasks, n):
    count = Counter(tasks)
    print(heapq.nlargest(n, count, key=count.get))


if __name__ == "__main__":
    # test(["A", "A", "A", "B", "B", "B"], 2)
    # test(["A", "A", "A", "B", "B", "B"], 3)
    # test(["A", "A", "A", "B", "B", "B"], 0)
    # test(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)

    test2(["A", "A", "A", "B", "B", "B"], 2)
    test2(["A", "A", "A", "B", "B", "B"], 3)
    test2(["A", "A", "A", "B", "B", "B"], 0)
    test2(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
