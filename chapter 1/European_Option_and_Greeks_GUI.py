from tkinter import *
from math import exp, log, pi

fields = ('Stock Price', 'Strike Price', 'Interest Rate', 'Volatility', 'Remaining Time')
call_put_fields = ('Vanilla Call Price','Vanilla Put Price','Delta Call Option','Delta Put Option','Gamma Call Option','Gamma Put Option','Theta Call Option','Theta Put Option','Vega Call Option','Vega Put Option','Rho Call Option','Rho Put Option')

def calculate(entries):
    S = float(entries['Stock Price'].get())
    K = float(entries['Strike Price'].get())
    r = float(entries['Interest Rate'].get())
    v = float(entries['Volatility'].get())
    T = float(entries['Remaining Time'].get())
    print('vanilla_call_price = %f' %vanilla_call_price(S, K, r, v, T))
    print('vanilla_put_price = %f' %vanilla_put_price(S, K, r, v, T))
    print("\n")
    print('Delta of the call option = %f' %vanilla_call_Delta(S, K, r, v, T))
    print('Delta of the put option = %f' %vanilla_put_Delta(S, K, r, v, T))
    print("\n")
    print('Gamma of the call option = %f' %vanilla_call_Gamma(S, K, r, v, T))
    print('Gamma of the put option = %f' %vanilla_call_Gamma(S, K, r, v, T))
    print("\n")
    print('Theta of the call option = %f' %vanilla_call_Theta(S, K, r, v, T))
    print('Theta of the put option = %f'%vanilla_put_Theta(S, K, r, v, T))
    print("\n")
    print('Vega of the call option = %f' %vanilla_call_Vega(S, K, r, v, T))
    print('Vega of the put option = %f' %vanilla_put_Vega(S, K, r, v, T))
    print("\n")
    print('Rho of the call option = %f' %vanilla_call_Rho(S, K, r, v, T))
    print('Rho of the put option = %f' %vanilla_put_Rho(S, K, r, v, T))
    
    updatelist[0].set(str(vanilla_call_price(S, K, r, v, T)))
    updatelist[1].set(str(vanilla_put_price(S, K, r, v, T)))

    updatelist[2].set(str(vanilla_call_Delta(S, K, r, v, T)))
    updatelist[3].set(str(vanilla_put_Delta(S, K, r, v, T)))

    updatelist[4].set(str(vanilla_call_Gamma(S, K, r, v, T)))
    updatelist[5].set(str(vanilla_call_Gamma(S, K, r, v, T)))

    updatelist[6].set(str(vanilla_call_Theta(S, K, r, v, T)))
    updatelist[7].set(str(vanilla_put_Theta(S, K, r, v, T)))

    updatelist[8].set(str(vanilla_call_Vega(S, K, r, v, T)))
    updatelist[9].set(str(vanilla_put_Vega(S, K, r, v, T)))

    updatelist[10].set(str(vanilla_call_Rho(S, K, r, v, T)))
    updatelist[11].set(str(vanilla_put_Rho(S, K, r, v, T)))
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

def vanilla_call_Delta(S, K, r, v, T):
    return norm_cdf(d_j(1, S, K, r, v, T))

def vanilla_put_Delta(S, K, r, v, T):
    return -norm_cdf(-d_j(1, S, K, r, v, T))

def vanilla_call_Gamma(S, K, r, v, T):
    return norm_pdf(d_j(1, S, K, r, v, T)) / (v * S * (T**0.5))

def vanilla_put_Gamma(S, K, r, v, T):
    return vanilla_call_Gamma(S, K, r, v, T)

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


def makeform(root, fields, callputfields):
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
        
   for field in callputfields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w', bg = 'light pink')
        lab2 = Label(row, width=22, textvariable = updatelist[call_put_fields.index(field)], anchor='w', bg = 'light yellow')
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        lab2.pack(side=RIGHT)   
    return entries

def initialise_list():
    templist = []
    for _ in range(12):
        var = StringVar()
        templist.append(var)
    return templist


if __name__ == '__main__':
    root = Tk()
    updatelist = initialise_list()
    root.title("European Option and Greeks")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Quit', bg = 'light pink', command=root.quit)
    b1.pack(side=RIGHT, padx=5, pady=5)
    b2 = Button(root, text='Calculate', bg = 'light pink',
            command=(lambda e=ents: calculate(e)))
    b2.pack(side=RIGHT, padx=5, pady=5)
    root.mainloop()
