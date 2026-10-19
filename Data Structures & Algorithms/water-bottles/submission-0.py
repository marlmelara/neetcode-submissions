class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange < 1:
            return numBottles

        if numBottles < 1:
            return 0

        totalBottles = numBottles
        curEmptyBottles = 0
        newBottles = 0

        while numBottles > 0:
            curEmptyBottles += numBottles
            newBottles = curEmptyBottles // numExchange # max number exchanged
            curEmptyBottles -= newBottles * numExchange
            totalBottles += newBottles
            numBottles = newBottles

        return totalBottles
