#do the loading of the obj file
def load_obj(filename) :
 V = [] #vertex
 T = [] #texcoords
 N = [] #normals
 F = [] #face indexies

 fh = open(filename)
 for line in fh :
  if line[0] == '#' : continue
 
  line = line.strip().split(' ')
  if line[0] == 'f' : #vertex
   F.append(line[1:])
  elif line[0] == 'vt' : #tex-coord
   T.append(line[1:])
  elif line[0] == 'v' : #face
   V.append(line[1:])
  elif line[0] == 'vn' : #normal vector
   N.append(line[1:])
   #face = line[1:]
   #if len(face) != 4 : 
    #print line
    #raise Exception('not a quad!')
   # continue
   #for i in range(0, len(face)) :
   # face[i] = face[i].split('/')
    # OBJ indexies are 1 based not 0 based hence the -1
    # convert indexies to integer
    #for j in range(0, len(face[i])) : face[i][j] = int(face[i][j]) - 1
   #F.append(face)

 return V, T, N, F

#V,T,N,F = load_obj("C:\Users\Steve\Desktop\Cell\Rhino\dteddy.obj")

def write_obj(filepath, V, T, N, F):
    with open(filepath, 'w') as f:
        f.write("# OBJ file\n")
        for vq in range(len(V)):
            f.write("v %.4f %.4f %.4f\n" % ( float(V[vq][0]), float(V[vq][1]), float(V[vq][2]) ) )
        for vn in range(len(N)):
            f.write("vn %.4f %.4f %.4f\n" % ( float(N[vn][0]), float(N[vn][1]), float(N[vn][2]) ) )
        if (len(F) > 1):
            for p in range(len(F)):
                f.write("f")
                for i in range(len(F[p])):
                    f.write(" %d" % int(F[p][i]))
                f.write("\n")
        elif (len(F)<=1):
            f.write("\n")
            
def write_obj_VN(filepath, V, N):
    with open(filepath, 'w') as f:
        f.write("# OBJ file\n")
        for vq in range(len(V)):
            f.write("v %.4f %.4f %.4f\n" % ( float(V[vq][0]), float(V[vq][1]), float(V[vq][2]) ) )
        for vn in range(len(N)):
            f.write("vn %.4f %.4f %.4f\n" % ( float(V[vn][0]), float(V[vn][1]), float(V[vn][2]) ) )
            
def write_XYZ(filepath, V):
    with open(filepath, 'w') as f:
        f.write("# XYZ file\n")
        for vq in range(len(V)):
            f.write("%.4f %.4f %.4f\n" % ( float(V[vq][0]), float(V[vq][1]), float(V[vq][2]) ) )
            
def write_obj_Textured(filepath,mtlpath,V,N,T,F,Tex): #Tex is vector of material names
    with open(filepath, 'w') as f:
        f.write("# OBJ file\n")
        f.write("mtllib %s\n" % mtlpath)
        for vq in range(len(V)):
            f.write("v %.4f %.4f %.4f\n" % ( float(V[vq][0]), float(V[vq][1]), float(V[vq][2]) ) )
        for vn in range(len(N)):
            f.write("vn %.4f %.4f %.4f\n" % ( float(V[vn][0]), float(V[vn][1]), float(V[vn][2]) ) )
        if (len(F) >1 ):
            
            f.write("usemtl material%i\n" % int(Tex[0][0]))
            f.write("f")
            for j in range(len(F[0])):
                    f.write(" %d" % int(F[0][j]))
            f.write("\n")
            
            for p in range(1,len(F)):
                if (int(Tex[p][0]) != int(Tex[p-1][0])):
                    f.write("usemtl material%i\n" % int(Tex[p][0]))
                    f.write("f")
                    for i in range(len(F[p])):
                        f.write(" %d" % int(F[p][i]))
                    f.write("\n")
                else:
                    f.write("f")
                    for i in range(len(F[p])):
                        f.write(" %d" % int(F[p][i]))
                    f.write("\n")
        elif (len(F) <=1):
            f.write("\n")