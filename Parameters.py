import numpy as np


class Parameters:

    def __init__(self):
        pass

    @staticmethod
    def Propane_Butane(T):

            Components = np.array(['Propane', 'Butane'])  # -----> Components
            R = 8.314  # ----------------------------------------> Gas constant (J*mol-1*K-1)
            Tc = np.array([369.8, 425.1])  # --------------------> Critical temperature (K)
            Pc = np.array([4248000, 3796000])  # ----------------> Critical pressure (Pascal)
            w = np.array([0.152, 0.2])  # -----------------------> acentric factor (dimensionless)
            Kij = np.array([0.0008]) #---------------------------> binary interaction parameter
            a = np.array([3.98292, 819.296, -24.417]) #----------> Antoine parameters for propane
            b = np.array([4.35576, 1175.581, -2.071]) #----------> Antoine parameters for butane
            Psat_C3H8 = a[0] - (a[1] / (T + a[2]))
            Psat_C4H10 = b[0] - (b[1] / (T + b[2]))
            Psat = 1e5 * np.array([np.exp(Psat_C3H8), np.exp(Psat_C4H10)])
            return Components, R, Tc, Pc, w, Kij, Psat