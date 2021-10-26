import pandas as pd

def from_csv(path):
    data = pd.read_csv(path)
    return data

if __name__ == '__main__':
    from_csv('Data/train.csv')