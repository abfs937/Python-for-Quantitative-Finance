from math import exp, log, pi


def norm_pdf(x):
    return (1.0/((2*pi)**0.5))*exp(-0.5*x*x)

def norm_cdf(x):
    k = 1.0 / (1.0 + 0.2316419 * x)
    k_sum = k * (0.319381530 + k * (-0.356563782 + k * (1.781477937 + k * (-1.821255978 + 1.330274429 * k))))

    if x >= 0.0:
        return (1.0 - (1.0 / ((2 * pi)**0.5)) * exp(-0.5 * x * x) * k_sum)
    else:
        return 1.0 - norm_cdf(-x)

def d_j(j, S, K, r, v, T):
    return (log(S/K) + (r + ((-1)**(j-1))*0.5*v*v)*T)/(v*(T**0.5))

def vanilla_call_price(S, K, r, v, T):
    return S * norm_cdf(d_j(1, S, K, r, v, T)) - \
        K*exp(-r*T) * norm_cdf(d_j(2, S, K, r, v, T))

def vanilla_put_price(S, K, r, v, T):
    return -S * norm_cdf(-d_j(1, S, K, r, v, T)) + \
        K*exp(-r*T) * norm_cdf(-d_j(2, S, K, r, v, T))

def vanila_call_Delta(S, K, r, v, T):
    return norm_cdf(d_j(1, S, K, r, v, T))

def vanila_put_Delta(S, K, r, v, T):
    return -norm_cdf(-d_j(1, S, K, r, v, T))

def vanila_call_Gamma(S, K, r, v, T):
    return norm_pdf(d_j(1, S, K, r, v, T)) / (v * S * (T**0.5))

def vanila_put_Gamma(S, K, r, v, T):
    return vanila_call_Gamma(S, K, r, v, T)

def vanilla_call_Theta(S, K, r, v, T):
    return -(v * S * norm_pdf(d_j(1, S, K, r, v, T)) / (2 * (T ** 0.5))) - r * exp ( -r * (T)) * K * norm_cdf(d_j(2, S, K, r, v, T))

def vanilla_put_Theta(S, K, r, v, T):
    return -(v * S * norm_pdf(-d_j(1, S, K, r, v, T)) / (2 * (T ** 0.5))) + r * exp ( -r * (T)) * K * norm_cdf(-d_j(2, S, K, r, v, T))

def vanilla_call_Vega(S, K, r, v, T):
    return S * norm_pdf(d_j(1, S, K, r, v, T)) * (T**0.5)

def vanilla_put_Vega(S, K, r, v, T):
    return vanilla_call_Vega(S, K, r, v, T)

def vanilla_call_Rho(S, K, r, v, T):
    return T * exp(-r * T) * K * norm_cdf(d_j(2, S, K, r, v, T))

def vanilla_put_Rho(S, K, r, v, T):
    return -T * exp(-r * T) * K * (1 - norm_cdf(d_j(2, S, K, r, v, T)))

S = float(input('S = '))
K = float(input('K = '))
r = float(input('r = '))
v = float(input('v = '))
T = float(input('T = '))

print("\n")

print('vanilla_call_price = ', round(vanilla_call_price(S, K, r, v, T), 4))
print('vanilla_put_price = ', round(vanilla_put_price(S, K, r, v, T), 4))
print("\n")
print('Delta of the call option = ', round(vanila_call_Delta(S, K, r, v, T), 4))
print('Delta of the put option =', round(vanila_put_Delta(S, K, r, v, T), 4))
print("\n")
print('Gamma of the call option = ', round(vanila_call_Gamma(S, K, r, v, T), 4))
print('Gamma of the put option = ', round(vanila_call_Gamma(S, K, r, v, T), 4))
print("\n")
print('Theta of the call option = ', round(vanilla_call_Theta(S, K, r, v, T), 4))
print('Theta of the put option = ', round(vanilla_put_Theta(S, K, r, v, T), 4))
print("\n")
print('Vega of the call option = ', round(vanilla_call_Vega(S, K, r, v, T), 4))
print('Vega of the put option = ', round(vanilla_put_Vega(S, K, r, v, T), 4))
print("\n")
print('Rho of the call option = ', round(vanilla_call_Rho(S, K, r, v, T), 4))
print('Rho of the put option = ', round(vanilla_put_Rho(S, K, r, v, T), 4))





