import numpy as np
from sympy.functions.combinatorial.numbers import primepi
from matplotlib import pyplot as plt


def func_pi_function_additive():
    r"""
    Notation
    ----------
    * The :math:`i^{\mathrm{th}}` prime is denoted as :math:`p_i`. 
    * :math:`\pi(x)` denotes the prime counting function, i.e. the number of primes less than or equal to :math:`x`.

    Description
    -------------
    This script contains codes for testing the conjecture :math:`\pi(xy) >= \pi(x) + \pi(y)` for :math:`2 \le x \le 17, 2 \le y \le 1500`.
    
    We then generate plots for the following functions.

    Function 1: for :math:`y \ge 17`, we plot the term in brackets for :math:`(2y / \ln(y)) (1.0 - \ln(17) / \ln(17y))`

    .. math:: 
        1.0 - \ln(17) / \ln(17y)
    
    Function 2: for :math:`y >= 100`
    
    .. math:: 
        (2 - 1.26) y / \ln(y) - \pi(17)
    """

    # --------------------------------------------------------------------
    # Check the conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x <= 17, 2 <= y <= 1500
    nx_start = 2
    nx_end = 17
    ny_start = 2
    ny_end = 1500

    primepi_list = np.zeros(shape=(nx_end * ny_end,), dtype=float)
    for i in range(nx_end * ny_end):
        primepi_list[i] = primepi(i + 1)

    check = 0
    for i in range(nx_start, nx_end + 1):

        if check == 1:
            break
        print("x=", i)

        for j in range(i, ny_end + 1):
            if primepi(i * j) < primepi(i) + primepi(j):
                check = 1
                print(i,j)
                break
    
    if check == 0:
        print("The conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x <= 17, 2 <= y <= 1500 is true.")
    else:
        print("The conjecture Pi(xy) > Pi(x) + Pi(y) for 2 <=x <= 17, 2 <= y <= 1500 is false.")
    
    # --------------------------------------------------------------------
    # Plot the two functions
    nstart = 2
    nend = 2000

    y = np.arange(2, 2000, 1, dtype=float)
    logy = np.log(y)

    f1y = 1.0 - np.log(17.0) / np.log(17 * y)
    f2y = 0.14 * y / logy

    # Create subplots with 1 row and 2 columns
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # First plot
    axs[0].plot(y, f1y, '-r')
    axs[0].grid(True)
    axs[0].set_xlabel(r"$y$")
    axs[0].set_title(r"Plot of $f_1(y) = 1.0 - \text{ln}(17) / \text{ln}(17y)$")

    # Second plot
    axs[1].plot(y, f2y, '-b')
    axs[1].grid(True)
    axs[1].set_xlabel(r"$y$")
    axs[1].set_title(r"Plot of $f_2(y) = (2 - \alpha) y / \text{ln}(y) - \text{Pi}(17), \; \alpha=1.26$")

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":

    func_pi_function_additive()