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
        return x,y

    def __len__(self):
        return self.csv.shape[0]


if __name__ == '__main__':

    csv_filepath = '../data/csv/linear.csv'
    csv = CSVDataset(csv_filepath)
    print('number of samples:',len(csv))

    dataloader = torch.utils.data.DataLoader(dataset=csv, batch_size=20)

    for epoch in range(2):
        for i, data in enumerate(dataloader):
            input, label = data
            print('epoch:', epoch, ' batch:', i, ' input:', input.size(), 'output:', label.size())
