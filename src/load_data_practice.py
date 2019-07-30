import pandas as pd
from torch.utils import data


class CSVDataset(data.Dataset):

    def __init__(self, filename):
        super(CSVDataset, self).__init__()
        self.csv = pd.read_csv(filename, iterator=True)

    def __getitem__(self, index: int):
        pass

    def __len__(self):
        pass


if __name__ == '__main__':

    csv_filepath = '../data/csv/'

