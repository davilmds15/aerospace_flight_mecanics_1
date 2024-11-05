import numpy as np
import matplotlib.pyplot as plt
teta=np.linspace(-np.pi, np.pi,200);
teta2=np.linspace(-3*np.pi/4, 3*np.pi/4,200);
p=1;
e=0;r1=p/(1+e*np.cos(teta));
e=0.5;r2=p/(1+e*np.cos(teta));
e=0.9999;r3=p/(1+e*np.cos(teta));
e=1.2;r4=p/(1+e*np.cos(teta2));
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(teta, r1,label='e=0')
ax.plot(teta, r2,label='e=0.5')
ax.plot(teta, r3,label='e=0.9999')
ax.plot(teta2, r4,label='e=1.2')
ax.set_rmax(3)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
ax.legend()
plt.show()