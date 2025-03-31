"""
P-bubble calculation.
Author: Arley Alles Cruz
"""

from Points import Points
from Parameters import Parameters
from Bubble import Bubble_Point
from Experimental_output import Exp_output

T = 323.15
x = Points().Propane_Butane()
P_exp, y_exp = Exp_output().Propane_Butane(T)
R, Tc, Pc, w, Kij, Psat = Parameters().Propane_Butane(T)
Bubble_Point(T, x, R, Tc, Pc, w, Kij, Psat, tol=1e-6, n_ite=2000).AARD(P_exp,y_exp)
