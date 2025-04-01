import numpy as np


class PengRobinson:
    """
    *Calculation of properties using Peng-Robinson EoS.
    In this class the following methods are present:

        - kij: Binary interaction parameter
        - mixture_rule: Molar volume calculation for a specific phase
        - Volume: Molar volume calculation for a specific phase in a multi-component system
        - phi: Coefficient fugacity (phi) for a multi-component system

    OBS: the methods: dPdro; d2Pdro2; pressure; Newton and Bissection are auxiliary methods for Volume

    """

    def __init__(self, P, T, R, Tc, Pc, w, Kij):
        self.P = float(P)  # ---------------------------------> Pressure (Pa)
        self.T = T  # ----------------------------------------> Temperature (K)
        self.R = R
        self.Tc = Tc
        self.Pc = Pc
        self.w = w

        # Global parameters of Peng-Robinson equation
        self.sigma = 1 + np.sqrt(2)
        self.epsilon = 1 - np.sqrt(2)
        self.Kij = Kij

    def kij(self):
        """
        Organization of binary interaction parameter
        :return: Kij
        """
        cont   = 0
        row    = len(self.w)
        column = row
        matrix = np.zeros((row, column))

        for i in range(row):
            for j in range(column):
                if j > i:
                    matrix[i, j] = self.Kij[cont]
                    cont += 1

        matrix_T   = np.transpose(matrix)
        matrix_kij = matrix + matrix_T
        Kij        = [matrix_kij[i, j] for i in range(row) for j in range(column)]

        return Kij

    def mixture_rule(self, x):
        """
        * Mixture attraction and repulsion coefficients by VdW rule mixture
            :param x: Mole fraction of a given phase
            :return: a, b, aij, bi
        """
        cont  = 0
        a     = 0
        aij   = np.zeros(2*len(self.w))
        Kij   = self.kij()
        Tr    = self.T/self.Tc
        Kpri  = 0.37464+(1.54226*self.w)-(0.26992*(self.w**2))
        alfai = (1+Kpri*(1-np.sqrt(Tr)))**2
        aci   = 0.45724*(self.R**2)*(self.Tc**2)/self.Pc
        ai    = aci*alfai
        bi    = 0.07780*self.R*(self.Tc/self.Pc)
        b     = sum(x*bi)
        for j in range(len(self.w)):
            for l in range(len(self.w)):
                aij[cont] = (np.sqrt(ai[j]*ai[l])*(1-Kij[cont]))
                a += x[j]*x[l]*aij[cont]
                cont += 1

        return a, b, aij, bi

    def dPdro(self, ro, a, b):

        f = self.R * self.T * b * ro / (-b * ro + 1) ** 2 + self.R * self.T / (-b * ro + 1) - a * ro ** 2 * (
                b ** 2 * ro - b * (-b * ro + 2)) / (b * ro * (-b * ro + 2) + 1) ** 2 - 2 * a * ro / (
                    b * ro * (-b * ro + 2) + 1)
        return f

    def d2Pdro2(self, ro, a, b):
        f = 2 * self.R * self.T * b ** 2 * ro / (-b * ro + 1) ** 3 + 2 * self.R * self.T * b / (
                -b * ro + 1) ** 2 - 2 * a * b ** 2 * ro ** 2 / (b * ro * (-b * ro + 2) + 1) ** 2 - a * ro ** 2 * (
                    b ** 2 * ro - b * (-b * ro + 2)) * (2 * b ** 2 * ro - 2 * b * (-b * ro + 2)) / (
                    b * ro * (-b * ro + 2) + 1) ** 3 - 4 * a * ro * (b ** 2 * ro - b * (-b * ro + 2)) / (
                    b * ro * (-b * ro + 2) + 1) ** 2 - 2 * a / (b * ro * (-b * ro + 2) + 1)
        return f

    def pressure(self, ro, a, b):
        f1 = (ro * self.R * self.T) / (1 - ro * b)
        f2 = (a * ro ** 2) / (1 + ro * b * (2 - ro * b))
        f = f1 - f2
        return f

    @staticmethod
    def Bissection(f, a, b, P_spe, ro_min, ro_max):

        tol = 1e-6

        while True:
            xr = (ro_min + ro_max) / 2
            f_min = f(ro_min, a, b) - P_spe
            f_r = f(xr, a, b) - P_spe
            if (f_min * f_r) < 0:
                ro_max = xr

            elif (f_min * f_r) > 0:
                ro_min = xr

            erro = f(xr, a, b) - P_spe
            if abs(erro) < tol:
                return xr


    def Volume(self, x, phase):

        global ro
        a, b, _, _ = self.mixture_rule(x)
        P_spe = self.P


        # Identify if condition belongs to curve C and find the root
        if self.d2Pdro2(0, a, b) > 0:
            # ro = self.Newton(self.pressure, self.dPdro, P_spe, 0.5, a, b)
            ro = self.Bissection(self.pressure, a, b, P_spe, 0, 1/ b)

        else:
            ro_cc = self.Bissection(self.d2Pdro2, a, b, 0, 0, 1 / b)
            P_cc = self.pressure(ro_cc, a, b)

            # Identify if condition belongs to curve B and find the root
            if self.dPdro(ro_cc, a, b) > 0:

                if P_spe < P_cc:
                    ro = self.Bissection(self.pressure, a, b, P_spe, 0, ro_cc)
                    return 1 / ro

                elif P_spe > P_cc:
                    ro = self.Bissection(self.pressure, a, b, P_spe, ro_cc, 1 / b)
                    return 1 / ro

            # Identify if condition belongs to curve A and find the root
            else:
                ro_max = self.Bissection(self.dPdro, a, b, 0, 0, ro_cc)
                ro_min = self.Bissection(self.dPdro, a, b, 0, ro_cc, 1 / b)

                if self.pressure(ro_max, a, b) > P_spe > self.pressure(ro_min, a, b):
                    if phase == 0:  # Vapor
                        ro = self.Bissection(self.pressure, a, b, P_spe, 0, ro_max)
                    elif phase == 1:  # Liquid
                        ro = self.Bissection(self.pressure, a, b, P_spe, ro_min, 1 / b)

                elif P_spe > self.pressure(ro_max, a, b):
                    ro = self.Bissection(self.pressure, a, b, P_spe, ro_min, 1 / b)

                elif P_spe < self.pressure(ro_min, a, b):
                    ro = self.Bissection(self.pressure, a, b, P_spe, 0, ro_max)

        return 1 / ro

    def phi(self, x, Vol):
        """
        * Coefficient fugacity (phi) for a multi-component system
            :param x: Molar fraction
            :param Vol: Molar volume
            :return (list): phi_L; phi_V
        """

        phi   = np.zeros(len(x))
        da    = np.zeros(len(x))
        q     = np.zeros(len(x))
        beta  = np.zeros(len(x))
        cont  = 0
        termo = 0

        a, b, aij, bi = self.mixture_rule(x)
        Z   = (self.P * Vol) / (self.R * self.T)
        num = Vol + (self.sigma * b)
        den = Vol + (self.epsilon * b)
        I   = (1/(self.sigma-self.epsilon))*np.log(num/den)

        for k in range(len(x)): #Iteration for calculating phi for each component
            for j in range(len(x)):
                termo += aij[cont] * x[j]
                cont  += 1

            da[k]   = (2 * termo - a)
            q[k]    = (a / (b * self.R * self.T))
            beta[k] = ((b * self.P) / (self.R * self.T))
            dq_l    = q[k] * (1 + (da[k] / a) - (bi[k] / b))
            phi[k]  = (np.exp(((bi[k]/b)*(Z-1))-np.log(Z-beta[k])-(dq_l*I)))
            termo   = 0

        return phi