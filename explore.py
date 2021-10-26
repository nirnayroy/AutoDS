def describe(data):
    print(data.describe())


if __name__ == '__main__':
    from Data import fetch
    data = fetch.from_csv('Data/train.csv')
    describe(data)