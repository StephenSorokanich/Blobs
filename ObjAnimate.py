import numpy as np
from math import *
from objload import *
#from objwrite import *

def ObjAnimate(outfilename, X, Y, Z):
    infile  = "/home/ssorokan/Documents/3DFiles/plane.obj"
    outlist = []
    
    V,T,N,F = load_obj(infile)

    for i in range(30):
        outlist.append(outfilename + "-%i.obj" %i)
    
        V2 = [] #new vertext list (keeping the same face list!)
        V3 = [] #put modified stuff in this

        for v in range(len(V)):
            V2.append( (float(V[v][0]),float(V[v][1]),float(V[v][2]) ) )
            # Cartesian
            x = float(V[v][0])*10
            y = float(V[v][2])*10
            z = float(V[v][1])*10

            # Cartesian
            V3.append((X(x) ,Z(z),Y(y)))
        
        write_obj(outlist[i], V3, T, N, F)