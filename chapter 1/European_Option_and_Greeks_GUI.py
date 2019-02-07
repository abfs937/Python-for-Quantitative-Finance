from tkinter import *
from math import exp, log, pi

fields = ('Stock Price', 'Strike Price', 'Interest Rate', 'Volatility', 'Dividend Yield', 'Expiry Time')

def calculate(entries):
    S = float(entries['Stock Price'].get())
    K = float(entries['Strike Price'].get())
    r = float(entries['Interest Rate'].get())
    v = float(entries['Volatility'].get())
    d = float(entries['Dividend Yield'].get())
    T = float(entries['Expiry Time'].get())
    print("\n")
    print('vanilla_call_price = ', round(vanilla_call_price(S, K, r, v, d, T), 6))
    print('vanilla_put_price = ', round(vanilla_put_price(S, K, r, v, d, T), 6))
    print("\n")
    print('Delta of the call option = ', round(vanilla_call_Delta(S, K, r, v, d, T), 6))
    print('Delta of the put option =', round(vanilla_put_Delta(S, K, r, v, d, T), 6))
    print("\n")
    print('Gamma of the call option = ', round(vanilla_call_Gamma(S, K, r, v, d, T), 6))
    print('Gamma of the put option = ', round(vanilla_call_Gamma(S, K, r, v, d, T), 6))
    print("\n")
    print('Theta of the call option = ', round(vanilla_call_Theta(S, K, r, v, d, T), 6))
    print('Theta of the put option = ', round(vanilla_put_Theta(S, K, r, v, d, T), 6))
    print("\n")
    print('Vega of the call option = ', round(vanilla_call_Vega(S, K, r, v, d, T), 6))
    print('Vega of the put option = ', round(vanilla_put_Vega(S, K, r, v, d, T), 6))
    print("\n")
    print('Rho of the call option = ', round(vanilla_call_Rho(S, K, r, v, d, T), 6))
    print('Rho of the put option = ', round(vanilla_put_Rho(S, K, r, v, d, T), 6))

def norm_pdf(x):
    return (1.0/((2*pi)**0.5))*exp(-0.5*x*x)

def norm_cdf(x):
    k = 1.0 / (1.0 + 0.2316419 * x)
    k_sum = k * (0.319381530 + k * (-0.356563782 + k * (1.781477937 + k * (-1.821255978 + 1.330274429 * k))))

    if x >= 0.0:
        return (1.0 - (1.0 / ((2 * pi)**0.5)) * exp(-0.5 * x * x) * k_sum)
    else:
        return 1.0 - norm_cdf(-x)

def d_j(j, S, K, r, v, d, T):
    return (log(S/K) + (r - d + ((-1)**(j-1))*0.5*v*v)*T)/(v*(T**0.5))

def vanilla_call_price(S, K, r, v, d, T):
    return  S * exp(-d*T) * norm_cdf(d_j(1, S, K, r, v, d, T)) - \
        K*exp(-r*T) * norm_cdf(d_j(2, S, K, r, v, d, T))

def vanilla_put_price(S, K, r, v, d, T):
    return -S * exp(-d*T) * norm_cdf(-d_j(1, S, K, r, v, d, T)) + \
        K*exp(-r*T) * norm_cdf(-d_j(2, S, K, r, v, d, T))

def vanilla_call_Delta(S, K, r, v, d, T):
    return norm_cdf(d_j(1, S, K, r, v, d, T)) * exp(-d*T)

def vanilla_put_Delta(S, K, r, v, d,  T):
    return -norm_cdf(-d_j(1, S, K, r, v, d, T)) * exp(-d*T)

def vanilla_call_Gamma(S, K, r, v, d, T):
    return norm_pdf(d_j(1, S, K, r, v, d, T)) * exp(-d*T) / (v * S * (T**0.5))

def vanilla_put_Gamma(S, K, r, v, d, T):
    return vanilla_call_Gamma(S, K, r, v, d, T)

def vanilla_call_Theta(S, K, r, v, d, T):
    return -(v * S * norm_pdf(d_j(1, S, K, r, v, d, T)) * exp(-d*T) / (2 * (T ** 0.5))) - r * exp ( -r * (T)) * K * norm_cdf(d_j(2, S, K, r, v, d, T)) + d * S * exp(-d*T) * norm_cdf(d_j(1, S, K, r, v, d, T))

def vanilla_put_Theta(S, K, r, v, d, T):
    return -(v * S * norm_pdf(-d_j(1, S, K, r, v, d, T)) * exp(-d*T) / (2 * (T ** 0.5))) + r * exp ( -r * (T)) * K * norm_cdf(-d_j(2, S, K, r, v, d, T)) - d * S * exp(-d*T) * norm_cdf(-d_j(1, S, K, r, v, d, T))

def vanilla_call_Vega(S, K, r, v, d, T):
    return S * norm_pdf(d_j(1, S, K, r, v, d, T)) * exp(-d*T) * (T**0.5)

def vanilla_put_Vega(S, K, r, v, d, T):
    return vanilla_call_Vega(S, K, r, v, d, T)

def vanilla_call_Rho(S, K, r, v, d, T):
    return T * exp(-r * T) * K * norm_cdf(d_j(2, S, K, r, v, d, T))

def vanilla_put_Rho(S, K, r, v, d, T):
    return -T * exp(-r * T) * K * norm_cdf(-d_j(2, S, K, r, v, d, T))


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w', bg = 'light blue')
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries




if __name__ == '__main__':
    root = Tk()
    root.title("European Option and Greeks")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Quit', bg = 'light pink', command=root.quit)
    b1.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(root, text='Calculate', bg = 'light pink',
            command=(lambda e=ents: calculate(e)))
    b2.pack(side=RIGHT, padx=5, pady=5)
    root.mainloop()