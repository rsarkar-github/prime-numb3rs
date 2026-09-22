from src.Constants import NtConstants
from src.PrimorialUtils import *
from src.GeneralUtils import *
from src.TruncatedSum import *
from matplotlib import pyplot as plt


def func_primorial_raw_bounds():
    r"""
    Notation
    ---------
    * The :math:`i^{\mathrm{th}}` prime is denoted as :math:`p_i`.
    * :math:`\mathrm{primorial}(i)` is the :math:`i^{\mathrm{th}}` primorial number, obtained as :math:`p_1 ... p_i`.
    * :math:`\sigma(n)` is the sum of divisors of :math:`n`, and :math:`\omega(n)` is the number of unique primes of :math:`n`.

    Description
    ------------

    This script contains codes for plotting the LHS and RHS of the conjecture for primorial primes.
    The conjecture is

    .. math::
        \sigma(n)/n \le e^{\gamma} \sum_{k=0}^{\omega(n)} \frac{1}{k!} (\ln \ln \ln n)^k, \quad n \ge 5040.

    

    This script plots the following functions:

    Function 1 (LHS):

    .. math:: 
        e^{-\gamma}  \sigma(\mathrm{primorial}(m)) / \mathrm{primorial}(m)
    
    Function 2 (LHS Upper Bound):

    .. math:: 
        e^{-\gamma + \sum_{k=1}^{m} p_k^{-1}}
    
    Function 3 (RHS):

    .. math:: 
        \sum_{k=0}^{m} \frac{1}{k!} (\ln \ln \ln (\mathrm{primorial}(m)))^k
    
    Function 4 (RHS Upper Bound):

    .. math:: 
        \ln \ln (\mathrm{primorial}(m))
    
    Function 5 (RHS Lower Bound):

    .. math:: 
        \ln \ln (\mathrm{primorial}(m)) (1.0 - \frac{1}{(m+1)!} (\ln \ln \ln (\mathrm{primorial}(m)))^{m+1})
    
    """

    # Initialize the class of constants
    consts = NtConstants()
    
    # Set m values, nproc
    mstart = 2
    mend = 10
    nproc = 16

    mlist = np.arange(mstart, mend + 1, 1)

    # Compute lhs and lhs upper bound of the conjecture
    lhs = range_primorials_sigma_by_n(mstart=mstart, mend=mend) / consts.epowgamma
    lhs_ub = np.exp(sum_range_primorials_inverse(mstart=mstart, mend=mend)) / consts.epowgamma

    # Compute rhs and rhs upper bound of the conjecture
    rhs = range_primorials_truncated_sum(mstart=mstart, mend=mend, nproc=nproc)
    rhs_ub = np.log(range_primorials_log(mstart=mstart, mend=mend))

    print(rhs / lhs)

    # Compute rhs lower bound of the conjecture
    primorials_log3 = np.log(np.log(range_primorials_log(mstart=mstart, mend=mend)))
    temp_arr = primorials_log3 * 0.0 + 1.0
    for i in range(mstart, mend + 1):
        x = primorials_log3[i - mstart]
        fac = 1.0
        for j in range(i+1):
            fac *= x / (j + 1)
        temp_arr[i - mstart] = fac

    rhs_lb = np.log(range_primorials_log(mstart=mstart, mend=mend)) * (1.0 - temp_arr)

    # Plot the two functions
    plt.figure()
    plt.plot(mlist, lhs, '-r', linewidth= 1)
    plt.plot(mlist, 0.85 * lhs_ub, '--r', linewidth= 1)
    plt.plot(mlist, rhs, '-g', linewidth= 1)
    plt.plot(mlist, rhs_ub, '--g', linewidth= 1)
    plt.plot(mlist, rhs_lb, '-.g', linewidth= 1)
    plt.grid("on")
    plt.xlabel(r"$m$")
    plt.legend(
        [
            r"$e^{-\gamma} \sigma(n) / n$", 
            r"$e^{-\gamma + \sum_{k=1}^{m} p_k^{-1}}$", 
            r"$\sum_{k=0}^{m} \frac{1}{k!} (\ln \ln \ln n)^k$", 
            r"$\ln \ln n$",
            r"$\ln \ln n (1.0 - \frac{1}{(m+1)!}(\ln \ln \ln n)^{m+1})$"
        ]
    )
    plt.title(r"$n=p_1 p_2 ... p_m$")
    plt.show()


if __name__ == "__main__":
    
    func_primorial_raw_bounds()