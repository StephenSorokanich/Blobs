import numpy as np
from math import *
from objload import *
#from objwrite import *

infile  = "/home/ssorokan/Documents/3DFiles/cube.obj"
outlist = []

V,T,N,F = load_obj(infile)

for i in range(30):
    outlist.append("CubeSphere-I0-%i.obj" %i)

    V2 = [] #new vertex list (keeping the same face list!)
    V3 = [] #put modified stuff in this
    M = np.array([[.2*i,1,0],[0,0,1],[1,0,0]])

    for v in range(len(V)):
        V2.append( (float(V[v][0]),float(V[v][1]),float(V[v][2]) ) )
        # Cartesian
        x = float(V[v][0])
        y = float(V[v][2])
        z = float(V[v][1])
        
        X = 0.0 
        Y = 0.0
        Z = 0.0
        
        if max(abs(x),abs(y),abs(z)) == abs(x):
            X = cos(pi*3*float(y))
            Y = cos(pi*3*float(z))
        elif max(abs(x),abs(y),abs(z)) == abs(y) :
            X = cos(pi*3*float(x))
            Y = cos(pi*3*float(z))
        elif max(abs(x),abs(y),abs(z)) == abs(z) :
            X = cos(pi*3*float(x))
            Y = cos(pi*3*float(y))

        #H0
        #VMOD = .01*(sin(Y*pi)*cos(sin(X*pi)+sin(2*pi*i/30))+sin(X*pi)*sin(sin(Y*pi)+cos(2*pi*i/30)))+.01*exp(sin(sin(X*pi)+sin(Y*pi))) 
        VMOD = .1*exp(cos(X+Y)+sin(2*pi*i/30))+.1*exp(-sin(Y+sin(2*pi*i/30)))
        #r = sqrt(x*x+y*y+z*z)

        # Cube Map 1
        #if abs(x) == max(abs(x),abs(y),abs(z)):
        #    V3. append(((VMOD+x)/r, V2[v][1]/r, V2[v][2]/r)) 
        #elif abs(y) == max(abs(x),abs(y),abs(z)):
        #    V3. append((V2[v][0]/r, V2[v][1]/r, (VMOD+y)/r))  
        #elif abs(z) == max(abs(x),abs(y),abs(z)):
        #    V3. append((V2[v][0]/r, (VMOD+z)/r, V2[v][2]/r)) 
        #else :
        #    V3.append((V2[v][0]/r ,V2[v][1]/r,V2[v][2]/r))
            
        # Cube Map 2
        if abs(x) == max(abs(x),abs(y),abs(z)):
            
            V3. append(((x*VMOD+x)*sqrt(1-y*y/2-z*z/2+y*y*z*z/3), V2[v][1]*sqrt(1-x*x/2-y*y/2+x*x*y*y/3), V2[v][2]*sqrt(1-z*z/2-x*x/2+z*z*x*x/3))) 
        elif abs(y) == max(abs(x),abs(y),abs(z)):
            V3. append((V2[v][0]*sqrt(1-y*y/2-z*z/2+y*y*z*z/3), V2[v][1]*sqrt(1-x*x/2-y*y/2+x*x*y*y/3), (VMOD*y+y)*sqrt(1-z*z/2-x*x/2+z*z*x*x/3)))  
        elif abs(z) == max(abs(x),abs(y),abs(z)):
            V3. append((V2[v][0]*sqrt(1-y*y/2-z*z/2+y*y*z*z/3), (VMOD*z+z)*sqrt(1-x*x/2-y*y/2+x*x*y*y/3), V2[v][2]*sqrt(1-z*z/2-x*x/2+z*z*x*x/3))) 
        else :
            V3.append((V2[v][0]*sqrt(1-y*y/2-z*z/2+y*y*z*z/3) ,V2[v][1]*sqrt(1-x*x/2-y*y/2+x*x*y*y/3),V2[v][2]*sqrt(1-z*z/2-x*x/2+z*z*x*x/3)))


    write_obj(outlist[i], V3, T, N, F)