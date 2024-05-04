import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import webbrowser


class DogUI(tk.Tk):
    def __init__(self, d1, d2, d3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Dog Breeds")
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.pages = {}
        self.pages_his = {}
        self.entry_story = None
        self.v1 = None
        self.v2 = None
        self.v3 = None
        self.init_page()
        self.show_page("home")

    def init_page(self):
        for i in ["home", "dog_list",
                  "story", "DSC", "histogram",
                  "IvsA", "IvsF", "AvsF",
                  "Intell", "Adapt", "Friend",
                  "final"]:
            page = tk.Frame(self)
            self.pages[i] = page
        self.init_home()
        self.init_dog_list()
        self.init_story()
        self.init_histogram()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)

    def init_menu(self, name):
        button_home = tk.Button(self.pages[name],
                                text="Home",
                                command=lambda:
                                self.show_page("home"),
                                font=('Arial', 25))
        button_exit = tk.Button(self.pages[name],
                                text="Exit",
                                command=self.quit,
                                font=('Arial', 25))
        space = tk.Label(self.pages[name],
                         text="Pattharamon Dumrongkittikule 6610545472",
                         font=('Arial', 20))
        button_home.grid(column=0,
                         row=0,
                         sticky=tk.NSEW,
                         columnspan=3,
                         padx=20,
                         pady=10,
                         ipadx=100,
                         ipady=0)
        button_exit.grid(column=3,
                         row=0,
                         sticky=tk.NSEW,
                         columnspan=3,
                         padx=20,
                         pady=10,
                         ipadx=100,
                         ipady=0)
        space.grid(column=0,
                   row=1,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=0,
                   ipadx=100,
                   ipady=0)

    def init_home(self):
        name_var = tk.StringVar()
        title = tk.Label(self.pages["home"],
                         text="Dog Breeds",
                         font=('Arial', 25))
        button_source = tk.Button(self.pages["home"],
                                  text="Source",
                                  command=lambda:
                                  webbrowser.open("https://www.kaggle.com"
                                                  "/datasets/mexwell/dog"
                                                  "-breeds-dogtime-dataset"),
                                  font=('Arial', 15))
        button_dog_list = tk.Button(self.pages["home"],
                                    text="All dog breeds",
                                    command=lambda:
                                    self.show_page("dog_list"),
                                    font=('Arial', 15))
        button_story = tk.Button(self.pages["home"],
                                 text="Data Storytelling Results",
                                 command=lambda:
                                 self.show_page("story"),
                                 font=('Arial', 15))
        self.entry_story = tk.Entry(self.pages["home"],
                                    textvariable=name_var,
                                    font=('Arial', 20))
        title.grid(column=0,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=2,
                   rowspan=2,
                   padx=20,
                   pady=5,
                   ipadx=50,
                   ipady=0)
        button_source.grid(column=2,
                           row=2,
                           sticky=tk.NSEW,
                           columnspan=2,
                           padx=20,
                           pady=5,
                           ipadx=50,
                           ipady=0)
        button_dog_list.grid(column=4,
                             row=2,
                             sticky=tk.NSEW,
                             columnspan=2,
                             padx=20,
                             pady=5,
                             ipadx=50,
                             ipady=0)
        button_story.grid(column=4,
                          row=3,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=20,
                          pady=5,
                          ipadx=50,
                          ipady=0)
        self.entry_story.grid(column=0,
                              row=4,
                              sticky=tk.NSEW,
                              columnspan=6,
                              padx=20,
                              pady=20,
                              ipadx=50,
                              ipady=0)
        self.entry_story.insert(0, "Entry here")
        self.entry_story.bind("<FocusIn>", self.focus_in)
        self.entry_story.bind("<FocusOut>", self.focus_out)
        self.entry_story.bind('<Return>', self.show_dog_solo)

    def init_dog_solo(self, name, index):
        ori_list = self.d1.get_list("Breed Name")
        ori_name = ori_list[index]
        title = tk.Label(self.pages[name],
                         text=ori_name)
        title.grid(column=0,
                   row=2)

    def init_dog_list(self):
        title = tk.Label(self.pages["dog_list"],
                         text="Dog Breeds")
        title.grid(column=0,
                   row=2)

    def init_story(self):
        title = tk.Label(self.pages["story"],
                         text="Data Storytelling Results",
                         font=('Arial', 25))
        des = tk.Label(self.pages["story"],
                       text="Topic: The relationship between Intelligence, "
                            "Adaptability and Friendliness",
                       font=('Arial', 15))
        button_histogram = tk.Button(self.pages["story"],
                                     text="The histogram of all level of "
                                          "Intelligence, Adaptability, "
                                          "and Friendliness",
                                     command=lambda:
                                     self.show_page("histogram"),
                                     font=('Arial', 15))
        button_IvsA = tk.Button(self.pages["story"],
                                text="Intelligence vs Adaptability",
                                command=lambda:
                                self.show_page("IvsA"),
                                font=('Arial', 15))
        button_IvsF = tk.Button(self.pages["story"],
                                text="Intelligence vs Friendliness",
                                command=lambda:
                                self.show_page("IvsF"),
                                font=('Arial', 15))
        button_AvsF = tk.Button(self.pages["story"],
                                text="Adaptability vs Friendliness",
                                command=lambda:
                                self.show_page("AvsF"),
                                font=('Arial', 15))
        button_Intell = tk.Button(self.pages["story"],
                                  text="Intelligence",
                                  command=lambda:
                                  self.show_page("Intell"),
                                  font=('Arial', 15))
        button_Adapt = tk.Button(self.pages["story"],
                                 text="Adaptability",
                                 command=lambda:
                                 self.show_page("Adapt"),
                                 font=('Arial', 15))
        button_Friend = tk.Button(self.pages["story"],
                                  text="Friendliness",
                                  command=lambda:
                                  self.show_page("Friend"),
                                  font=('Arial', 15))
        button_DSC = tk.Button(self.pages["story"],
                               text="Descriptive Statistics and Correlations",
                               command=lambda:
                               self.show_page("DSC"),
                               font=('Arial', 15))
        button_final = tk.Button(self.pages["story"],
                                 text="The story from the dataset",
                                 command=lambda:
                                 self.show_page("final"),
                                 font=('Arial', 15))
        title.grid(column=0,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=100,
                   ipady=0)
        des.grid(column=0,
                 row=3,
                 sticky=tk.NSEW,
                 columnspan=6,
                 padx=20,
                 pady=5,
                 ipadx=100,
                 ipady=0)
        button_histogram.grid(column=0,
                              row=4,
                              sticky=tk.NSEW,
                              columnspan=6,
                              padx=20,
                              pady=5,
                              ipadx=100,
                              ipady=0)
        button_IvsA.grid(column=0,
                         row=5,
                         sticky=tk.NSEW,
                         columnspan=2,
                         padx=20,
                         pady=5,
                         ipadx=100,
                         ipady=0)
        button_IvsF.grid(column=2,
                         row=5,
                         sticky=tk.NSEW,
                         columnspan=2,
                         padx=20,
                         pady=5,
                         ipadx=100,
                         ipady=0)
        button_AvsF.grid(column=4,
                         row=5,
                         sticky=tk.NSEW,
                         columnspan=2,
                         padx=20,
                         pady=5,
                         ipadx=100,
                         ipady=0)
        button_Intell.grid(column=0,
                           row=6,
                           sticky=tk.NSEW,
                           columnspan=2,
                           padx=20,
                           pady=5,
                           ipadx=100,
                           ipady=0)
        button_Adapt.grid(column=2,
                          row=6,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=20,
                          pady=5,
                          ipadx=100,
                          ipady=0)
        button_Friend.grid(column=4,
                           row=6,
                           sticky=tk.NSEW,
                           columnspan=2,
                           padx=20,
                           pady=5,
                           ipadx=100,
                           ipady=0)
        button_DSC.grid(column=0,
                        row=7,
                        sticky=tk.NSEW,
                        columnspan=6,
                        padx=20,
                        pady=5,
                        ipadx=100,
                        ipady=0)
        button_final.grid(column=0,
                          row=8,
                          sticky=tk.NSEW,
                          columnspan=6,
                          padx=20,
                          pady=5,
                          ipadx=100,
                          ipady=0)

    def init_histogram(self):
        sub_page = tk.Frame(self.pages["histogram"])
        his_page = tk.Frame(self.pages["histogram"])
        self.pages_his["sub_page"] = sub_page
        self.pages_his["his_page"] = his_page
        title = tk.Label(self.pages_his["sub_page"],
                         text="The histogram of all level of Intelligence, "
                              "Adaptability, and Friendliness",
                         font=('Arial', 25))
        self.v1 = tk.BooleanVar()
        self.v2 = tk.BooleanVar()
        self.v3 = tk.BooleanVar()
        self.v1.set(True)
        self.v2.set(True)
        self.v3.set(True)
        self.his_change()
        check_intell = tk.Checkbutton(self.pages_his["sub_page"],
                                      text="Intelligence",
                                      variable=self.v1,
                                      command=self.his_change,
                                      font=('Arial', 15))
        check_Adapt = tk.Checkbutton(self.pages_his["sub_page"],
                                     text="Adaptability",
                                     variable=self.v2,
                                     command=self.his_change,
                                     font=('Arial', 15))
        check_Friend = tk.Checkbutton(self.pages_his["sub_page"],
                                      text="Friendliness",
                                      variable=self.v3,
                                      command=self.his_change,
                                      font=('Arial', 15))
        sub_page.grid(column=0,
                      row=2,
                      sticky=tk.NSEW,
                      columnspan=6)

        his_page.grid(column=0,
                      row=3,
                      sticky=tk.NSEW,
                      columnspan=6)
        title.grid(column=0,
                   row=0,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=100,
                   ipady=0)
        check_intell.grid(column=0,
                          row=1,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=20,
                          pady=5,
                          ipadx=100,
                          ipady=0)
        check_Adapt.grid(column=2,
                         row=1,
                         sticky=tk.NSEW,
                         columnspan=2,
                         padx=20,
                         pady=5,
                         ipadx=100,
                         ipady=0)
        check_Friend.grid(column=4,
                          row=1,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=20,
                          pady=5,
                          ipadx=100,
                          ipady=0)

    def show_page(self, name):
        for page in self.pages.values():
            page.grid_forget()
        self.pages[name].grid(row=0,
                              column=0)
        self.init_menu(name)
        self.pages["home"].focus_set()

    def show_dog_solo(self, event):
        ori_name = self.entry_story.get()
        name = ori_name.lower().replace(" ", "")
        ori_list = self.d1.get_list("Breed Name")
        name_list = [i.lower().replace(" ", "") for i in ori_list]
        self.pages["home"].focus_set()
        if name not in name_list:
            messagebox.showwarning(f"No {ori_name}",
                                   f"There is no {ori_name}.")
        else:
            if name not in self.pages.keys():
                page = tk.Frame(self)
                self.pages[name] = page
                self.init_dog_solo(name, name_list.index(name))
                self.show_page(name)
            else:
                self.show_page(name)

    def focus_in(self, event):
        self.entry_story.delete(0, tk.END)

    def focus_out(self, event):
        self.entry_story.delete(0, tk.END)
        self.entry_story.insert(0, "Entry here")

    @staticmethod
    def histogram(page, column, row, span, df, x, name, x_name, y_name):
        fig, ax = plt.subplots()
        sns.histplot(data=df,
                     x=x,
                     binwidth=1,
                     kde=True,
                     ax=ax, )
        ax.set_xlabel(x_name,
                      fontsize=15,
                      fontfamily='Arial')
        ax.set_ylabel(y_name,
                      fontsize=15,
                      fontfamily='Arial')
        ax.set_title(name,
                     fontsize=15,
                     fontfamily='Arial')
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)

    def his_change(self):
        self.pages_his["his_page"].grid_forget()
        his_page = tk.Frame(self.pages["histogram"])
        self.pages_his["his_page"] = his_page
        self.pages_his["his_page"].grid(column=0,
                                        row=3,
                                        columnspan=6)
        all_list = []
        name_list = []
        if not self.v1.get() and not self.v2.get() and not self.v3.get():
            messagebox.showwarning(f"Can't uncheck all",
                                   f"You can't uncheck all three.")
            self.v1.set(True)
            self.v2.set(True)
            self.v3.set(True)
        if self.v1.get():
            all_list += self.d1.get_list("Intelligence")
            name_list.append("Intelligence")
        if self.v2.get():
            all_list += self.d1.get_list("Adaptability")
            name_list.append("Adaptability")
        if self.v3.get():
            all_list += self.d1.get_list("Adaptability")
            name_list.append("Adaptability")
        df = pd.DataFrame({"histogram_list": all_list})
        name = ", ".join(name_list)
        self.histogram(self.pages_his["his_page"],
                       0,
                       3,
                       6,
                       df,
                       "histogram_list",
                       "The histogram of all levels of "
                       f"{name}",
                       "Level",
                       "Frequency")
