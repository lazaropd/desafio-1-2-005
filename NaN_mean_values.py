import pandas as pd
import numpy as np

# get the mean of NaN values for each column in the dataset
class wana:
    def read_file(self, file):
        data_NaN = pd.DataFrame() # creating a an empty dataframe
        df = pd.read_csv(file, header=0, sep=';') #reading my file
        for i in df: # for in dataframe's columns
            data_NaN[i] = np.where((df[i] == '') | (df[i]== 'Sem Informações'),1, 0) # filling my empty dataframe by conditions: where my conditions are true it sets 1 and zero when false
        return data_NaN

linha = wana()
data_mean = linha.read_file('portalbio_export_16-10-2019-14-39-54.csv')S
data_mean = data_mean.mean()
print(data_mean.mean)
