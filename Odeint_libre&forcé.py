# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#z = qdot
#w0=10, Q=5,l'amplittude vaut A=4, et la pulsation w=1

t = np.linspace (0,40,1000)


#Résolution grâce à Odeint : régime libre

def f(q,t,w0,Q):#q_dot=f(q,t)

    z_dot = -(w0/Q)*q[1]-w0**2*q[0] #q[1]=q_dot et q[0]=q
    return [q[1],z_dot] #vecteur (q_dot,q_dot2)


sol_ode = odeint(f,(2,0),t,args=(5,100))#2=q0 et args=(w0/Q,w0**2)
plt.title("Evolution temporelle de q(t) en régime libre")
plt.plot (t,sol_ode[:,0],"b")
plt.xlabel('Temps(s)')
plt.ylabel('Charge q')
plt.grid()
plt.figure()
plt.show()
plt.savefig("figure.pdf")



#Résolution grâce à Odeint : régime forcé

def F(q,t,w0,Q):#q_dot=f(q,t)

    z_dot = 4*np.cos(1*t)-(w0/Q)*q[1]-w0**2*q[0] #q[1]=q_dot et q[0]=q
    return [q[1],z_dot] #vecteur (q_dot,q_dot2)


sol_ode = odeint(F,(2,0),t,args=(5,100))#2=q0 et args=(w0/Q,w0**2)
plt.title("Evolution temporelle de q(t) en régime forcé")
plt.plot (t,sol_ode[:,0],"b")
plt.xlabel('Temps(s)')
plt.ylabel('Charge q')
plt.grid()
plt.figure()
plt.show()
plt.savefig("figure.pdf")




