import numpy as np
import matplotlib.pyplot as plt
import scipy 

def pdf(x):
    a1 = 1 / (np.sqrt(2 * np.pi)) * np.exp(-np.power((x-2),2))
    a2 = 1 / (np.sqrt(2 * np.pi)) * np.exp(-np.power((x+1),2))
    return a1 + a2

def main():
    xi = np.random.uniform(low=-5, high=5, size=[10000])
    ui = np.random.uniform(low=0, high=1, size=[10000])
    samples = xi[ui < pdf(xi)]


    x = np.linspace(-5,5,1000)
    Z, _ = scipy.integrate.quad(pdf,0,5)
    plt.plot(x, pdf(x)/(2*Z))

    plt.hist(samples,bins=50,density=True, edgecolor ='w')
    plt.savefig("1.jpg")
    plt.cla()


if __name__ == "__main__":
    main()