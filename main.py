"""
P-bubble calculation.
Author: Arley Alles Cruz
"""

from Points import Points
from Parameters import Parameters
from Bubble import Bubble_Point

T     = 323.15
x,y,P = Points().Propane_Butane(T)
R, Tc, Pc, w, Kij, Psat = Parameters().Propane_Butane(T)
P_calc, y_calc = Bubble_Point(T, x, R, Tc, Pc, w, Kij, Psat, tol=1e-6, n_ite=2000).bubble_P()
