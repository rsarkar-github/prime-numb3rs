from src.Constants import NtConstants
from src.PrimorialUtils import *
from src.GeneralUtils import *
from src.TruncatedSum import *
from matplotlib import pyplot as plt


if __name__ == "__main__":
    """
    This script contains codes for experiments for testing the conjecture for primorial primes.
    """

    # Initialize the class of constants
    consts = NtConstants()
    
    # Set m values, nproc
    mstart = 2
    mend = 1000
    nproc = 16

    mlist = np.arange(mstart, mend + 1, 1)


    # Compute rhs of the conjecture
    primorials_log = range_primorials_log(mstart=mstart, mend=mend)
    primorials_log2 = np.log(primorials_log)
    rhs = primorials_log * primorials_log2

    # Compute lhs of the conjecture
    primes_log = range_primes_log(mstart=mstart, mend=mend)
    primes = np.exp(primes_log)
    lhs = primes * primes_log

    primorials_log_ub = primes_log * mlist

    # Plot the graphs
    plt.figure()
    plt.plot(mlist, lhs, '-r')
    plt.plot(mlist, rhs, '-k')
    # plt.plot(mlist, primorials_log, '-b.')
    # plt.plot(mlist, primes_log * mlist, '-g.')
    # plt.plot(mlist, primorials_log * np.log(primorials_log_ub), '-g.')
    plt.grid("on")
    plt.xlabel("m")
    plt.legend(["p log(p)", "log log(n) log(n)", "n", "nm"])
    plt.show()
