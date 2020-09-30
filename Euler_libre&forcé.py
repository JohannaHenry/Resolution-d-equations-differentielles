import numpy as np
import matplotlib.pyplot as plt


#Résolution par la méthode d'Euler : Régime libre

def EQD_libre(t0,tf,j,p,q0): #t0 et tf designent respectivement le temps 
#initial et le temps final, j designe w0, et p designe Q.
    h=0.05 #h designe le pas
    t,q,z=t0,q0,0 #valeurs initiales
    T,Q,Z=[t],[q],[z] #création de 3 listes
    while t<tf:
        t,q,z=t+h,q+h*z,z+h*((-j*z)/p-q*j**2)
        T.append(t)
        Q.append(q)
        Z.append(z)
    return T,Q


def graphe_libre(t0,tf,j,p,q0): #création d'une fonction qui permet de tracer 
#q(t) en éxecutant la fonction précédente
    T,Q=EQD_libre(t0,tf,j,p,q0)
    #création du graphiqu
    plt.plot(T,Q,label='blue')
    plt.legend(loc="upper center")
    plt.title("Modélisation du circuit RLC par la méthode d'Euler")
    plt.xlabel("temps (seconde)") #abscisse
    plt.ylabel("Q(t)") #ordonnée
    plt.legend('C')
    plt.grid()
    plt.show()
   
    
    
#Résolution par la méthode d'Euler : Régime forcé
    
def EQD_force(t0,tf,j,p,q0,A,w):
    h=0.05 #h designe le pas
    t,q,z=t0,q0,0 #valeurs initiales
    T,Q,Z=[t],[q],[z] #création de 3 listes
    while t<tf:
        t,q,z=t+h,q+h*z,z+h*((-j*z)/p-q*j**2+A*np.cos(w*t))
        T.append(t)
        Q.append(q)
        Z.append(z)
    return T,Q


def graphe_force(t0,tf,j,p,q0,A,w): #création d'une fonction qui permet de 
#tracer q(t) en executant la fonction précédente
    T,Q=EQD_force(t0,tf,j,p,q0,A,w)
    #création du graphique
    plt.plot(T,Q,label='blue') 
    plt.legend(loc="upper center")
    plt.title("Modélisation du circuit RLC par la méthode d'Euler")
    plt.xlabel("temps (seconde)") #abscisse
    plt.ylabel("Q(t)") #ordonnée
    plt.legend('C')
    plt.grid()
    plt.show()
