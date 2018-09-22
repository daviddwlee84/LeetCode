class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = height

        maxAreaTemp = 0

        front = 0
        end = len(height)-1

        while end > front:
            # Update Max Area
            if maxAreaTemp < self.calcArea(front, end):
                maxAreaTemp = self.calcArea(front, end)
            # Update pointer
            if height[front] > height[end]:
                end -= 1
            else:
                front += 1

        return maxAreaTemp
        
        
    def calcArea(self, idx1, idx2):
        return abs(idx2 - idx1) * min(self.height[idx1], self.height[idx2])