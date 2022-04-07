import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

os.chdir('Mini 3')

data = pd.read_csv("1000_standard.csv")
data_B0 = pd.read_csv("1000_B0.csv")
data_D0 = pd.read_csv("1000_D0.csv")
#labels = data.columns()[1:]
#data = data.to_numpy().T

def plot_relation(samples: pd.DataFrame, filename, nrows = 3):
    """
    samples shape = MxN, N samples and M variables
    """

    variable_names = list(samples.columns)[1:]

    N,M = samples.shape
    M -= 1
    ncols = int(np.ceil(M*(M-1)/2/nrows))

    fig, axs = plt.subplots(nrows = nrows, ncols = ncols) 
    plot_number = 0
    for i in range(M-1):
        for j in range(i+1,M):
            #print(plot_number, int(plot_number/nrows), plot_number%nrows)
            ax = axs[plot_number//ncols, plot_number%ncols]
            ax.plot(samples.iloc[:,i+1], samples.iloc[:,j+1], '.', alpha = 0.3, markersize = 2)
            ax.set_title(f"{variable_names[i]} vs. {variable_names[j]} {np.cov(samples.iloc[:,[i+1,j+1]].T)[0,1]:.4}")
            plot_number += 1
    plt.suptitle(filename)
    plt.savefig(f"{filename}_relation.png")

def plot_dist(samples, filename, nrows = 3):
    
    variable_names = list(samples.columns)[1:]

    N,M = samples.shape
    M -= 1
    ncols = int(np.ceil(M/nrows))

    fig, axs = plt.subplots(nrows = nrows, ncols = ncols) 
    for i in range(M):
        ax = axs[i//ncols, i%ncols]
        ax.hist(samples.iloc[:,i+1], bins = 50)
        ax.set_title(variable_names[i])

    plt.suptitle(filename)
    plt.savefig(f"{filename}_distributions.png")

def load_plot_save_img(filename):
    samples = pd.read_csv(f"{filename}.csv")
    plot_dist(samples, filename)
    plot_relation(samples, filename)
    return samples

load_plot_save_img("1000_standard")
load_plot_save_img("1000_B0")
load_plot_save_img("1000_D0")



