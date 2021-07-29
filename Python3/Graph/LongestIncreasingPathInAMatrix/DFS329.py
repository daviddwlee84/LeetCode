from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        def dfs(i: int, j: int) -> int:
            ans = 1
            if not dp[i][j]:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < M and 0 <= y < N:
                        if matrix[x][y] > matrix[i][j]:
                            ans = max(ans, dfs(x, y) + 1)
                dp[i][j] = ans
            return dp[i][j]

        ans = 0
        for i in range(M):
            for j in range(N):
                ans = max(ans, dfs(i, j))

        return ans

# Runtime: 448 ms, faster than 80.21% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 15 MB, less than 89.85% of Python3 online submissions for Longest Increasing Path in a Matrix.


# class Solution {
# private:
#     vector<vector<int>> dp;
#     int M;
#     int N;
#     const int dirs[4][2] = { {1, 0}, {-1, 0}, {0, -1}, {0, 1} };
# public:
#     int longestIncreasingPath(vector<vector<int>>& matrix) {
#         this->M = matrix.size();
#         this->N = matrix[0].size();
#         dp = vector<vector<int>>(M, vector<int>(N));
#
#         int ans = 0;
#         for (int i = 0; i < M; i++) {
#             for (int j = 0; j < N; j++) {
#                 ans = max(ans, dfs(matrix, i, j));
#             }
#         }
#         return ans;
#     }
#
#     int dfs(vector<vector<int>>& matrix, int i, int j) {
#         if (dp[i][j]) return dp[i][j];
#         int ans = 1;
#         for (auto& d : dirs) {
#             const int x = i + d[0];
#             const int y = j + d[1];
#             if (x < 0 || y < 0 || x >= M || y >= N) continue;
#             if (matrix[x][y] > matrix[i][j]) {
#                 ans = max(ans, dfs(matrix, x, y) + 1);
#             }
#         }
#         dp[i][j] = ans;
#         return ans;
#     }
# };
