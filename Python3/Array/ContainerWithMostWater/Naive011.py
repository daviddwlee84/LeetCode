class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = height

        maxAreaTemp = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if self.calcArea(i, j) > maxAreaTemp:
                    maxAreaTemp = self.calcArea(i, j) 
        return maxAreaTemp
        
        
    def calcArea(self, idx1, idx2):
        return abs(idx2 - idx1) * min(self.height[idx1], self.height[idx2])