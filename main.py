import argparse

import Data
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-source', default='Data\train.csv', help='path of data file')
parser.add_argument('-type', default=None)
args = parser.parse_args()

data = pd.read_csv(r'Data\train.csv')
print(data.head)