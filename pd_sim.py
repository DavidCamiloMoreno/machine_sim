class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self, indice):
        print('indice',indice)
        if isinstance(indice,slice):
            print('slice',indice.start,indice.step,indice.stop)
<<<<<<< HEAD
    def head(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]
=======

    def iat(self,row,column):
        a=self.data
        b=a[row]
        c=b[column]
        print(c)
        
>>>>>>> origin/main

            
def __getitem__(self,i):
        print ("Indice: ",i) 
 
 
def funcion_tail(arch, n):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]
 
 

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        titulo=titulo.strip()
        data[titulo]=[]
        titulos.append(titulo)
        
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem.strip())
    return DataFrame(data)         


#prueba
d=read_csv('datos.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])

#x=sum(map(len,d.data.values()))
#print(x)




for t in d.data:
   print (t, ":", d.data[t])
   

  
print ("\n",funcion_tail("datos.csv",5))  
            
        
#pruebaaa
d=read_csv('datos.csv')
print(d.data)

#prueba Willian
#d=read_csv('datos.csv')
#print(d.data)
z=len(funcion_tail("datos.csv",5))

print ("\n",funcion_tail("datos.csv",5))

strA="".join(funcion_tail("datos.csv",5))

print(strA)

print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])

            
        
#prueba
d=read_csv('datos.csv')
print(d.data)

def loc (columna,fila=None): #Función para seleccionar por etiquetas (loc), identificar filas y columnas identificando si es un str, int, slice.
    dat=titulo
    fila=titulo

    
#prueba
d=read_csv('csv.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])
