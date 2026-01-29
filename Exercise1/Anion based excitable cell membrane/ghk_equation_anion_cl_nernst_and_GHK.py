import numpy as np # math + arrays
import matplotlib.pyplot as plt # plotting

cl_out = np.linspace(0.1, 1000, 10000) # 10,000 points from 1 to 1000
# vm = 58*np.log10((1045)/(30 + 9*cl_out)) # original GHK equation, this will show deviation between nernst and GHK even for larger concentrations
vm = 58*np.log10((1045)/(30 + 9*cl_out)) - 58*np.log10(23) 
'''
This one will make sure that the two curves coincide for larger values of concentration as we subtracted the deviation term. 
For Nitrate ion this deviation term is very small hence we don't see deviation there. 
Also this deviation term is constant for a given set of internal concentrations and how did we get this value?
We know that at very high concentration of external anion, both GHK and Nernst should give same result. So we can calculate the value of 
membrane potential at very high concentration using both equations and the difference will be our deviation term.
So for cl- ion, at very high concentration (say 1000 mM):
Using GHK: Vm = 58 * log10( (1045) / (30 + 9*1000) ), neglecting 30 here = 58 * log10(1045/9000) ~ 58 * log10(116/1000) ~ 58 * log10(5 * 23 / 1000) = 58 * (log10(5/1000)) + 58 * log10(23)
Using Nernst: Vm = 58 * log10(5/1000)
So the deviation term = + 58 * log10(23)
We subtract this deviation term from the GHK equation to align both curves at high concentration.
 '''
ecl = 58*np.log10(5/cl_out)

plt.plot(cl_out, vm)
plt.plot(cl_out, ecl)

for key in ["nernst", "ghk"] :
    x0 = 1
    if(key == "nernst"):
        y0 = 58*np.log10(5/x0)
    else:
        y0 = 58*np.log10((1045)/(30 + 9*x0)) - 58*np.log10(23)

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
plt.savefig("GHK_anion_cl_9_no_deviation_nernst_and_GHK.png")
plt.show()

