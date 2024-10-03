import math 
AB = int(input())
BC = int(input())
MBCradian = math.atan(AB/BC)
MBCdegree = math.degrees(MBCradian)
print(f"{MBCdegree:.0f}\u00b0")