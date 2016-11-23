import numpy as np
from math import *
from objload import *
#from objwrite import *

infile  = "/home/ssorokan/Documents/3DFiles/plane.obj"
outlist = []

V,T,N,F = load_obj(infile)

for i in range(30):
    outlist.append("Plane-I2-%i.obj" %i)

    V2 = [] #new vertext list (keeping the same face list!)
    V3 = [] #put modified stuff in this
    M = np.array([[.2*i,1,0],[0,0,1],[1,0,0]])

    for v in range(len(V)):
        V2.append( (float(V[v][0]),float(V[v][1]),float(V[v][2]) ) )
        # Cartesian
        x = float(V[v][0])*10
        y = float(V[v][2])*10
        z = float(V[v][1])*10
        
        # Cylindrical
        #R = sqrt(float(V[v][0])*float(V[v][0])+float(V[v][2])*float(V[v][2]))
        #phi = atan2(float(V[v][2]),float(V[v][0]))
        #z = float(V[v][1])*2
        
        # Spherical
        #r =sqrt(float(V[v][0])*float(V[v][0])+float(V[v][1])*float(V[v][1])+float(V[v][2])*float(V[v][2]))
        #theta = acos(float(V[v][1])/r)
        #phi = atan2(float(V[v][2]),float(V[v][0]))
        #if theta != 0:
            #phi2 = phi*(1/theta)
        #    phi2 = phi*sin(theta)
        #else :
        #    phi2 = 1     
        
        # Torus
        # r = const
        #theta = atan2(float(V[v][2]),float(V[v][0]))
        #phi = asin(float(V[v][1])/r)
        #norm = 

        VMOD = abs(sin(exp(x))*sin(2*pi*i/30)+cos(y)-cos(2*pi*i/30))*log(sin(x)+cos(y)+2)*sin(2*pi*i/30)
        # Cartesian
        V3.append((10*V2[v][0] ,VMOD,10*V2[v][2]))
        
        # Cylindrical 
        #V3.append((VMOD*cos(phi),z,VMOD*sin(phi)))
        
        # Spherical
        #V3.append((VMOD*sin(theta)*cos(phi),VMOD*cos(theta),VMOD*sin(theta)*sin(phi)))
        
        # Toroidal
        #V3.append((VMOD*cos(phi),z,VMOD*sin(phi)))
        
    write_obj(outlist[i], V3, T, N, F)