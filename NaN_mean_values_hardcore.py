class CSVFile():
    def __init__(self):
        self.arquivo = None
        self.data = list()
    # self.data armazena uma lista contendo as linhas do arquivo csv
    def read_file(self, filePath):
        try: 
            f = open(filePath,"r")
            data = f.readlines()
            self.data = list(map(lambda line: line.split(";"), data) )
            f.close()
        except IOError as e:
            print (e.args)
            
        return self.data
    
class wana_hardcore:
    def __init__(self):
        self.nan_means = []
        self.dictionary = {}
    def if_else(self, word):
        return 1 if (word == '' )\
                or (word == 'Sem Informações') else 0
    def count_nan(self, r):
        qtdColumn = len(r[0])
        a = [i.strip('\n') for i in r[0]]
        r = r[1:]
        col = [(sum([self.if_else(r[i][j].strip('\n'))\
                for i in range(len(r)-1)]))/len([self.if_else(r[i][j].strip('\n'))\
                        for i in range(len(r)-1)]) for j in range(qtdColumn)]
        self.nan_means = list(zip(a, col)) # return list
        self.dictionary =  {k:v for k,v in zip(a,col)} # return dictionary
        return self.dictionary
    
a = wana_hardcore()
cfile = CSVFile()
r = cfile.read_file('portalbio_export_16-10-2019-14-39-54.csv')
b = a.count_nan(r)
print(b)
