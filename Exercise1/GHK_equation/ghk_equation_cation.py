import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

k_out = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
alphas = [0.0001, 0.001, 0.01, 0.03, 0.1, 0.2]

for alpha in alphas:
    vm = 58*np.log10((k_out + alpha*120)/(140 + alpha*12))
    plt.plot(k_out, vm, label=f"alpha = {alpha}")

    # label on curve
    x0 = 0.1
    y0 = 58*np.log10((x0 + alpha*120)/(140 + alpha*12))
    
    plt.annotate(
    f"alpha = {alpha}",
    xy=(x0, y0),
    xytext=(x0, y0 + 10),
    arrowprops=dict(arrowstyle="->"),
    fontsize=9
    )

plt.xscale("log")
plt.xticks([0.1, 1, 10, 100], ["0.1", "1", "10", "100"]) # here if we didnt write the second array then the ticks will be named as 10^-1, 10^0, 10^1, 10^2
plt.xlabel("[K] (Outside)")
plt.ylabel("Vm (Membrane Potential)")
plt.title("Vm vs [K] for different alpha values")
plt.savefig("GHK_cation.png")
plt.show()

