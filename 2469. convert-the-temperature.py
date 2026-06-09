class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ls=[]
        K=celsius+273.15
        F=celsius*1.80+32.00
        ls.append(K)
        ls.append(F)
        return ls
