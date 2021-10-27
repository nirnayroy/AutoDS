import numpy as np
from sklearn.model_selection import train_test_split

class Explorer:
    def __init__(self, data, dependentVars, ratio=0.8) -> None:
        self.data = data
        self.categorical, self.numerical = self.separateCatNum()
        self.dependentVars = dependentVars
        self.X, self.y = self.splitXy()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, 
                                                                                self.y)

    def separateCatNum(self):
        categorical = self.data.select_dtypes(include=[object]).astype("category")
        numerical = self.data.select_dtypes(exclude=[object])
        return categorical, numerical
   
    def findDependentVars(self):
        try:
            depVars = self.data[self.dependentVarsdependentVars]
            return depVars
        except:
            raise Exception("Dependent Variables not found")
    
    def splitTrainTest(self, df, ratio):
        msk = np.random.rand(len(df)) < 0.8
        train, test = df[msk], df[~msk]
        return train, test
    
    def splitXy(self):
        X = self.data.drop(self.dependentVars, axis=1)
        y = self.data[self.dependentVars]
        return X, y


    
    def findCategories(self):
        for col in self.categorical:
            print(col, ':',dataExp.categorical[col].cat.categories)

    def printDescription(self):
        print(self.data.describe())

    def printInfo(self):
        print(self.data.info())


if __name__ == '__main__':
    from Data import fetch
    data = fetch.from_csv('Data/train.csv')
    dataExp = Explorer(data, ['SalePrice'])
    print(len(dataExp.X))
    print(len(dataExp.X_train))
