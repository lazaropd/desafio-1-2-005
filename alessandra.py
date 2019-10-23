class alessandra():
    __arq = ''
    __txt = []
    __sep = ""

    def __init__(self, path, sep):
        self.__arq = open(path, 'r')
        self.__txt = self.__arq.readlines()
        self.__sep = sep

    def __structlist(self):
        lst = [[a.replace("\n", "") for a in y.split(self.__sep)] for y in self.__txt]
        return lst

    def __column(self):
        org = self.__structlist()
        out = []
        for i in range(len(org[0])):
            b = [a[i] for a in org]
            out.append(b)
        return out

    def orfilter(self, cat, status):
        # Filtra as ocorrencias que possui ao menos uma caracteristica indicada
        if len(cat) != len(status):
            print("Erro")
        else:
            ref = []
            out = []
            a = 0
            data = self.__column()
            pos = [[i for i in data if i[0] == a] for a in cat]
            for y in range(len(pos)):
                ref.append(pos[y][0])
            output = []
            for list in ref:
                for info in list:
                    for par in status:
                        b = self.__txt[a].replace("\n", "")
                        if info == par and b not in out:
                            output.append(b)
                    a +=1
                a = 0
        return output

    def andfilter(self, cat, status):
        # Filtra as ocorrencias que possuem todas as caracteristicas indicadas
        if len(cat) != len(status):
            print("Erro")
        else:
            ref = []
            out = []
            a = 0
            data = self.__column()
            output = []
            pos = [[i for i in data if i[0] == a] for a in cat]
            for y in range(len(pos)):
                ref.append(pos[y][0])
            for i in ref:
                for k in range(len(i)):
                    for n in range(0, len(status)):
                        out.append(ref[n][k])
                        b = self.__txt[a].replace("\n", "")
                        if out == status and b not in output:
                            output.append(b)
                    out = []
                    a+=1
                a=0
        return output

"""obj = alessandra('/home/alessandra/PycharmProjects/tensorEnv/bd/bd0.csv',";")
keywords = ['Localidade','Categoria de Ameaca']
values = ['Engenho Sacramento','Vulnerável']
#obj.orfilter(keywords,values)
print(obj.andfilter(keywords,values))"""
