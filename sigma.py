import numpy as np
import matplotlib.pyplot as plt

## Primero se imprimen los datos
n = open("valores.txt", "r")
datos = n.readlines()
for i in range(len(datos)):
    datos[i] = float(datos[i])
	
def proba(a,b,x):
    sigma = np.linspace(a,b,50)
    fp = []
    limite = (1.0/(b-a))
    a = limite
    for i in range(len(sigma)):
        sigmal = sigma[i]
        a = limite
        for j in range(len(x)):
            a = a * (1/(sigmal*np.sqrt(2*np.pi)))* np.exp((x[j]**2)/(-2)*sigmal**2)
        fp.append(a)   
        
    return sigma,fp

def plots(a,b,x):
    sigma,fp = proba(a,b,x)
    plt.plot(sigma, fp)
    plt.xlabel(r'$\sigma$')
    plt.ylabel(r'P($\sigma$|x)')

def fp(a,b,sigma,x):
    limite = (1.0/(b-a))
    a = limite
    sigmal = sigma
    for j in range(len(x)):
        a = a * (1/(sigmal*np.sqrt(2*np.pi)))* np.exp((x[j]**2)/(-2)*sigmal**2)
    return a

## MetropolisHasting
N = 100000
lista = [np.random.random()]
sigma_delta = 1.0

for i in range(1,N):
    a = -2
    b = 2
    x = datos
    propuesta  = lista[i-1] + np.random.normal(0,1)
    r = min(1,fp(a,b,propuesta,x)/fp(a,b,lista[i-1],x))
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])   

sigma, fp = proba(-2,2,datos)

plt.figure(figsize=(10,10))
_ = plt.hist(lista, density=True)  
plt.title("N = 0, desv = 1")
plt.savefig("sigma.png")
