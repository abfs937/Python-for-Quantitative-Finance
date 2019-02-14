# up-and-out barrier option with a European call pricing

import scipy as sp
from scipy import log, exp, sqrt, stats


def black_scholes_call(S, X, T, r, sigma):
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)


def up_and_out_call(s0, x, T, r, sigma, n_simulation, barrier):
    n_steps = 1000
    dt = T/n_steps
    total = 0
    for j in sp.arange(0, n_simulation):
        sT = s0
        out = False
        for i in range(0, int(n_steps)):
            e = sp.random.normal()
            sT *= sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt))
            if sT > barrier:
               out = True

        if out is False:
            total += black_scholes_call(s0, x, T, r, sigma)

    return total/n_simulation


print(round(up_and_out_call(100, 90, 2, 0.03, 0.05, 100, 120), 4))