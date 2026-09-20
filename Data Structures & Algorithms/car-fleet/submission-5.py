class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPosSpeed = [(p, s) for (p, s) in zip(position, speed)]
        carFleet = []

        carPosSpeed.sort(reverse = True)

        for p, s in carPosSpeed:
            timeToDestination = (target - p) / s
            carFleet.append(timeToDestination)
            while len(carFleet) >= 2 and carFleet[-1] <= carFleet[-2]:
                carFleet.pop()

        return len(carFleet)