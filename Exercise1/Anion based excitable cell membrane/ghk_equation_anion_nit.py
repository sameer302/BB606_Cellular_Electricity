import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

nit_out = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
vm = 58*np.log10(1020/(50*nit_out + 280))
enit = 58*np.log10(20/nit_out)

plt.plot(nit_out, vm)
plt.plot(nit_out, enit)

for key in ["nernst", "ghk"] :
    x0 = 1

    if (key == "nernst") :
        y0 = 58*np.log10(1000/50*x0)
    else :
        y0 = 58*np.log10((1020)/(50*x0 + 280))

    plt.annotate(
        f"eqn = {key}",
        xy = (x0,y0),
        xytext = (x0 - 0.8, y0 - 10),
        arrowprops=dict(arrowstyle="->"),
        fontsize=9
    )

plt.xscale("log")
plt.xticks([0.1, 1, 10, 100],["0.1", "1", "10", "100"])
plt.xlabel("[NO3] (Outside)")
plt.ylabel("Vm (Membrane Potential)")
plt.title("Vm vs [NO3]")
plt.savefig("GHK_anion_nit_.png")
plt.show()

