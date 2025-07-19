import numpy as np
from sympy.ntheory.generate import primepi
from matplotlib import pyplot as plt


if __name__ == "__main__":
    """
    This script contains codes for generating plots for the following functions.

    ----------
    Notation:
    The ith prime is denoted as p_i. 
    Pi(x) denotes the prime counting function, i.e. the number of primes less than or equal to x.

    
    Function 1: for :math:`y >=17`
    .. math:: 
        2y / ln(y) - 2y / ln(17y)
    
    Function 2: for :math:`y >= 100`
    .. math:: 
        (2 - 1.25506) y / ln(y) - Pi(17)
    """

    # Check the conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x,y <= 1500
    nstart = 2
    nend = 1500
    
    primepi_list = np.zeros(shape=(nend * nend,), dtype=float)
    for i in range(nend * nend + 1):
        if i % 1000 == 0:
            print("i=", i)
        primepi_list[i] = primepi(i)

    check = 0
    # for i in range(nstart, nend + 1):
    #     print("i=", i)
    #     for j in range(i, nend + 1):
    #         if primepi(i * j) <= primepi(i) + primepi(j):
    #             check = 1
    #             break
    
    if check == 0:
        print("The conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x,y <= 1500 is true.")
    else:
        print("The conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x,y <= 1500 is false.")


    # y = np.arange(2, 20000, 1, dtype=float)
    # logy = np.log(y)

    # f1y = 1.0 - np.log(17.0) / np.log(17 * y)
    # f2y = 7.0 * logy / y

    # # Plot the graphs
    # plt.figure()
    # plt.plot(y, f1y, '-r')
    # plt.plot(y, f2y, '-b')
    # plt.grid("on")
    # plt.xlabel("$y$")
    # plt.show()
