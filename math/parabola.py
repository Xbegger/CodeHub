from sympy import *
import math

import sympy


def feval(phi, x):
    return phi(x)

def qmin(phi, a, b, delta, epsilon):
    s0 = a
    maxj = 20
    maxk = 30
    big = 1e6
    err = 1
    k = 1
    S = []
    S.append(s0)
    cond = 0
    h = 1
    ds = 0.00001

    if( abs(s0) > 1e4 ):
        h = abs(s0) * (1e-4)
    
    while( k < maxk and err > epsilon and cond != 5):
    # 进行抛物线法的条件
    # k 迭代次数
    # err  abs(phi1 - barphi)
    # cond==5  abs(h) > 1e6 or abs(s0) > 1e6

        # 计算在 s0 点处的近似导数
        f1 = ( feval(phi, s0 + ds) - feval(phi, s0 - ds) ) / (2 * ds)

        if(f1 > 0):
            h = -abs(h)
        s1 = s0 + h
        s2 = s0 + 2 * h
        bars = s0

        phi0 = feval(phi, s0)
        phi1 = feval(phi, s1)
        phi2 = feval(phi, s2)
        barphi = phi0

        cond = 0
        j = 0

        # cond == -1 确定 h ,使得 s0 < s1 < s2 ,满足 phi0 > phi1, phi1 < phi2
        # cond == 5
        while(j < maxj and abs(h) > delta and cond == 0):
            if(phi0 <= phi1):
                s2 = s1
                phi2 = phi1
                h = 0.5 * h
                s1 = s0 +h
                phi1 = feval(phi, s2)
            else:
                if(phi2 < phi1):
                    s1 = s2
                    phi1 = phi2
                    h = 2 * h
                    s2 = s0 + 2 * h
                    phi2 = feval(phi, s2)
                else:
                    cond = -1
            j = j + 1

            if(abs(h) > big or abs(s0) > big):
                cond = 5

     
        if(cond == 5):
            bars = s1
            barphi = feval(phi, s1)
        else:
        # 计算插值点
            d = 2 * (2 * phi1 - phi0 - phi2)
            if(d < 0):
                barh = h * (4 * phi1 - 3 * phi0 - phi2) / d
            else:
                barh = h / 3
                cond = 4
            bars = s0 + barh
            barphi = feval(phi, bars)
            h = abs(h)
            h0 = abs(barh)
            h1 = abs(barh - h)
            h2 = abs(barh - 2 * h)

            # 确定下一次迭代的 h
            if(h0 < h):
                h = h0
            if(h1 < h):
                h = h1
            if(h2 < h):
                h = h2
            if(h == 0):
                h = barh
            if(h < delta):
                cond = 1
            if(abs(h) > big or abs(bars) > big):
                cond = 5
            err = abs(phi1 - barphi)
            s0 = bars
            k = k + 1

            #S(k) = s0
            S.append(s0)
        if(cond == 2 and h < delta):
            cond = 3
    s = s0
    phis = feval(phi, s)
    ds = h
    dphi = err
    return s, phis, k, ds, dphi, S


def npForm(f, x):
    return lambdify([x], f, 'numpy')

x = symbols('x')
# f = x**2 - sympy.sin(x)
f = x**3 - 2 * x + 1
print(f)
phi = npForm(f, x)
print(qmin(phi, 0., 3., 0.01, 1e-6))