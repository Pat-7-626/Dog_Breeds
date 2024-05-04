from csv_file import CSVDataset


class DogDataset:
    def __init__(self, name):
        csv = CSVDataset("dataset/")
        csv.import_csv()
        self.d = csv.get_csv(name)

    def get_list(self, column_name):
        return self.d[column_name].tolist()