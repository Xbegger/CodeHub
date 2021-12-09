from sympy import *
import math
import numpy as np

# x1 = symbols('x1')
# x2 = symbols('x2')

# f = (100 * (x1**2 - x2)**2 + (x1 - 1)**2)

# print(f)

# gf = [diff(f, x1), diff(f, x2) ]
# print(gf)

# fn = lambdify([(x1, x2)], f, 'numpy')
# print( fn([4,1]))
# a = np.array([1, 3])
# b = np.array([1, 1])
# print( 0.3 * b)

# print()
# print(gf.evalf(subs={'x2':4, 'x1':1}))


def feval(func, x):

    try:
        ans = list()
        for f in func:
            ans.append(f(x))
        ans = np.array(ans)
    except:
        ans = func(x)
    return ans


def grad(fun, gfun, x0):
    maxk = 5000
    rho = 0.5
    sigma = 0.4
    k = 0
    epsilon = 1e-5

    while( k < maxk ):
        g = feval(gfun, x0)
        d = -g
        if( np.linalg.norm(g) < epsilon):
            break
        m = 0
        mk = 0

        while( m < 20 ):
            if( feval(fun, x0 + rho**m * d) < feval(fun, x0) + sigma * rho**m * g @ d):
                mk = m
                break
            m = m + 1
        x0 = x0 + rho**mk * d
        k = k + 1

    x = x0
    val = feval(fun, x0)
    return val, k

def npForm(f, x):
    return lambdify([x], f, 'numpy')


x1 = symbols('x1')
x2 = symbols('x2')
x = (x1, x2)
# f = (100 * (x1**2 - x2)**2 + (x1 - 1)**2)
f = (x1 - 2)**4 + (x1 - 2 * x2)**2

fun = npForm(f, x)

gfun = np.array([npForm(diff(f, x1), x), npForm(diff(f, x2), x)])

x0 = np.array([0., 3.])


print( grad(fun, gfun, x0) )

