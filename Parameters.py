import numpy as np


class Parameters:
    """
    This class gathers all necessary parameters for running the code. Such parameters are:

        * R ---------------->  Universal gas constant [float];
        * Tc ---------------> Critical temperature [array - float];
        * Pc ---------------> Critical pressure [array - float];
        * w ----------------> Acentric factor[array - float];
        * Kij --------------> Binary interaction parameter [array - float];
        * a ----------------> Antoine parameters of components [array - float];
        * Psat -------------> Saturation pressure by Antoine equation [array - float]

    OBS: For add a new system, the users must add the information here, creating a
    new method with the name of the system.
    """
    def __init__(self):
        pass

    @staticmethod
    def Propane_Butane(T):
            R          = 8.314  # ----------------------------------------> Gas constant (J*mol-1*K-1)
            Tc         = np.array([369.8, 425.1])  # --------------------> Critical temperature (K)
            Pc         = np.array([4248000, 3796000])  # ----------------> Critical pressure (Pascal)
            w          = np.array([0.152, 0.2])  # -----------------------> acentric factor (dimensionless)
            Kij        = np.array([0.0008]) #---------------------------> binary interaction parameter
            a          = np.array([[3.98292, 819.296, -24.417],[4.35576, 1175.581, -2.071]]) #----------> Antoine parameters for propane
            Psat       = 1e5*np.array([np.exp(a[i,0]-(a[i,1]/(T+a[i,2]))) for i in range(len(w))])

            return R, Tc, Pc, w, Kij, Psat