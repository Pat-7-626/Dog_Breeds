from dog_data import DogDataset
from dog_ui import DogUI

if __name__ == "__main__":
    d_1 = DogDataset("dog_breeds_1")
    d_2 = DogDataset("dog_breeds_2")
    d_3 = DogDataset("dog_breeds_3")
    app = DogUI(d_1, d_2, d_3)
    app.mainloop()
