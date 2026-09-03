import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width = None) -> float:
        if width:
            area = length * width
        else:
            area = round((length ** 2) * math.pi, 2)
        
        return area
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
