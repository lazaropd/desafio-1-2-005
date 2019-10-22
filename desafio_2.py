
import pandas as pd

from itertools import islice

from read_file import CSVFile


class Lazaro:
    
    __COLUMNS = ['Filo', 'Classe', 'Ordem', 'Familia', 'Genero', 'Especie']
    
    def __init__(self, content):
        if type(content) == str:
            cfile = CSVFile()
            cfile.read_file(content)
            self.df_columns = cfile.data[0]
            self.df_taxonomy = pd.DataFrame(cfile.data[1:], columns=self.df_columns)
            print("Content loaded")
        elif type(content) == list:
            self.df_columns = content[0]
            self.df_taxonomy = pd.DataFrame(content[1:], columns=self.df_columns)
            print("Content loaded")
        else:
            self.df_taxonomy = None
            print("Invalid input object. Please inform file_path or list of rows")
        
    def extract_taxonomy_subset(self):
        self.df_taxonomy_filtered = self.df_taxonomy[self.__COLUMNS]
    
    def get_last_filled(self, columns):
        filled_columns = [column for column in columns if column != "Sem Informações"]
        return self.__COLUMNS[len(filled_columns)-1]
    
    def extract_taxonomic_level(self, graph=False):
        self.df_taxonomy['Nível Taxonômico'] = self.df_taxonomy_filtered.apply(lambda x: self.get_last_filled(x), axis=1)
        if graph: self.df_taxonomy['Nível Taxonômico'].value_counts().plot()

    def get_taxonomy(self, content, top=5):
        content.extract_taxonomy_subset()
        content.extract_taxonomic_level()
        self.taxonomic_level = {linha: content.df_taxonomy['Nível Taxonômico'].iloc[linha] for linha in content.df_taxonomy.index}
        self.sample = {item:self.taxonomic_level[item] for item in islice(taxonomy.taxonomic_level, top)}
       



# call class using csv file path
if __name__ == "__main__":
    filePath = "portalbio_export_16-10-2019-14-39-54.csv"
    taxonomy = Lazaro(filePath)
    taxonomy.get_taxonomy(taxonomy)
    print("\nColumns:\n", taxonomy.df_columns)
    taxonomy.extract_taxonomy_subset()
    print("\nSample:\n", taxonomy.df_taxonomy_filtered[0:2].T)
    taxonomy.extract_taxonomic_level(graph=True)
    print("\nSample:\n", taxonomy.df_taxonomy[0:1].T)
    print(taxonomy.sample)
    #see taxonomic_level and df_taxonomy for more detailed results

"""
# call class using csv content
if __name__ == "__main__":
    filePath = "portalbio_export_16-10-2019-14-39-54.csv"
    cfile = CSVFile()
    cfile.read_file(filePath)
    taxonomy = Lazaro(cfile.data)
    taxonomy.get_taxonomy(taxonomy)
    print("\nColumns:\n", taxonomy.df_columns)
    taxonomy.extract_taxonomy_subset()
    print("\nSample:\n", taxonomy.df_taxonomy_filtered[0:2].T)
    taxonomy.extract_taxonomic_level()
    print("\nSample:\n", taxonomy.df_taxonomy[0:1].T)
    print(taxonomy.sample)
    #see taxonomic_level and df_taxonomy for more detailed results
"""



# call class using list of csv rows
#cfile = CSVFile()
#cfile.read_file(filePath)
#cfile = Lazaro(cfile.data)
#cfile.extract_taxonomy_subset()
#print(cfile.df_taxonomy_filtered[0:3].T)

