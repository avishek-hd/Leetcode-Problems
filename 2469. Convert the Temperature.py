#2469. Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin= celsius+273.15
        fah=celsius*1.8+32
        res=[kelvin,fah]
        return res