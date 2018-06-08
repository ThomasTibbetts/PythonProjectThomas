import math
while True:
    print("Input radius.")
    radius = int(raw_input())
    volume = radius ** 3 * math.pi * 4/3
    print("The volume is " + str(volume))
