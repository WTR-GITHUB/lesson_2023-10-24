# 3) Create lamba functions for these caclulations:
#    - calculate lenght of circle
#    - calculate average speed of the car (knowing distance and time passed
#      to drive that distance)
# - calculate percentage of value if 5500 is equal 200%
import math
cicrle_lenght = lambda diameter: math.pi*diameter
print(cicrle_lenght(10))

average_speed = lambda distance, time_pass: distance/time_pass
print(average_speed(28, 2.5))

value_percentage = lambda val_user: (val_user * 200) / 5500
print("Value in percents: {:.0%}".format(round(value_percentage(50),1)))

