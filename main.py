import numpy as np
import matplotlib.pyplot as plt

np.seterr(invalid='ignore') # one of tl or tr will probably be invalid, so i just dont really care that much

### USER INPUT PARAMETERS
sa = 3
sb = 3
sc = 3
d = 8

### MATH
o = d - sb
r1 = sa**2
r2 = sc**2
ix = (-r2 + r1 + o**2) / (2*o)
iy = np.sqrt(r1 - ix**2)
tl = np.sqrt(r2 - r1)
tr = np.sqrt(r1 - r2)
theta1 = (np.arcsin(iy/sa)*(180/np.pi) if ((o > tl) or (np.isnan(tl))) else 180-np.arcsin(iy/sa)*(180/np.pi)) # Use arcsin result unless offset surpasses some value (tl or tr), in which case use 180-arcsin. This is because after you cross this threshold, the required angle will be obtuse, but of course arcsin can only produce acute angles.
theta2 = (np.arcsin(iy/sc)*(180/np.pi) if ((o > tr) or (np.isnan(tr))) else 180-np.arcsin(iy/sc)*(180/np.pi))

### CURSOR OBJECT FOR GRAPHING
class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
    def line(self, length: int, angle: int):
        self.angle += angle # rotate cursor
        x1 = self.x
        y1 = self.y
        x2 = length * np.cos(np.radians(self.angle)) + self.x
        y2 = length * np.sin(np.radians(self.angle)) + self.y
        plt.plot([x1,x2],[y1,y2])
        self.x = x2 # move cursor to end of new line segment
        self.y = y2
    def report(self,precision=3,name="",showerrors=False):
        print("_________________")
        print("Cursor Report: " + "("+name+")")
        print("X: " + str(round(self.x,precision)))
        print("Y: " + str(round(self.y, precision)))
        print("Angle: " + str(round(self.angle,precision)))
        if showerrors:
            print("Errors: ",end="")
            nominal = (True if (round(self.x,precision) == d) and (round(self.y,precision) == 0) else False)
            if nominal:
                print("No errors exist.")
            else:
                print("Errors exist at this precision. If precision is a large number, try making it smaller. There is some margin of error within this program. Current precision: " + str(precision))
        print("_________________")
        
c = Cursor()

c.line(sa,theta1)
c.line(sb,-theta1)
c.line(sc,-theta2)
c.report(precision=3,name="Cursor",showerrors=True)

plt.grid()
plt.show()