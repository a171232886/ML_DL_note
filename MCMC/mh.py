import numpy as np
import matplotlib.pyplot as plt
import scipy 

def pdf(x):
    a1 = 1 / (np.sqrt(2 * np.pi)) * np.exp(-np.power((x-2),2))
    a2 = 2 / (np.sqrt(2 * np.pi)) * np.exp(-np.power((x+1),2))
    a3 = 1 / (np.sqrt(2 * np.pi)) * np.exp(-np.power((x+3),2))
    return a1 + a2 + a3

def q(x, sigma):
    return 1 / (np.sqrt(2 * np.pi)) / sigma * np.exp(-np.power(x/sigma,2))

def judge_steady(err, i, errs):
    # 判断稳态
    errs[i % 5] = np.abs(err)
    if np.mean(errs) < 0.05:
        return True
    else:
        return False



def main(k = 5, sigma = 3):
    xi = 0
    num = 0
    errs = np.ones([5])
    for i in range(100000):
        xj = np.random.normal(loc=xi, scale=sigma, size=[1])
        uj = np.random.uniform(low=0, high=k*q(xj,sigma), size=[1])

        if uj < pdf(xj):
            xi = xj

        err = xi - xj    
        if judge_steady(err, i, errs):
            break


    samples = []    
    for j in range(10000):
        xj = np.random.normal(loc=xi, scale=sigma, size=[1])
        uj = np.random.uniform(low=0, high=k*q(xj,sigma), size=[1])

        if uj < pdf(xj):
            samples.append(xj[0])


    x = np.linspace(-10,10,10000)
    Z, _ = scipy.integrate.quad(pdf,-10,10)
    plt.plot(x, pdf(x)/Z)
    plt.plot(x, k*q(x,sigma))
    plt.plot(x, k * 1 / (np.sqrt(2 * np.pi)) / sigma * np.exp(-np.power((x-xj)/sigma,2)))

    

    plt.hist(samples,bins=50,density=True, edgecolor ='w')
    plt.savefig("1.jpg")
    plt.cla()


if __name__ == "__main__":
    main()    