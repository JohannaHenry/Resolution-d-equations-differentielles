# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#z = ydot
t = np.linspace (0,40,1000)


#Tracé Euler et module Scipy : régime libre

def EQD_libre(t0,tf,j,p,q0): #t0 et tf designent respectivement le temps initial et le temps final, j designe w0 , et p designe Q
    h=0.05 #h designe le pas
    t,q,z=t0,q0,0 #valeurs initiales
    T,Q,Z=[t],[q],[z] #création de 3 listes
    while t<tf:
        t,q,z=t+h,q+h*z,z+h*((-j*z)/p-q*j**2)
        T.append(t)
        Q.append(q)
        Z.append(z)
    return T,Q


def f(q,t,w0,Q):#q_dot=f(q,t)
    z_dot = -(w0/Q)*q[1]-w0**2*q[0] #q[1]=q_dot et q[0]=q
    return [q[1],z_dot] #vecteur (q_dot,q_dot2)

sol_ode = odeint(f,(2,0),t,args=(2,100))#2=q0 et args=(w0/Q,w0**2)


def graphe_libre(t0,tf,j,p,q0): #fonction qui permet de tracer q(t) en executant les deux fonctions précédentes
    T,Q=EQD_libre(t0,tf,j,p,q0)
    #création du graphique
    plt.plot(T,Q,'b',label='Euler')
    plt.plot (t,sol_ode[:,0],"r",label='Scipy')
    plt.legend(loc="upper center")
    plt.title("Modélisation du circuit RLC par la méthode d'Euler et d'Odeint")
    plt.xlabel("temps (seconde)") #abscisse
    plt.ylabel("Q(t)") #ordonnée
    plt.legend()
    plt.grid()
    plt.show()




#Tracé Euler et module Scipy : régime forcé

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


def F(y,t,w0,Q):#y_dot=f(y,t)
    z_dot = 4*np.cos(1*t)-(w0/Q)*y[1]-w0**2*y[0] #y[1]=y_dot et y[0]=y
    return [y[1],z_dot] #vecteur (y_dot,y_dot2)

sol_ode = odeint(F,(2,0),t,args=(2,100))#2=q0 et args=(w0/Q,w0**2)


def graphe_force(t0,tf,j,p,q0,A,w): #fonction qui permet de tracer q(t) en executant les deux fonctions précédentes
    T,Q=EQD_force(t0,tf,j,p,q0,A,w)
    #création du graphique
    plt.plot(T,Q,'b', label='Euler')
    plt.plot (t,sol_ode[:,0],"r",label='Scipy')
    plt.legend(loc="upper center")
    plt.title("Modélisation du circuit RLC par la méthode d'Euler et d'Odeint")
    plt.xlabel("temps (seconde)") #abscisse
    plt.ylabel("Q(t)") #ordonnée
    plt.legend()
    plt.grid()
    plt.show()
   
    


    











