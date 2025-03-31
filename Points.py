import numpy as np

class Points:
    """
        This class gathers all desirable molar liquid fraction points for each available system.
    """

    def __int__(self):
        pass

    @staticmethod
    def Propane_Butane():
        x = np.array([0.054, 0.112, 0.226, 0.334,
                      0.426, 0.535, 0.634, 0.714,
                      0.808, 0.895, 0.922, 0.951])
        return x