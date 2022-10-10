class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self, indice):
        print('indice',indice)
        if isinstance(indice,slice):
            print('slice',indice.start,indice.step,indice.stop)
    def head(arch, n, sep=';'):
        with open(arch) as f:
        lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]


def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo)
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)
            
        
#prueba
d=read_csv('csv.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])
