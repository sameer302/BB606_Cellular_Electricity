import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

cl_out = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
k = 9
vm = 58*np.log10((1000 + k*5)/(30 + k*cl_out))
ecl = 58*np.log10(5/cl_out)

plt.plot(cl_out, vm)
plt.plot(cl_out, ecl)

for key in ["nernst", "ghk"] :
    x0 = 1
    if(key == "nernst"):
        y0 = 58*np.log10(5/x0)
    else:
        y0 = 58*np.log10((1000 + k*5)/(30 + k*x0))

    plt.annotate(
        f"eqn = {key}",
        xy = (x0, y0),
        xytext = (x0 - 0.8, y0 - 15),
        arrowprops=dict(arrowstyle="->"),
        fontsize=9
    )


plt.xscale("log")
plt.xticks([0.1, 1, 10, 100],["0.1", "1", "10", "100"])
plt.xlabel("[Cl] (Outside)")
plt.ylabel("Vm (Membrane Potential)")
plt.title("Vm vs [Cl]")
plt.savefig("GHK_anion_cl_9_updated.png")
plt.show()

