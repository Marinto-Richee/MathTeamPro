import math
radius=float(input("Enter the radius of the cone: "))
height=float(input("Enter the height of the cone: "))
volume_cone=math.pi*(radius**2)*(height/3)
print("\n\n2Cone dimensions\nradius=\t{}\nHeight=\t{}\nvolume=\t{:.3f}\n".format(radius,height,volume_cone)) 