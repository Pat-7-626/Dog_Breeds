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
        self.IAF_v1 = tk.BooleanVar()
        self.IAF_v2 = tk.BooleanVar()
        self.IAF_v3 = tk.BooleanVar()
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
                  "IAF", "final"]:
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
        self.init_IAF()
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
                         padx=10,
                         pady=10,
                         ipadx=100,
                         ipady=0)
        button_exit.grid(column=3,
                         row=0,
                         sticky=tk.NSEW,
                         columnspan=3,
                         padx=10,
                         pady=10,
                         ipadx=100,
                         ipady=0)
        space.grid(column=0,
                   row=1,
                   sticky=tk.W,
                   columnspan=6,
                   padx=10,
                   pady=10,
                   ipadx=10,
                   ipady=5)

    def init_Results(self, page, row):
        button_Results = tk.Button(page,
                                   text="Data Storytelling Results",
                                   command=lambda:
                                   self.show_page("story"),
                                   font=(self.font, 15),
                                   bg=self.red,
                                   fg="white",
                                   activebackground="white",
                                   activeforeground=self.red)
        button_Results.grid(column=5,
                            row=row,
                            sticky=tk.E,
                            padx=10,
                            pady=20,
                            ipadx=10,
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
                           padx=10,
                           pady=10,
                           ipadx=10,
                           ipady=10)
        button_dog_list.grid(column=4,
                             row=2,
                             sticky=tk.NSEW,
                             columnspan=2,
                             padx=10,
                             pady=10,
                             ipadx=10,
                             ipady=10)
        button_story.grid(column=4,
                          row=3,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=10,
                          pady=10,
                          ipadx=10,
                          ipady=10)
        self.entry_story.grid(column=0,
                              row=4,
                              sticky=tk.NSEW,
                              columnspan=6,
                              padx=10,
                              pady=10,
                              ipadx=10,
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
        button_all_1 = ["Intelligence vs Adaptability",
                        "Intelligence vs Friendliness",
                        "Adaptability vs Friendliness",
                        "The bar graph of all levels of "
                        "Intelligence, Adaptability, and Friendliness",
                        "The histogram of all levels of "
                        "Intelligence, Adaptability, and Friendliness",
                        "Descriptive Statistics and Correlations",
                        "The story from the dataset"]
        button_all_2 = ["IvsA", "IvsF", "AvsF", "IAF",
                        "histogram", "DSC", "final"]
        col = [0, 2, 4, 0, 0, 0, 0]
        row = [4, 4, 4, 5, 6, 7, 8]
        span = [2, 2, 2, 6, 6, 6, 6]
        for i in range(0, 7):
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
                        padx=10,
                        pady=10,
                        ipadx=10,
                        ipady=10)
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
                       padx=80,
                       pady=10,
                       ipadx=5,
                       ipady=5)
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
                                       text="Switching between "
                                            "Intelligence and Adaptability",
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
                                padx=10,
                                pady=20,
                                ipadx=100,
                                ipady=0)

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
                                       text="Switching between "
                                            "Intelligence and Friendliness",
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
                                padx=10,
                                pady=20,
                                ipadx=100,
                                ipady=0)

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
                                       text="Switching between "
                                            "Adaptability and Friendliness",
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
                                padx=10,
                                pady=20,
                                ipadx=100,
                                ipady=0)

    def init_IAF(self):
        sub_IAF_page = tk.Frame(self.pages["IAF"],
                                bg=self.blue)
        self.pages_2["sub_IAF_page"] = sub_IAF_page
        self.IAF_v1.set(True)
        self.IAF_v2.set(True)
        self.IAF_v3.set(True)
        self.bar_change()
        check_1 = [self.IAF_v1, self.IAF_v2, self.IAF_v3]
        check_2 = ["Intelligence", "Adaptability", "Friendliness"]
        for i in range(0, 3):
            check = tk.Checkbutton(self.pages_2["sub_IAF_page"],
                                   text=check_2[i],
                                   variable=check_1[i],
                                   command=self.bar_change,
                                   font=(self.font, 20),
                                   bg=self.blue,
                                   activebackground=self.blue,
                                   activeforeground=self.red)
            check.grid(column=i,
                       row=0,
                       padx=80,
                       pady=10,
                       ipadx=5,
                       ipady=5)
        sub_IAF_page.grid(column=0,
                          row=2,
                          columnspan=6)

    def init_DSC(self):
        # todo: grid, label are all separate
        self.show_page_2("DSC_page", "DSC")
        description = self.d1.d.describe().transpose()
        filtered_des = description.loc[["Intelligence",
                                        "Adaptability",
                                        "Friendliness"]]
        text_des = str(filtered_des).split()
        text_head = [""] + [text_des[i] for i in range(0, 8)]
        text_Intell = [text_des[i] for i in range(8, 17)]
        text_Adapt = [text_des[i] for i in range(17, 26)]
        text_Friend = [text_des[i] for i in range(26, 35)]
        text_all = text_head + text_Intell + text_Adapt + text_Friend
        title = tk.Label(self.pages["DSC"],
                         text="Descriptive\nStatistics\nand Correlations",
                         font=(self.font, 35),
                         bg=self.blue,
                         fg="white")
        count = 0
        for i in range(0, 4):
            for j in range(0, 9):
                bg_color = self.red
                fg_color = "white"
                if text_all[count] in ["count", "mean", "std", "min", "25%",
                                       "50%", "75%", "max", "Intelligence",
                                       "Adaptability", "Friendliness"]:
                    bg_color = "white"
                    fg_color = self.red
                elif text_all[count] == "":
                    bg_color = self.blue
                des = tk.Label(self.pages_2["DSC_page"],
                               text=text_all[count],
                               font=(self.font, 15),
                               bg=bg_color,
                               fg=fg_color)
                des.grid(column=j,
                         row=i,
                         sticky=tk.NSEW,
                         padx=5,
                         pady=5,
                         ipadx=5,
                         ipady=5)
                count += 1
        title.grid(column=0,
                   row=2,
                   sticky=tk.E,
                   padx=20,
                   pady=5,
                   ipadx=30,
                   ipady=10)

    def show_page(self, name):
        for page in self.pages.values():
            page.grid_forget()
        self.pages[name].grid(row=0,
                              column=0)
        self.init_menu(name)
        self.pages["home"].focus_set()

    def show_page_2(self, name, name_parent):
        if name in self.pages_2:
            self.pages_2[name].grid_forget()
        his_page = tk.Frame(self.pages[name_parent],
                            bg=self.blue)
        self.pages_2[name] = his_page
        self.pages_2[name].grid(column=0,
                                row=3,
                                columnspan=6)

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

    def histogram(self, name, page, column, row, span, df, x, x_name, y_name):
        fig, ax = plt.subplots()
        sns.histplot(data=df,
                     x=x,
                     binwidth=1,
                     kde=True,
                     color=self.red,
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
        ax.grid(True)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)
        plt.close(fig)

    def his_change(self):
        self.show_page_2("his_page", "histogram")
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
        self.histogram("The histogram of all levels of\n"
                       f"{name}",
                       self.pages_2["his_page"],
                       0,
                       0,
                       6,
                       df,
                       "histogram_list",
                       "Level",
                       "Frequency of level")
        self.init_Results(self.pages["histogram"], 4)

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
        ax.grid(True)
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
        self.show_page_2(f"{name}_page", name)
        df = pd.DataFrame({x: self.d1.get_list(x),
                           y: self.d1.get_list(y)})
        self.scatter(self.pages_2[f"{name}_page"],
                     0,
                     0,
                     6,
                     df,
                     x,
                     y)
        self.init_Results(self.pages[name], 4)

    def bar(self, name, page, column, row, span, df, color):
        melted_df = df.melt(id_vars="Level",
                            var_name="each_topic",
                            value_name="val")
        fig, ax = plt.subplots()
        sns.barplot(data=melted_df,
                    x="Level",
                    y="val",
                    hue="each_topic",
                    palette=color,
                    ax=ax)
        ax.set_xlabel("Level",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel("Frequency of Level",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"The bar graph of levels of \n"
                     f"{name}",
                     fontsize=15,
                     fontfamily=self.font_fam)
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span)
        plt.close(fig)

    def bar_change(self):
        self.show_page_2("IAF_page", "IAF")
        name_dict = {}
        all_dict = {}
        color = []
        if (not self.IAF_v1.get()
                and not self.IAF_v2.get()
                and not self.IAF_v3.get()):
            messagebox.showwarning(f"Can't uncheck all",
                                   f"You can't uncheck all three.")
            self.IAF_v1.set(True)
            self.IAF_v2.set(True)
            self.IAF_v3.set(True)
        if self.IAF_v1.get():
            name_dict["Intelligence"] = "Frequency_Intell"
            color.append(self.red)
        if self.IAF_v2.get():
            name_dict["Adaptability"] = "Frequency_Adapt"
            color.append(self.blue)
        if self.IAF_v3.get():
            name_dict["Friendliness"] = "Frequency_Friend"
            color.append(self.bone)
        all_dict["Level"] = self.d2.get_list("Level")
        for i, j in name_dict.items():
            all_dict.update({i: self.d2.get_list(j)})
        df = pd.DataFrame(all_dict)
        name = ", ".join([i for i, j in name_dict.items()])
        self.bar(name,
                 self.pages_2["IAF_page"],
                 0,
                 0,
                 6,
                 df,
                 color)
        self.init_Results(self.pages["IAF"], 4)

    def close_window_and_exit(self):
        self.destroy()
        self.quit()
