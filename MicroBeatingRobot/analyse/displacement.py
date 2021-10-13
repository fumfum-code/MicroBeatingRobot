import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

df = pd.read_csv('~/Desktop/MicroBeatingRobot/MicroBeatingRobot/Databank/data_displacement.csv')


ax.set_title("displacement")
plt.plot(df.loc[1:,'step'], df.loc[1:,'displacement_x'], color = 'r', label = "x displacement")
plt.plot(df.loc[1:,'step'], df.loc[1:,'displacement_y'], color = 'b', label = "y displacement")
ax.legend(loc = 0)
fig.savefig("data.png")
plt.show()
