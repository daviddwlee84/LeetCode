class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        bottleLeft = 0
        while numBottles >= numExchange:
            canExchange = numBottles // numExchange
            bottleLeft = numBottles % numExchange
            totalBottles += canExchange
            numBottles = canExchange + bottleLeft

        return totalBottles
