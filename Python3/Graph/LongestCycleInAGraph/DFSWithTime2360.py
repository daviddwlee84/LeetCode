from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        longest_cycle_length = -1

        # Use this to calculate length
        time_step = 1
        # 0 means not visited
        node_visited_at_time = [0] * len(edges)

        for current_node in range(len(edges)):
            if node_visited_at_time[current_node] > 0:
                # Already visited
                continue

            start_time = time_step
            node = current_node
            # -1 means end of a path
            while node != -1 and node_visited_at_time[node] == 0:
                node_visited_at_time[node] = time_step
                time_step += 1
                # Going to next node
                node = edges[node]

            # node != -1 means found cycle
            if node != -1 and node_visited_at_time[node] >= start_time:
                longest_cycle_length = max(
                    longest_cycle_length, time_step - node_visited_at_time[node])

        return longest_cycle_length
