import pandas as pd
import numpy as np
from scipy.sparse import data
from sklearn.model_selection import train_test_split

class Explorer:
    def __init__(self, data, dependentVars, ratio=0.8) -> None:
        self.data = data
        self.dependentVars = dependentVars
        self.X, self.y = self.splitXy()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, 
                                                                                self.y)
        #self.categorical, self.numerical = self.separateCatNum()
        self.printOutputType()

    def splitXy(self):
        X = self.data.drop(self.dependentVars, axis=1)
        y = self.findDependentVars()
        return X, y

    def separateCatNum(self):
        categorical = self.X_train.select_dtypes(include=[object]).astype("category")
        numerical = self.X_train.select_dtypes(exclude=[object])
        return categorical, numerical

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
    
    def findCategories(self):
        for col in self.categorical:
            print(col, ':', data.categorical[col].cat.categories)

    def askContOrDisc(self):
        cont = pd.DataFrame()
        disc = pd.DataFrame()
        for col in self.X:
            # print no entries, unique entries and null values
            print(col, 'has ', len(self.X[col].unique()), ' unique entries out of', len(self.X[col]),'entries belonging to',
            self.X[col].dtype,'datatype')
            type = input('Is dicrete or continuous? Press d for discrete and c for continuous.')
            if type == 'd':
                # add column to dataframe
                cont[col] = self.X[col]
            else:
                # add column to dataframe
                disc[col] = self.X[col]

    def printOutputType(self):
        print('Output Type:', self.y_train.dtypes)

    def printDescription(self):
        print('Description:', self.data.describe())

    def printInfo(self):
        print('Information:', self.data.info())

if __name__ == '__main__':
    from Data import fetch
    data = fetch.from_csv('Data/train.csv')
    dataExp = Explorer(data, ['SalePrice'])
    dataExp.askContOrDisc()
