import sympy as sp

k = sp.symbols('k')

expr = 58 * sp.log((1000 + 5*k)/(30 + 70*k), 10) + 60

solution = sp.nsolve(expr, 1)

print(solution)

''' As we know that Action Potentials are generated not by change in concentrations but by change in permeability. 
So we keep the concentrations same as they were at RMP and set the Vm to -60 and keeping the permeability of Cl as unknown,
we find the value of permeability of Cl (to simplify the equation we cancelled the powers of 10 from the GHK equation and so in the
equation we calculate the value of k but in reality the permeability will be k * 10 ^ (-8)). 

By solving the above equation we get the value of k as 680.38 (approx) and so we will use this value further. 
 '''
