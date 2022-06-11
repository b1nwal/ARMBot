import matplotlib.pyplot as plt
import numpy as np

x,y = 1,1
a,b = 4,3
c = np.sqrt(x**2 + y**2)

if x <= 0 or y <= 0 or c > a+b:
  print("ERR: Coordinates out of range of end effector.")

B = (np.arccos((a**2+c**2-b**2)/(2*a*c)) - np.arctan(y/x)) * -1
C = np.pi - np.arccos((a**2 + b**2 - c**2)/(2*a*b)) + B

print(np.degrees(B),np.degrees(C))

fig = plt.figure("Inverse Kinematics 2D Test Space")
ax = plt.gca()
ax.set_aspect("equal")
ax.grid()
ax.set_ylim([-10, 10])
ax.set_xlim([-10, 10])
ax.plot(x, y, marker="o", markersize=12, markerfacecolor="green")
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
fig.show()

def plot_point(point, angle, length):
     x, y = point
     endy = y + length * np.sin(angle)
     endx = x + length * np.cos(angle)
     ax.plot([x, endx], [y, endy], color="blue")
     fig.show()
     return round(endx,3),round(endy,3)

print(plot_point(plot_point((0,0),B,a),C,b))
