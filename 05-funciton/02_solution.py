import math 

def circle_stats(redius):
    area = math.pi * redius **2 
    cirumference = 2 * math.pi * redius 
    return {area, cirumference}


area, cirumference  = circle_stats(3)
print("Area:",area, "Circumference:",cirumference)