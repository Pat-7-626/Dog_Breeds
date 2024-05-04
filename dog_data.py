from csv_file import CSVDataset


class DogDataset:
    def __init__(self, name):
        csv = CSVDataset("dataset/")
        csv.import_csv()
        self.df = csv.get_csv(name)

    def get_list(self, column_name):
        return self.df[column_name].tolist()


dog_1 = DogDataset("dog_breeds_2")


