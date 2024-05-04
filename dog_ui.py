import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import webbrowser
import tkinter as tk
from tkinter import ttk
from dog_data import DogDataset


class DogUI:
    def __init__(self, root):
        self.entry_story = None
        self.root = root
        self.root.title("Dog Breeds")
        self.pages = {}
        self.init_page()
        self.show_page("home")

    def init_page(self):
        for i in ["home", "dog_list",
                  "story", "DSC", "histogram",
                  "IvsH", "SvsD", "TvsA",
                  "In", "Kid", "To", "final"]:
            page = tk.Frame(self.root)
            self.pages[i] = page
            self.init_home()

    def init_home(self):
        name_var = tk.StringVar()
        title = tk.Label(self.pages["home"],
                         text="Dog Breeds")
        button_source = tk.Button(self.pages["home"],
                                  text="Source",
                                  command=lambda:
                                  webbrowser.open("https://www.kaggle.com"
                                                  "/datasets/mexwell/dog"
                                                  "-breeds-dogtime-dataset"))
        button_dog_list = tk.Button(self.pages["home"],
                                    text="All dog breeds",
                                    command=lambda:
                                    self.show_page("dog_list"))
        button_story = tk.Button(self.pages["home"],
                                 text="Data Storytelling Results",
                                 command=lambda:
                                 self.show_page("story"))
        self.entry_story = tk.Entry(self.pages["home"],
                                    textvariable=name_var)

        title.grid(column=0,
                   row=1)
        button_source.grid(column=1,
                           row=1)
        button_dog_list.grid(column=2,
                             row=1)
        button_story.grid(column=0,
                          row=2)
        self.entry_story.grid(column=0,
                              row=3)

        self.entry_story.bind('<Return>', self.show_dog_solo)

    def init_menu(self, name):
        button_home = tk.Button(self.pages[name],
                                text="Home",
                                command=lambda:
                                self.show_page("home"))
        button_exit = tk.Button(self.pages[name],
                                text="Exit",
                                command=self.root.quit)

        button_home.grid(column=0,
                         row=0)
        button_exit.grid(column=1,
                         row=0)

    def show_page(self, name):
        for page in self.pages.values():
            page.grid_forget()
        self.pages[name].grid(row=0, column=0)
        self.init_menu(name)

    def show_dog_solo(self, event):
        name = self.entry_story.get()
        if name not in self.pages.keys():
            page = tk.Frame(self.root)
            self.pages[name] = page
        self.show_page(name) # check if exist




if __name__ == "__main__":
    root = tk.Tk()
    app = DogUI(root)
    root.mainloop()
