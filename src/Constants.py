import numpy as np
import sympy as sym


class NtConstants:
    """
    A class for useful number theory constants needed in the project.
    The constants are initialized and stored inside the class as attributes.
    ...

    Attributes
    ----------
    e : np.float64
        The constant e
    gamma : np.float64
        Euler-Mascheroni constant
    epowgamma : np.float64
        The constant e raised to the power Euler-Mascheroni constant

    Methods
    -------

    """
    
    def __init__(self):
        """
        Parameters
        ----------
        
        """

        self._e = np.exp(1.0)
        self._gamma = np.float64(sym.S.EulerGamma.n(20))
        self._epowgamma = self._e ** self._gamma


    @property
    def e(self):
        """
        The property 'e'.
        """
        return self._e
    
    @property
    def egamma(self):
        """
        The property 'gamma'.
        """
        return self._gamma
    
    @property
    def epowgamma(self):
        """
        The property 'epowgamma'.
        """
        return self._epowgamma