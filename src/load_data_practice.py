import numpy
import pandas as pd
import torch
from torch.utils import data


class CSVDataset(data.Dataset):

    def __init__(self, filename):
        super(CSVDataset, self).__init__()
        self.csv = pd.read_csv(filename)
        self.x = self.csv.drop(columns='y')
        self.y = self.csv['y']

    def __getitem__(self, index: int):
        x = torch.tensor(numpy.asarray(self.x.loc[index]))
        y = torch.tensor(numpy.asarray(self.y.loc[index]))
        return {'x':x,'y':y}

    def __len__(self):
        return self.csv.shape[0]


if __name__ == '__main__':

    csv_filepath = '../data/csv/linear.csv'
    csv = CSVDataset(csv_filepath)
    print('number of samples:',len(csv))
    print(csv[1])



