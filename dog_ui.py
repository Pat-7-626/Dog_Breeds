import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import webbrowser


class DogUI(tk.Tk):
    blue = "#80A1C1"
    vanilla = "#EEE3AB"
    bone = "#D9CFC1"
    brown = "#A77E58"
    red = "#BA3F1D"
    font = "Terminal"
    font_fam = "monospace"

    def __init__(self, d1, d2, d3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.pages = {}
        self.pages_2 = {}
        self.scat = {}
        self.name_var = tk.StringVar()
        self.v1 = tk.BooleanVar()
        self.v2 = tk.BooleanVar()
        self.v3 = tk.BooleanVar()
        self.list_Intell_var = [tk.BooleanVar(), tk.BooleanVar(),
                                tk.BooleanVar(), tk.BooleanVar(),
                                tk.BooleanVar()]
        self.list_Adapt_var = [tk.BooleanVar(), tk.BooleanVar(),
                               tk.BooleanVar(), tk.BooleanVar(),
                               tk.BooleanVar()]
        self.list_Friend_var = [tk.BooleanVar(), tk.BooleanVar(),
                                tk.BooleanVar(), tk.BooleanVar(),
                                tk.BooleanVar()]
        self.entry_story = None
        self.title("Dog Breeds")
        self.configure(bg=self.blue,
                       borderwidth=35,
                       cursor="hand2")
        self.init_page()
        self.show_page("home")
        self.focus_force()
        self.protocol("WM_DELETE_WINDOW", self.close_window_and_exit)

    def init_page(self):
        for i in ["home", "dog_list",
                  "story", "DSC", "histogram",
                  "IvsA", "IvsF", "AvsF",
                  "Intell", "Adapt", "Friend",
                  "final"]:
            page = tk.Frame(self,
                            bg=self.blue)
            self.pages[i] = page
        self.init_home()
        self.init_dog_list()
        self.init_story()
        self.init_histogram()
        self.init_IvsA()
        self.init_IvsF()
        self.init_AvsF()
        self.init_Intell()
        self.init_Adapt()
        self.init_Friend()
        self.init_DSC()
        self.columnconfigure(0,
                             weight=100)
        self.rowconfigure(0,
                          weight=100)

    def init_menu(self, name):
        button_home = tk.Button(self.pages[name],
                                text="Home",
                                command=lambda:
                                self.show_page("home"),
                                font=(self.font, 15),
                                bg=self.red,
                                fg="white",
                                activebackground="white",
                                activeforeground=self.red)
        button_exit = tk.Button(self.pages[name],
                                text="Exit",
                                command=self.close_window_and_exit,
                                font=(self.font, 15),
                                bg=self.red,
                                fg="white",
                                activebackground="white",
                                activeforeground=self.red)
        space = tk.Label(self.pages[name],
                         text="Pattharamon Dumrongkittikule 6610545472",
                         font=(self.font, 20),
                         bg=self.blue,
                         fg="white")
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
                   sticky=tk.W,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=10,
                   ipady=5)

    def init_Results(self, page):
        button_home = tk.Button(page,
                                text="Results",
                                command=lambda:
                                self.show_page("story"),
                                font=(self.font, 15),
                                bg=self.red,
                                fg="white",
                                activebackground="white",
                                activeforeground=self.red)
        button_home.grid(column=5,
                         row=1,
                         sticky=tk.NSEW,
                         columnspan=1,
                         padx=0,
                         pady=20,
                         ipadx=70,
                         ipady=0)

    def init_home(self):
        title = tk.Label(self.pages["home"],
                         text="Dog Breeds",
                         font=(self.font, 90),
                         bg=self.blue,
                         fg="white")
        button_source = tk.Button(self.pages["home"],
                                  text="Source",
                                  command=lambda:
                                  webbrowser.open("https://www.kaggle.com"
                                                  "/datasets/mexwell/dog"
                                                  "-breeds-dogtime-dataset"),
                                  font=(self.font, 20),
                                  bg=self.bone,
                                  fg=self.brown,
                                  activebackground=self.red,
                                  activeforeground="white")
        button_dog_list = tk.Button(self.pages["home"],
                                    text="All dog breeds",
                                    command=lambda:
                                    self.show_page("dog_list"),
                                    font=(self.font, 20),
                                    bg=self.bone,
                                    fg=self.brown,
                                    activebackground=self.red,
                                    activeforeground="white")
        button_story = tk.Button(self.pages["home"],
                                 text="Data Storytelling Results",
                                 command=lambda:
                                 self.show_page("story"),
                                 font=(self.font, 20),
                                 bg=self.bone,
                                 fg=self.brown,
                                 activebackground=self.red,
                                 activeforeground="white")
        self.entry_story = tk.Entry(self.pages["home"],
                                    textvariable=self.name_var,
                                    font=(self.font, 20),
                                    bg="white",
                                    fg=self.red)
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
                           pady=10,
                           ipadx=50,
                           ipady=10)
        button_dog_list.grid(column=4,
                             row=2,
                             sticky=tk.NSEW,
                             columnspan=2,
                             padx=20,
                             pady=10,
                             ipadx=50,
                             ipady=10)
        button_story.grid(column=4,
                          row=3,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=20,
                          pady=10,
                          ipadx=50,
                          ipady=10)
        self.entry_story.grid(column=0,
                              row=4,
                              sticky=tk.NSEW,
                              columnspan=6,
                              padx=20,
                              pady=10,
                              ipadx=50,
                              ipady=10)
        self.entry_story.insert(0, "   Name of a dog breed here...")
        self.entry_story.bind("<FocusIn>",
                              lambda event: self.focus_in(self.entry_story))
        self.entry_story.bind("<FocusOut>",
                              lambda event: self.focus_out(
                                  self.entry_story,
                                  "   Name of a dog breed here..."))
        self.entry_story.bind("<Return>", self.show_dog_solo)

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
                         font=(self.font, 35),
                         bg=self.blue,
                         fg="white")
        des = tk.Label(self.pages["story"],
                       text="The topic: The relationship between "
                            "Intelligence, Adaptability, and Friendliness.",
                       font=(self.font, 20),
                       bg=self.blue,
                       fg="white")
        button_all_1 = ["The histogram of all levels of "
                        "Intelligence, Adaptability, and Friendliness",
                        "Intelligence vs Adaptability",
                        "Intelligence vs Friendliness",
                        "Adaptability vs Friendliness",
                        "Intelligence", "Adaptability", "Friendliness",
                        "Descriptive Statistics and Correlations",
                        "The story from the dataset"]
        button_all_2 = ["histogram", "IvsA", "IvsF", "AvsF",
                        "Intell", "Adapt", "Friend", "DSC", "final"]
        col = [0, 0, 2, 4, 0, 2, 4, 0, 0]
        row = [4, 5, 5, 5, 6, 6, 6, 7, 8]
        span = [6, 2, 2, 2, 2, 2, 2, 6, 6]
        for i in range(0, 9):
            button = tk.Button(self.pages["story"],
                               text=button_all_1[i],
                               command=lambda page=button_all_2[i]:
                               self.show_page(page),
                               font=(self.font, 20),
                               bg=self.bone,
                               fg=self.brown,
                               activebackground=self.red,
                               activeforeground="white")
            button.grid(column=col[i],
                        row=row[i],
                        sticky=tk.NSEW,
                        columnspan=span[i],
                        padx=20,
                        pady=10,
                        ipadx=5,
                        ipady=5)
        title.grid(column=0,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=30,
                   ipady=5)
        des.grid(column=0,
                 row=3,
                 sticky=tk.NSEW,
                 columnspan=6,
                 padx=20,
                 pady=5,
                 ipadx=30,
                 ipady=5)

    def init_histogram(self):
        sub_his_page = tk.Frame(self.pages["histogram"],
                                bg=self.blue)
        self.pages_2["sub_his_page"] = sub_his_page
        self.v1.set(True)
        self.v2.set(True)
        self.v3.set(True)
        self.his_change()
        check_1 = [self.v1, self.v2, self.v3]
        check_2 = ["Intelligence", "Adaptability", "Friendliness"]
        for i in range(0, 3):
            check = tk.Checkbutton(self.pages_2["sub_his_page"],
                                   text=check_2[i],
                                   variable=check_1[i],
                                   command=self.his_change,
                                   font=(self.font, 20),
                                   bg=self.blue,
                                   activebackground=self.blue,
                                   activeforeground=self.red)
            check.grid(column=i,
                       row=0,
                       columnspan=2,
                       padx=20,
                       pady=5,
                       ipadx=100,
                       ipady=10)
        sub_his_page.grid(column=0,
                          row=2,
                          columnspan=6)

    def init_IvsA(self):
        sub_IvsA_page = tk.Frame(self.pages["IvsA"],
                                 bg=self.blue)
        self.pages_2["sub_IvsA_page"] = sub_IvsA_page
        self.scat["IvsA"] = False
        self.scatter_change("Intelligence",
                            "Adaptability",
                            "IvsA",
                            self.scat["IvsA"])
        button_switch_IvsA = tk.Button(self.pages_2["sub_IvsA_page"],
                                       text="Switch X <-> Y",
                                       command=lambda:
                                       self.scatter_change("Intelligence",
                                                           "Adaptability",
                                                           "IvsA",
                                                           self.scat["IvsA"]),
                                       font=(self.font, 20),
                                       bg=self.bone,
                                       fg=self.brown,
                                       activebackground=self.red,
                                       activeforeground="white")
        sub_IvsA_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_IvsA.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=20,
                                pady=20,
                                ipadx=5,
                                ipady=5)

    def init_IvsF(self):
        sub_IvsF_page = tk.Frame(self.pages["IvsF"],
                                 bg=self.blue)
        self.pages_2["sub_IvsF_page"] = sub_IvsF_page
        self.scat["IvsF"] = False
        self.scatter_change("Intelligence",
                            "Friendliness",
                            "IvsF",
                            self.scat["IvsF"])
        button_switch_IvsF = tk.Button(self.pages_2["sub_IvsF_page"],
                                       text="Switch X <-> Y",
                                       command=lambda:
                                       self.scatter_change("Intelligence",
                                                           "Friendliness",
                                                           "IvsF",
                                                           self.scat["IvsF"]),
                                       font=(self.font, 20),
                                       bg=self.bone,
                                       fg=self.brown,
                                       activebackground=self.red,
                                       activeforeground="white")
        sub_IvsF_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_IvsF.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=20,
                                pady=20,
                                ipadx=5,
                                ipady=5)

    def init_AvsF(self):
        sub_AvsF_page = tk.Frame(self.pages["AvsF"],
                                 bg=self.blue)
        self.pages_2["sub_AvsF_page"] = sub_AvsF_page
        self.scat["AvsF"] = False
        self.scatter_change("Adaptability",
                            "Friendliness",
                            "AvsF",
                            self.scat["AvsF"])
        button_switch_AvsF = tk.Button(self.pages_2["sub_AvsF_page"],
                                       text="Switch X <-> Y",
                                       command=lambda:
                                       self.scatter_change("Adaptability",
                                                           "Friendliness",
                                                           "AvsF",
                                                           self.scat["AvsF"]),
                                       font=(self.font, 20),
                                       bg=self.bone,
                                       fg=self.brown,
                                       activebackground=self.red,
                                       activeforeground="white")
        sub_AvsF_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_AvsF.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=20,
                                pady=20,
                                ipadx=5,
                                ipady=5)

    def init_Intell(self):
        sub_Intell_page = tk.Frame(self.pages["Intell"],
                                   bg=self.blue)
        self.pages_2["sub_Intell_page"] = sub_Intell_page
        for i in self.list_Intell_var:
            i.set(False)
        self.list_Intell_var[0].set(True)
        self.bar_change("Intelligence",
                        "Intell",
                        "Level",
                        "Frequency_Intell",
                        [i for i in self.list_Intell_var])
        for i in range(0, 5):
            check = tk.Checkbutton(self.pages_2["sub_Intell_page"],
                                   text=f"Level {i + 1}",
                                   variable=self.list_Intell_var[i],
                                   command=lambda:
                                   self.bar_change(
                                       "Intelligence",
                                       "Intell",
                                       "Level",
                                       "Frequency_Intell",
                                       [i for i in self.list_Intell_var]),
                                   font=(self.font, 20),
                                   bg=self.blue,
                                   activebackground=self.blue,
                                   activeforeground=self.red)
            check.grid(column=i,
                       row=0,
                       columnspan=1,
                       padx=20,
                       pady=5,
                       ipadx=50,
                       ipady=10)
        sub_Intell_page.grid(column=0,
                             row=2,
                             columnspan=6)

    def init_Adapt(self):
        sub_Adapt_page = tk.Frame(self.pages["Adapt"],
                                  bg=self.blue)
        self.pages_2["sub_Adapt_page"] = sub_Adapt_page
        for i in self.list_Adapt_var:
            i.set(False)
        self.list_Intell_var[0].set(True)
        self.bar_change("Adaptability",
                        "Adapt",
                        "Level",
                        "Frequency_Adapt",
                        [j for j in self.list_Intell_var])
        for i in range(0, 5):
            check = tk.Checkbutton(self.pages_2["sub_Adapt_page"],
                                   text=f"Level {i + 1}",
                                   variable=self.list_Intell_var[i],
                                   command=lambda:
                                   self.bar_change(
                                       "Adaptability",
                                       "Adapt",
                                       "Level",
                                       "Frequency_Adapt",
                                       [j for j in self.list_Intell_var]),
                                   font=(self.font, 20),
                                   bg=self.blue,
                                   activebackground=self.blue,
                                   activeforeground=self.red)
            check.grid(column=i,
                       row=0,
                       columnspan=1,
                       padx=20,
                       pady=5,
                       ipadx=50,
                       ipady=10)
        sub_Adapt_page.grid(column=0,
                            row=2,
                            columnspan=6)

    def init_Friend(self):
        sub_Friend_page = tk.Frame(self.pages["Friend"],
                                   bg=self.blue)
        self.pages_2["sub_Friend_page"] = sub_Friend_page
        for i in self.list_Friend_var:
            i.set(False)
        self.list_Friend_var[0].set(True)
        self.bar_change("Friendliness",
                        "Friend",
                        "Level",
                        "Frequency_Friend",
                        [i for i in self.list_Friend_var])
        for i in range(0, 5):
            check = tk.Checkbutton(self.pages_2["sub_Friend_page"],
                                   text=f"Level {i + 1}",
                                   variable=self.list_Friend_var[i],
                                   command=lambda:
                                   self.bar_change(
                                       "Friendliness",
                                       "Friend",
                                       "Level",
                                       "Frequency_Friend",
                                       [j for j in self.list_Friend_var]),
                                   font=(self.font, 20),
                                   bg=self.blue,
                                   activebackground=self.blue,
                                   activeforeground=self.red)
            check.grid(column=i,
                       row=0,
                       columnspan=1,
                       padx=20,
                       pady=5,
                       ipadx=50,
                       ipady=10)
        sub_Friend_page.grid(column=0,
                             row=2,
                             columnspan=6)

    def init_DSC(self):
        # todo: grid, label are all separate
        description = self.d1.d.describe().transpose()
        filtered_des = description.loc[["Intelligence",
                                        "Adaptability",
                                        "Friendliness"]]
        text_des = str(filtered_des).split()
        text_head = [""] + [text_des[i] for i in range(0, 8)]
        text_Intell = [text_des[i] for i in range(8, 17)]
        text_Adapt = [text_des[i] for i in range(17, 26)]
        text_Friend = [text_des[i] for i in range(26, 35)]
        title = tk.Label(self.pages["DSC"],
                         text="Descriptive Statistics and Correlations",
                         font=(self.font, 35),
                         bg=self.blue,
                         fg="white")
        des_head = tk.Label(self.pages["DSC"],
                            text="".join(text_head),
                            font=(self.font, 20),
                            bg=self.blue,
                            fg="white")
        des_Intell = tk.Label(self.pages["DSC"],
                              text="".join(text_Intell),
                              font=(self.font, 20),
                              bg=self.blue,
                              fg="white")
        des_Adapt = tk.Label(self.pages["DSC"],
                             text="".join(text_Adapt),
                             font=(self.font, 20),
                             bg=self.blue,
                             fg="white")
        des_Friend = tk.Label(self.pages["DSC"],
                              text="".join(text_Friend),
                              font=(self.font, 20),
                              bg=self.blue,
                              fg="white")
        title.grid(column=0,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=30,
                   ipady=5)
        des_head.grid(column=0,
                      row=3,
                      sticky=tk.NSEW,
                      columnspan=6,
                      padx=20,
                      pady=5,
                      ipadx=30,
                      ipady=5)
        des_Intell.grid(column=0,
                        row=4,
                        sticky=tk.NSEW,
                        columnspan=6,
                        padx=20,
                        pady=5,
                        ipadx=30,
                        ipady=5)
        des_Adapt.grid(column=0,
                       row=5,
                       sticky=tk.NSEW,
                       columnspan=6,
                       padx=20,
                       pady=5,
                       ipadx=30,
                       ipady=5)
        des_Friend.grid(column=0,
                        row=6,
                        sticky=tk.NSEW,
                        columnspan=6,
                        padx=20,
                        pady=5,
                        ipadx=30,
                        ipady=5)

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
                page = tk.Frame(self, bg=self.blue)
                self.pages[name] = page
                self.init_dog_solo(name, name_list.index(name))
                self.show_page(name)
            else:
                self.show_page(name)

    @staticmethod
    def focus_in(entry):
        entry.delete(0, tk.END)

    @staticmethod
    def focus_out(entry, word):
        entry.delete(0, tk.END)
        entry.insert(0, word)

    def histogram(self, page, column, row, span, df, x, name, x_name, y_name):
        fig, ax = plt.subplots()
        sns.histplot(data=df,
                     x=x,
                     binwidth=1,
                     kde=True,
                     ax=ax)
        ax.set_xlabel(x_name,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel(y_name,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(name,
                     fontsize=15,
                     fontfamily=self.font_fam)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)
        plt.close(fig)

    def his_change(self):
        if "his_page" in self.pages_2:
            self.pages_2["his_page"].grid_forget()
        his_page = tk.Frame(self.pages["histogram"],
                            bg=self.blue)
        self.pages_2["his_page"] = his_page
        self.pages_2["his_page"].grid(column=0,
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
            all_list += self.d1.get_list("Friendliness")
            name_list.append("Friendliness")
        df = pd.DataFrame({"histogram_list": all_list})
        name = ", ".join(name_list)
        self.histogram(self.pages_2["his_page"],
                       0,
                       0,
                       6,
                       df,
                       "histogram_list",
                       "The histogram of all levels of\n"
                       f"{name}",
                       "Level",
                       "Frequency of level")
        self.init_Results(self.pages_2["his_page"])

    def scatter(self, page, column, row, span, df, x, y):
        fig, ax = plt.subplots()
        sns.regplot(data=df,
                    x=x,
                    y=y,
                    color=self.red,
                    line_kws={"color": self.blue},
                    ax=ax)
        ax.set_xlabel(f"Levels of {x}",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel(f"Levels of {y}",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"{x} vs {y}",
                     fontsize=15,
                     fontfamily=self.font_fam)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)
        plt.close(fig)

    def scatter_change(self, x, y, name, var):
        if var:
            temp = x
            x = y
            y = temp
            self.scat[name] = False
        else:
            self.scat[name] = True
        if f"{name}_page" in self.pages_2:
            self.pages_2[f"{name}_page"].grid_forget()
        new_page = tk.Frame(self.pages[name],
                            bg=self.blue)
        self.pages_2[f"{name}_page"] = new_page
        self.pages_2[f"{name}_page"].grid(column=0,
                                          row=3,
                                          columnspan=6)
        df = pd.DataFrame({x: self.d1.get_list(x),
                           y: self.d1.get_list(y)})
        self.scatter(self.pages_2[f"{name}_page"],
                     0,
                     0,
                     6,
                     df,
                     x,
                     y)
        self.init_Results(self.pages_2[f"{name}_page"])

    def bar(self, name, page, column, row, span, df, x, y):
        fig, ax = plt.subplots()
        sns.barplot(data=df,
                    x=x,
                    y=y,
                    color=self.red,
                    ax=ax)
        ax.set_xlabel(x,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel(y,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"The bar graph of levels of {name}",
                     fontsize=15,
                     fontfamily=self.font_fam)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)
        plt.close(fig)

    def bar_change(self, ori_name, name, x, y, var_list):
        # todo: grid of all
        if f"{name}_page" in self.pages_2:
            self.pages_2[f"{name}_page"].grid_forget()
        new_page = tk.Frame(self.pages[name],
                            bg=self.blue)
        self.pages_2[f"{name}_page"] = new_page
        self.pages_2[f"{name}_page"].grid(column=0,
                                          row=3,
                                          columnspan=6)
        if (not var_list[0].get() and not var_list[1].get()
                and not var_list[2].get() and not var_list[3].get()
                and not var_list[4].get()):
            messagebox.showwarning(f"Can't uncheck all",
                                   f"You can't uncheck all five.")
            for i in var_list:
                i.set(False)
            var_list[0].set(True)
        all_list = self.d2.get_list(y)
        level_list = [str(i) for i in self.d2.get_list(x)]
        spe = 0
        name_list = []
        num = 0
        num_name = 0
        for i in var_list:
            if i.get():
                spe += self.d2.get_list(y)[num_name]
                all_list.pop(num)
                level_list.pop(num)
                name_list.append(f"{num_name + 1}")
            else:
                num += 1
            num_name += 1
        y_df = [spe] + all_list
        x_df = [", ".join(name_list)] + level_list
        df = pd.DataFrame({x: x_df,
                           y: y_df})
        self.bar(ori_name,
                 self.pages_2[f"{name}_page"],
                 0,
                 0,
                 6,
                 df,
                 x,
                 y)
        self.init_Results(self.pages_2[f"{name}_page"])

    def close_window_and_exit(self):
        self.destroy()
        self.quit()
