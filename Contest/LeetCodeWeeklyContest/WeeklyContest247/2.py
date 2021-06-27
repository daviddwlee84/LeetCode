from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def get_ring_of_layer(layer: int):
            min_i, min_j = layer, layer
            max_i, max_j = len(grid) - layer, len(grid[0]) - layer  # excluded

            # print((min_i, max_i), (min_j, max_j))

            i = min_i
            j = min_j

            ring = []

            # 1. from top to bottom
            while i < max_i:
                ring.append(grid[i][j])
                i += 1
            i -= 1

            # print(i, j)

            # 2. from left to right
            j += 1
            while j < max_j:
                ring.append(grid[i][j])
                j += 1
            j -= 1

            # print(i, j)

            # 3. from bottom to top
            i -= 1
            while i >= min_i:
                ring.append(grid[i][j])
                i -= 1
            i += 1

            # print(i, j)

            # 4. from right to left
            j -= 1
            while j > min_j:
                ring.append(grid[i][j])
                j -= 1

            # print(i, j)

            return ring

        def construct_rings_to_grid(rings: List[List[int]]) -> List[List[int]]:
            """
            From outer to inner
            """
            for layer, ring in enumerate(rings):

                min_i, min_j = layer, layer
                max_i, max_j = len(grid) - layer, len(grid[0]) - layer

                i = min_i
                j = min_j
                k = 0

                # 1. from top to bottom
                while i < max_i:
                    grid[i][j] = ring[k]
                    i += 1
                    k += 1
                i -= 1

                # 2. from left to right
                j += 1
                while j < max_j:
                    grid[i][j] = ring[k]
                    j += 1
                    k += 1
                j -= 1

                # 3. from bottom to top
                i -= 1
                while i >= min_i:
                    grid[i][j] = ring[k]
                    i -= 1
                    k += 1
                i += 1

                # 4. from right to left
                j -= 1
                while j > min_j:
                    grid[i][j] = ring[k]
                    j -= 1
                    k += 1

            return grid

        layer_count = min(len(grid), len(grid[0])) // 2

        final_rings = []

        for layer in range(layer_count):
            ring = get_ring_of_layer(layer)
            shift = len(ring) - k % len(ring)
            final_rings.append(ring[shift:] + ring[:shift])

        return construct_rings_to_grid(final_rings)
