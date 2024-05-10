import pandas as pd
import os


class CSVDataset:
    """
    CSV Dataset import
    """

    def __init__(self, csv_directory):
        """
        init
        :param csv_directory: str
        """
        self.csv_directory = csv_directory
        self.csv_files = [file for file in os.listdir(csv_directory) if
                          file.endswith('.csv')]
        self.dataframes_dict = {}

    def import_csv(self):
        """
        import CSV
        :return: none
        """
        for file in self.csv_files:
            file_path = os.path.join(self.csv_directory, file)
            name = file.split('.')[0]
            self.dataframes_dict[name] = pd.read_csv(file_path)

    def get_csv(self, name):
        """
        get DSV
        :param name: str
        :return: pd.DataFrame
        """
        return self.dataframes_dict.get(name, None)


class DogDataset:
    """
    Dog Dataset
    """

    def __init__(self, name):
        """
        init
        :param name: str
        """
        csv = CSVDataset("dataset/")
        csv.import_csv()
        self.d = csv.get_csv(name)

    def get_list(self, column_name):
        """
        get the list of the data
        :param column_name: str
        :return: list
        """
        return self.d[column_name].tolist()
