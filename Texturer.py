import numpy as np
from math import *
from objload import *
#from objwrite import *

infile  = "/home/ssorokan/Documents/3DFiles/plane.obj"
mtlpath = "ship2.mtl"
outlist = []
Tex = []


V,T,N,F = load_obj(infile)

for i in range(3):
    outlist.append("TextureTest-1-%i.obj" %i)

    V2 = [] #new vertext list (keeping the same face list!)
    V3 = [] #put modified stuff in this
    M = np.array([[.2*i,1,0],[0,0,1],[1,0,0]])

    for v in range(len(V)):
        V2.append( (float(V[v][0]),float(V[v][1]),float(V[v][2]) ) )
        # Cartesian
        x = float(V[v][0])*10
        y = float(V[v][2])*10
        z = float(V[v][1])*10

        VMOD = abs(sin(x)*sin(2*pi*(i+25)/30)+cos(y)-cos(2*pi*(i+25)/30))*log(sin(x)+cos(y)+2)*sin(2*pi*(i+25)/30)
        # Cartesian
        V3.append((10*V2[v][0] ,VMOD,10*V2[v][2]))
        
    # Determine Texture Values
    for f in range(len(F)):
        if abs(float(V3[int(F[f][1])-1][1])) > .09:
            Tex.append([1]) #number for material definition
        else:
            Tex.append([2])
                            
    write_obj_Textured(outlist[i],mtlpath,V3,N,T,F,Tex) #filepath,mtlpath,V,N,T,F,Tex