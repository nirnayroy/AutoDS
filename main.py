import argparse
from Data import fetch
import explore
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-source', default='Data/train.csv', help='path of data file')
parser.add_argument('-type', default=None)
args = parser.parse_args()

data = fetch.from_csv(args.source)

explore.describe(data)