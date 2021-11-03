import pandas as pd
import numpy as np
from scipy.sparse import data
from sklearn.model_selection import train_test_split

class Explorer:
    def __init__(self, data, dependentVars, ratio=0.8) -> None:
        self.data = data
        self.dependentVars = dependentVars
        self.X, self.y = self.splitXy()
        self.askRegOrClass()
        self.askContOrDisc()

    def splitXy(self):
        X = self.data.drop(self.dependentVars, axis=1)
        y = self.findDependentVars()
        return X, y

    def findDependentVars(self):
        try:
            depVars = self.data[self.dependentVars]
            return depVars
        except:
            raise Exception("Dependent Variables not found")
    
    def splitTrainTest(self, df, ratio):
        msk = np.random.rand(len(df)) < 0.8
        train, test = df[msk], df[~msk]
        return train, test

    def askRegOrClass(self):
        print(self.dependentVars, 'has ', self.y[self.dependentVars].nunique(), 'unique entries out of', self.y[self.dependentVars].count(),'entries belonging to',
            self.y[self.dependentVars].dtypes,'datatype')
        type = input('Is dicrete or continuous? Press d for discrete and c for continuous.')
        if type == 'd':
            print('It is a classification problem')
        elif type == 'c':
            print('It is a regression problem')
        else:
            pass
        
    def askContOrDisc(self):
        cont = pd.DataFrame()
        disc = pd.DataFrame()
        for col in self.X:
            # print no entries, unique entries and null values
            print(col, 'has ', self.X[col].nunique(), 'unique entries out of', self.X[col].count(),'entries belonging to',
            self.X[col].dtype,'datatype')
            type = input('Is dicrete or continuous? Press d for discrete and c for continuous.')
            if type == 'd':
                # add column to dataframe
                cont[col] = self.X[col]
            elif type == 'c':
                # add column to dataframe
                disc[col] = self.X[col]
            else:
                pass
        print(cont.shape, disc.shape)
        return cont, disc

    def printDescription(self):
        print('Description:', self.data.describe())

    def printInfo(self):
        print('Information:', self.data.info())

if __name__ == '__main__':
    from Data import fetch
    data = fetch.from_csv('Data/telecom_churn.csv')
    dataExp = Explorer(data, ['Churn'])
