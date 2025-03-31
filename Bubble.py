import numpy as np
from EoS import PengRobinson
from tabulate import tabulate


class Bubble_Point:
    """
    * Calculation of saturation point (bubble point) of mixtures using ϕ-ϕ approach.
    In this class the following methods are present:

        - Ki: Equilibrium constant calculation
        - bubble_P: Bubble point pressure and molar vapor fraction
    """

    def __init__(self, T, X, R, Tc, Pc, w, Kij, Psat, tol, n_ite):
        self.T = T
        self.X = X
        self.R = R
        self.Tc = Tc
        self.Pc = Pc
        self.w = w
        self.Kij = Kij
        self.Psat = Psat
        self.tol = tol
        self.n_ite = n_ite

    def Ki(self, P, x, y):
        """
        ECalculation of equilibrium constant for liquid and vapor phases
        :param P: Pressure of system [float]
        :param x: Molar liquid fraction [array - float]
        :param y: Molar vapor fraction [array - float]
        :return: Equilibrium constant [array - float]
        """
        Eos    = PengRobinson(P, self.T, self.R, self.Tc, self.Pc, self.w, self.Kij)
        Vol_l  = Eos.Volume(x, phase=1)
        Vol_v  = Eos.Volume(y, phase=0)
        phi_L  = Eos.phi(x, Vol_l)
        phi_V  = Eos.phi(y, Vol_v)
        Ki     = (np.array(phi_L) / np.array(phi_V))
        return Ki

    def bubble_P(self):
        """
        Saturation point calculation
        :return: Pressure and molar vapor fraction
        """

        print(f'\n############# Initialization of calculations ##############\n')
        P_out = np.zeros(len(self.X))
        y_out = np.zeros(len(self.X))

        #Raoult law (Initial guess)
        for i,x in enumerate(self.X):
            x   = np.array([x, 1-x])
            P   = sum(self.Psat*x)
            y   = (self.Psat/P)*x
            Ki  = self.Ki(P, x, y)
            ite = 0

            while(True):
                ite   += 1
                Ki_old = Ki
                P      = P*sum(Ki*x)
                y      = Ki*x
                y      = y/sum(y)
                Ki     = self.Ki(P, x, y)
                error  = sum(abs(Ki-Ki_old))
                if (error<self.tol) or (ite>self.n_ite):
                    P_out[i] = P
                    y_out[i] = y[0]
                    print(f'Procedure accomplished for molar fraction (xa): {x[0]}')
                    break

        results = {"Calculated saturation pressure":P_out,
                   "Calculated vapor molar fraction":y_out,
                   "Liquid molar fraction":self.X}
        print(f'\n{tabulate(results, headers="keys", tablefmt="grid", colalign=("center", "center", "center"))}')

        return P_out,y_out





