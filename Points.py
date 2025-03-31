import numpy as np

class Points:
    """
        This class gathers all experimental points for each available system.
    """

    def __int__(self):
        pass

    @staticmethod
    def Propane_Butane(T):

        if T == 323.15:
            P = np.array([557000, 618000, 743000, 878000, 971000, 1101000, 1222000, 1324000, 1448000, 1564000, 1602000, 1643000])
            x = np.array([0.054, 0.112, 0.226, 0.334, 0.426, 0.535, 0.634, 0.714, 0.808, 0.895, 0.922, 0.951])
            y = np.array([0.139, 0.254, 0.432, 0.563, 0.651, 0.732, 0.804, 0.853, 0.906, 0.95, 0.964, 0.978])

        else:
            raise TypeError(f"There is no experimental points for Propane_Butane in such condition\n"
                            f"The available conditions are:\n"
                            f"T ---> 323.15 K")
        return x, y, P