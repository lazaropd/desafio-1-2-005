import pandas as pd
import numpy as np

# get the mean of NaN values from each column in the dataset
class wana:
    index = []
    data_mean = None
    data_NaN = pd.DataFrame() # empty dataframe
    def __init__(self, file):
        self.file = file
    def read_file(self):
        df = pd.read_csv(self.file, header=0, sep=';') #reading my file
        for i in df: # for in dataframe's columns
            self.data_NaN[i] = np.where((df[i] == '') | (df[i]== 'Sem Informações'),1, 0) # filling my empty dataframe by conditions: where my conditions are true it sets 1 and zero when false

    def show_data(self):
        self.read_file()
        data = self.data_NaN.mean()
        data = data.reset_index().set_index('index', True)
        data['média de valores ausentes'] = data[0]
        self.data_mean = data.drop(0, axis=1)
        
        return self.data_mean

csvfile = wana('portalbio_export_16-10-2019-14-39-54.csv')
mean = csvfile.show_data()

print(mean)
