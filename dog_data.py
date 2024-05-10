import pandas as pd
import os


class CSVDataset:

    def __init__(self, csv_directory):
        self.csv_directory = csv_directory
        self.csv_files = [file for file in os.listdir(csv_directory) if
                          file.endswith('.csv')]
        self.dataframes_dict = {}

    def import_csv(self):
        for file in self.csv_files:
            file_path = os.path.join(self.csv_directory, file)
            name = file.split('.')[0]
            self.dataframes_dict[name] = pd.read_csv(file_path)

    def get_csv(self, name):
        return self.dataframes_dict.get(name, None)


class DogDataset:
    def __init__(self, name):
        csv = CSVDataset("dataset/")
        csv.import_csv()
        self.d = csv.get_csv(name)

    def get_list(self, column_name):
        return self.d[column_name].tolist()
