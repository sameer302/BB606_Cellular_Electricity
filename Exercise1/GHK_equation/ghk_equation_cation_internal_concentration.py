import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

k_in = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
alpha = 0.03

vm = 58*np.log10((3.5 + alpha*120)/(k_in + alpha*12))
ek = 58*np.log10(3.5/k_in)
plt.plot(k_in, vm, label="GHK")
plt.plot(k_in, ek, label="Nernst")

plt.xscale("log")
plt.xticks([0.1, 1, 10, 100], ["0.1", "1", "10", "100"]) # here if we didnt write the second array then the ticks will be named as 10^-1, 10^0, 10^1, 10^2
plt.xlabel("[K] (inside)")
plt.ylabel("Vm (Membrane Potential)")
plt.title("Vm vs [K] for GHK and Nernst")
plt.savefig("GHK_cation_new.png")
plt.show()

