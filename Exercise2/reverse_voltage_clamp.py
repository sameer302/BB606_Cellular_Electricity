import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Constants
# -----------------------------
gK_max = 30.0          # mS/cm^2
EK = -77.0             # mV (typical squid value)
Vr = -68.0             # resting membrane potential (mV)
n0 = 0.24              # initial value of n
dt = 0.01              # ms
t_max = 8.0            # ms
time = np.arange(0, t_max + dt, dt)

# Clamp voltages
Vm_values = np.arange(-50, 70, 20)  # -50 to +60 in steps of 20

# -----------------------------
# Hodgkin-Huxley rate functions
# -----------------------------
def alpha_n(v):
    return 0.01*(10 - v)/(np.exp((10 - v)/10) - 1)

def beta_n(v):
    return 0.125*np.exp(-v/80)

# -----------------------------
# Simulation
# -----------------------------
plt.figure(figsize=(12, 8))

for Vm in Vm_values:
    
    v = Vm - Vr  # voltage relative to rest
    
    an = alpha_n(v)
    bn = beta_n(v)
    
    tau_n = 1.0 / (an + bn)
    n_inf = an / (an + bn)
    
    # n(t)
    n_t = n_inf - (n_inf - n0)*np.exp(-time/tau_n)
    
    # gK(t)
    gK_t = gK_max * n_t**3
    
    # iK(t)
    iK_t = gK_t * (Vm - EK)
    
    # Plot gK
    plt.subplot(4,1,1)
    plt.plot(time, gK_t, label=f"Vm={Vm} mV")
    plt.ylabel("gK (mS/cm^2)")
    plt.title("Potassium Conductance gK(t)")
    
    # Plot iK
    plt.subplot(4,1,2)
    plt.plot(time, iK_t, label=f"Vm={Vm} mV")
    plt.ylabel("iK (uA/cm^2)")
    plt.xlabel("Time (ms)")
    plt.title("Potassium Current iK(t)")

    # Plot nk
    plt.subplot(4,1,3)
    plt.plot(time, n_t, label=f"Vm={Vm} mV")
    plt.ylabel("n(t)")
    plt.xlabel("Time (ms)")
    plt.title("Potassium Activation Variable n(t)")

    # Plot nk**4
    plt.subplot(4,1,4)
    plt.plot(time, n_t**4, label=f"Vm={Vm} mV")
    plt.ylabel("n(t)^4")
    plt.xlabel("Time (ms)")
    plt.title("Potassium Activation Variable n(t)^4")

plt.subplot(4,1,1)
plt.legend(loc="upper right")
plt.subplot(4,1,2)
plt.legend(loc="upper right")
plt.subplot(4,1,3)
plt.legend(loc="upper right")
plt.subplot(4,1,4)
plt.legend(loc="upper right")

plt.tight_layout()
plt.savefig("reverse_voltage_clamp_nplot.png")
plt.show()