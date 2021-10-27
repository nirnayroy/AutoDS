from pandas.core.arrays import categorical

class Explorer:
    def __init__(self, data, dependentVars) -> None:
        self.data = data
        self.categorical, self.numerical = self.separateCatNum()
        self.dependentVar = self.findDependentVars(dependentVars)

    def separateCatNum(self):
        categorical = self.data.select_dtypes(include=[object])
        numerical = self.data.select_dtypes(exclude=[object])
        return categorical, numerical
   
    def findDependentVars(self, dependentVars):
        try:
            depVars = self.data[dependentVars]
            return depVars
        except:
            raise Exception("Dependent Variables not found")

    def describe(self):
        print(self.data.describe())

    def info(self):
        print(self.data.info())


if __name__ == '__main__':
    from Data import fetch
    data = fetch.from_csv('Data/train.csv')
    dataExp = Explorer(data, ['SalePrice'])
    print(dataExp.dependentVar)