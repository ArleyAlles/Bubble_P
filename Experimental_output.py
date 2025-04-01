import numpy as np

class Exp_output:

    def __init__(self):
        pass

    @staticmethod
    def Propane_Butane(T):

        if T == 323.15:
            P = np.array([557000, 618000, 743000, 878000, 971000, 1101000, 1222000, 1324000, 1448000, 1564000, 1602000, 1643000])
            y = np.array([0.139, 0.254, 0.432, 0.563, 0.651, 0.732, 0.804, 0.853, 0.906, 0.95, 0.964, 0.978])
        else:
            raise TypeError(f"There is no experimental points for this system in such temperature condition\n"
                            f"The available conditions are:\n"
                            f"T ---> 323.15 K")

        return P, y