import numpy as np
import matplotlib.pyplot as plt

n = 10000


def sample(n, C=None, half_E=False, A_norm=False):
    A = np.random.exponential(7, n) if not A_norm else np.random.normal(7, 49, n) 
    B = np.random.normal(1, np.sqrt(4), n)
    C = np.random.choice([1, 2, 3], p=[1/6, 2/6, 3/6],
                         size=n) if C == None else C
    D = A + B + 30*np.random.choice([0, 1], p=[3/5, 2/5], size=n)
    E = B+20*C*(1/2 if half_E else 1)
    F = 3/2*D+E

    return np.array([A, B, C, D, E, F])


def plot(*samples, variables = [0,3,4,5]):
    for j, s in enumerate(zip(*samples)):
        if j not in variables: continue
        fig, axs = plt.subplots(1, len(s), sharex=True, sharey=True)
        for i, ax in enumerate(axs):
            ax.hist(s[i], bins=100, density = True)
        plt.show()


mi_sample = sample(n)
#print(mi_sample.mean(axis = 0))
#print(mi_sample.var(axis = 0))
# plot(sample(10000))
C_none = sample(n, C=None)
C_1 = sample(n, C=1)
C_2 = sample(n, C=2)
E_half = sample(n, half_E=True)
A_e = sample(n)
A_norm = sample(n, A_norm=True)

# plot(C_none, C_1, C_2)
# plot(C_none, E_half)
plot(A_e, A_norm)