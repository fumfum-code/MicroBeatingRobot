import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import particle_4 as c


fig, ax = plt.subplots()
"""
df = pd.read_csv(f'~/Desktop/MicroBeatingRobot/MicroBeatingRobot/Databank/data_angle_k={c.K_star}_f={c.frec}.csv')


ax.set_title("angle")
plt.plot(df.loc[1:,'step'], df.loc[1:,'angle1'], color = 'r', label = "angle1")
plt.plot(df.loc[1:,'step'], df.loc[1:,'angle2'], color = 'b', label = "angle2")
ax.legend(loc = 0)
fig.savefig(f"analyse/angle_k={c.K_star}.png")
plt.show()

df = pd.read_csv(f'~/Desktop/MicroBeatingRobot/MicroBeatingRobot/Databank/data_arm_k={c.K_star}_f={c.frec}.csv')


fig, ax = plt.subplots()
ax.set_title("arm")
plt.plot(df.loc[1:,'step'], df.loc[1:,'arm1'], color = 'r', label = "arm1")
plt.plot(df.loc[1:,'step'], df.loc[1:,'arm2'], color = 'b', label = "arm2")
plt.plot(df.loc[1:,'step'], df.loc[1:,'arm3'], color = 'g', label = "arm3")
ax.legend(loc = 0)
fig.savefig(f"analyse/armlen_k={c.K_star}_f={c.frec}.png")
plt.show()
"""
df = pd.read_csv(f'~/Desktop/MicroBeatingRobot/MicroBeatingRobot/Databank/data_displacement_K={c.K_star}_f={c.frec}.csv')


fig, ax = plt.subplots()
ax.set_title("displacement")
plt.plot(df.loc[1:,'step'], df.loc[1:,'displacement_x'], color = 'r', label = "x displacement")
plt.plot(df.loc[1:,'step'], df.loc[1:,'displacement_y'], color = 'b', label = "y displacement")
ax.legend(loc = 0)
fig.savefig(f"analyse/data_displacement_k={c.K_star}_f={c.frec}.png")
plt.show()
