import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

cl_out = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
k = 4
vm = 58*np.log10((1000 + k*5)/(30 + k*cl_out))

plt.plot(cl_out, vm)
plt.xscale("log")
plt.xticks([0.1, 1, 10, 100],["0.1", "1", "10", "100"])
plt.xlabel("[Cl] (Outside)")
plt.ylabel("Vm (Membrane Potential)")
plt.title("Vm vs [Cl]")
plt.savefig("GHK_anion_cl_4.png")
plt.show()

