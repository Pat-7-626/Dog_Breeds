import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.stats as stats
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import webbrowser


class DogUI(tk.Tk):
    background = "#98c1d9"
    light = "#e0fbfc"
    pitch = "#293241"
    dark = "#3d5a80"
    main = "#ee6c4d"
    font = "Terminal"
    font_fam = "monospace"

    def __init__(self, d1, d2, t, ma_t, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d1 = d1
        self.d2 = d2
        self.t1 = t[0]
        self.t2 = t[1]
        self.t3 = t[2]
        self.m_t1 = ma_t[0]
        self.m_t2 = ma_t[1]
        self.m_t3 = ma_t[2]
        self.pages = {}
        self.pages_2 = {}
        self.scat = {}
        self.name_var = tk.StringVar()
        self.skew = tk.StringVar()
        self.v1 = tk.BooleanVar()
        self.v2 = tk.BooleanVar()
        self.v3 = tk.BooleanVar()
        self.IPA_v1 = tk.BooleanVar()
        self.IPA_v2 = tk.BooleanVar()
        self.IPA_v3 = tk.BooleanVar()
        self.entry_story = None
        self.text = None
        self.melted_df = None
        self.title("Dog Breeds")
        self.configure(bg=self.background,
                       borderwidth=35,
                       cursor="hand2")
        self.init_page()
        self.show_page("home")
        self.focus_force()
        self.protocol("WM_DELETE_WINDOW", self.close_window_and_exit)

    def init_page(self):
        for i in ["home", "story", "DSC", "histogram", "IvsP", "IvsA",
                  "PvsA", "IPA", "final"]:
            page = tk.Frame(self,
                            bg=self.background)
            self.pages[i] = page
        self.init_home()
        self.init_story()
        self.init_histogram()
        self.init_IvsP()
        self.init_IvsA()
        self.init_PvsA()
        self.init_IPA()
        self.init_DSC()
        self.init_final()
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
                                bg=self.main,
                                fg=self.light,
                                activebackground=self.light,
                                activeforeground=self.main)
        button_exit = tk.Button(self.pages[name],
                                text="Exit",
                                command=self.close_window_and_exit,
                                font=(self.font, 15),
                                bg=self.main,
                                fg=self.light,
                                activebackground=self.light,
                                activeforeground=self.main)
        space = tk.Label(self.pages[name],
                         text="Pattharamon Dumrongkittikule 6610545472",
                         font=(self.font, 20),
                         bg=self.background,
                         fg=self.pitch)
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
                                   bg=self.main,
                                   fg=self.light,
                                   activebackground=self.light,
                                   activeforeground=self.main)
        button_Results.grid(column=5,
                            row=row,
                            sticky=tk.E,
                            padx=15,
                            pady=15,
                            ipadx=10,
                            ipady=0)

    def init_home(self):
        title = tk.Label(self.pages["home"],
                         text="Dog Breeds",
                         font=(self.font, 130),
                         bg=self.background,
                         fg=self.main)
        button_source = tk.Button(self.pages["home"],
                                  text="Source",
                                  command=lambda:
                                  webbrowser.open("https://www.kaggle.com"
                                                  "/datasets/mexwell/dog"
                                                  "-breeds-dogtime-dataset"),
                                  font=(self.font, 15),
                                  bg=self.dark,
                                  fg=self.light,
                                  activebackground=self.main,
                                  activeforeground=self.light)
        button_dog_web = tk.Button(self.pages["home"],
                                   text="All dog breeds",
                                   command=lambda:
                                   webbrowser.open("https://dogtime.com/"),
                                   font=(self.font, 15),
                                   bg=self.dark,
                                   fg=self.light,
                                   activebackground=self.main,
                                   activeforeground=self.light)
        button_story = tk.Button(self.pages["home"],
                                 text="Data Storytelling Results",
                                 command=lambda:
                                 self.show_page("story"),
                                 font=(self.font, 15),
                                 bg=self.dark,
                                 fg=self.light,
                                 activebackground=self.main,
                                 activeforeground=self.light)
        self.entry_story = tk.Entry(self.pages["home"],
                                    textvariable=self.name_var,
                                    font=(self.font, 20),
                                    bg=self.light,
                                    fg=self.main)
        title.grid(column=0,
                   row=2,
                   sticky=tk.E,
                   columnspan=3,
                   rowspan=4,
                   padx=10,
                   pady=10,
                   ipadx=50,
                   ipady=10)
        button_source.grid(column=3,
                           row=3,
                           sticky="NSE",
                           padx=10,
                           pady=10,
                           ipadx=30,
                           ipady=10)
        button_dog_web.grid(column=4,
                            row=3,
                            sticky=tk.NSEW,
                            columnspan=2,
                            padx=10,
                            pady=10,
                            ipadx=10,
                            ipady=10)
        button_story.grid(column=4,
                          row=4,
                          sticky=tk.NSEW,
                          columnspan=2,
                          padx=10,
                          pady=10,
                          ipadx=10,
                          ipady=10)
        self.entry_story.grid(column=0,
                              row=6,
                              sticky=tk.NSEW,
                              columnspan=6,
                              padx=10,
                              pady=0,
                              ipadx=500,
                              ipady=10)
        self.entry_story.insert(0, "   Name of a dog breed here...")
        self.entry_story.bind("<FocusIn>",
                              lambda event: self.focus_in(self.entry_story))
        self.entry_story.bind("<FocusOut>",
                              lambda event: self.focus_out(
                                  self.entry_story,
                                  "   Name of a dog breed here..."))
        self.entry_story.bind("<Return>", self.show_dog_solo)

    def init_story(self):
        title = tk.Label(self.pages["story"],
                         text="Data Storytelling Results",
                         font=(self.font, 50),
                         bg=self.background,
                         fg=self.main)
        des = tk.Label(self.pages["story"],
                       text=f"The topic: The relationship between\n\n"
                            f"{self.t1}, {self.t2}, and {self.t3}.",
                       font=(self.font, 20),
                       bg=self.background,
                       fg=self.pitch)

        button_all_1 = [f"{self.t1}\nvs\n{self.t2}",
                        f"{self.t1}\nvs\n{self.t3}",
                        f"{self.t2}\nvs\n{self.t3}",
                        "The bar graph of all levels of "
                        f"{self.t1}, {self.t2}, and {self.t3}",
                        "The histogram of all levels of "
                        f"{self.t1}, {self.t2}, and {self.t3}",
                        "Descriptive Statistics and Correlations",
                        "The story from the dataset"]
        button_all_2 = ["IvsP", "IvsA", "PvsA", "IPA",
                        "histogram", "DSC", "final"]
        col = [0, 2, 4, 0, 0, 0, 0]
        row = [4, 4, 4, 5, 6, 7, 8]
        span = [2, 2, 2, 6, 6, 6, 6]
        for i in range(0, 7):
            button = tk.Button(self.pages["story"],
                               text=button_all_1[i],
                               command=lambda page=button_all_2[i]:
                               self.show_page(page),
                               font=(self.font, 15),
                               bg=self.dark,
                               fg=self.light,
                               activebackground=self.main,
                               activeforeground=self.light)
            button.grid(column=col[i],
                        row=row[i],
                        sticky=tk.NSEW,
                        columnspan=span[i],
                        padx=10,
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
                                bg=self.background)
        self.pages_2["sub_his_page"] = sub_his_page
        self.v1.set(True)
        self.v2.set(True)
        self.v3.set(True)
        self.text = tk.Label(self.pages["histogram"],
                             textvariable=self.skew,
                             font=(self.font, 20),
                             bg=self.background,
                             fg=self.dark)
        self.his_change()
        check_1 = [self.v1, self.v2, self.v3]
        check_2 = ["Trainability,\n"
                   f"The major topic of\n{self.t1}",
                   "Exercise Needs,\n"
                   f"The major topic of\n{self.t2}",
                   "Adaptability,\n"
                   f"The major topic of\n{self.t3}"]
        for i in range(0, 3):
            check = tk.Checkbutton(self.pages_2["sub_his_page"],
                                   text=check_2[i],
                                   variable=check_1[i],
                                   command=self.his_change,
                                   font=(self.font, 20),
                                   bg=self.background,
                                   activebackground=self.background,
                                   activeforeground=self.main)
            check.grid(column=i,
                       row=0,
                       sticky=tk.NSEW,
                       padx=5,
                       pady=5,
                       ipadx=5,
                       ipady=0)
        sub_his_page.grid(column=0,
                          row=2,
                          columnspan=6)
        self.text.grid(column=0,
                       row=4,
                       padx=5,
                       pady=5,
                       ipadx=0,
                       ipady=0)
        self.init_Results(self.pages["histogram"], 5)

    def init_IvsP(self):
        sub_IvsP_page = tk.Frame(self.pages["IvsP"],
                                 bg=self.background)
        self.pages_2["sub_IvsP_page"] = sub_IvsP_page
        self.scat["IvsP"] = False
        self.scatter_change(f"{self.t1}",
                            f"{self.t2}",
                            "IvsP",
                            self.scat["IvsP"])
        button_switch_IvsP = tk.Button(self.pages_2["sub_IvsP_page"],
                                       text="Switching between "
                                            f"{self.t1} and {self.t2}",
                                       command=lambda:
                                       self.scatter_change(f"{self.t1}",
                                                           f"{self.t2}",
                                                           "IvsP",
                                                           self.scat["IvsP"]),
                                       font=(self.font, 15),
                                       bg=self.dark,
                                       fg=self.light,
                                       activebackground=self.main,
                                       activeforeground=self.light)
        cor = self.d1.d[[f"{self.t1}", f"{self.t2}"]].corr().iloc[0, 1]
        text_1 = tk.Label(self.pages["IvsP"],
                          text=f"Correlation Coefficient: {cor: .4f}\n"
                               f"Relationship: {self.find_cor(cor)}",
                          font=(self.font, 20),
                          bg=self.background,
                          fg=self.dark,
                          justify=tk.LEFT)
        sub_IvsP_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_IvsP.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=5,
                                pady=5,
                                ipadx=100,
                                ipady=5)
        text_1.grid(column=0,
                    row=4,
                    sticky=tk.W,
                    columnspan=6,
                    padx=5,
                    pady=0,
                    ipadx=5,
                    ipady=0)
        self.init_Results(self.pages["IvsP"], 5)

    def init_IvsA(self):
        sub_IvsA_page = tk.Frame(self.pages["IvsA"],
                                 bg=self.background)
        self.pages_2["sub_IvsA_page"] = sub_IvsA_page
        self.scat["IvsA"] = False
        self.scatter_change(f"{self.t1}",
                            f"{self.t3}",
                            "IvsA",
                            self.scat["IvsA"])
        button_switch_IvsA = tk.Button(self.pages_2["sub_IvsA_page"],
                                       text="Switching between "
                                            f"{self.t1} and {self.t3}",
                                       command=lambda:
                                       self.scatter_change(f"{self.t1}",
                                                           f"{self.t3}",
                                                           "IvsA",
                                                           self.scat["IvsA"]),
                                       font=(self.font, 15),
                                       bg=self.dark,
                                       fg=self.light,
                                       activebackground=self.main,
                                       activeforeground=self.light)
        cor = self.d1.d[[f"{self.t1}", f"{self.t3}"]].corr().iloc[0, 1]
        text_1 = tk.Label(self.pages["IvsA"],
                          text=f"Correlation Coefficient: {cor: .4f}\n"
                               f"Relationship: {self.find_cor(cor)}",
                          font=(self.font, 20),
                          bg=self.background,
                          fg=self.dark,
                          justify=tk.LEFT)
        sub_IvsA_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_IvsA.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=5,
                                pady=5,
                                ipadx=100,
                                ipady=5)
        text_1.grid(column=0,
                    row=4,
                    sticky=tk.W,
                    columnspan=6,
                    padx=5,
                    pady=0,
                    ipadx=5,
                    ipady=0)
        self.init_Results(self.pages["IvsA"], 5)

    def init_PvsA(self):
        sub_PvsA_page = tk.Frame(self.pages["PvsA"],
                                 bg=self.background)
        self.pages_2["sub_PvsA_page"] = sub_PvsA_page
        self.scat["PvsA"] = False
        self.scatter_change(f"{self.t2}",
                            f"{self.t3}",
                            "PvsA",
                            self.scat["PvsA"])
        button_switch_PvsA = tk.Button(self.pages_2["sub_PvsA_page"],
                                       text="Switching between "
                                            f"{self.t2} and {self.t3}",
                                       command=lambda:
                                       self.scatter_change(f"{self.t2}",
                                                           f"{self.t3}",
                                                           "PvsA",
                                                           self.scat["PvsA"]),
                                       font=(self.font, 15),
                                       bg=self.dark,
                                       fg=self.light,
                                       activebackground=self.main,
                                       activeforeground=self.light)
        cor = self.d1.d[[f"{self.t2}", f"{self.t3}"]].corr().iloc[0, 1]
        text_1 = tk.Label(self.pages["PvsA"],
                          text=f"Correlation Coefficient: {cor: .4f}\n"
                               f"Relationship: {self.find_cor(cor)}",
                          font=(self.font, 20),
                          bg=self.background,
                          fg=self.dark,
                          justify=tk.LEFT)
        sub_PvsA_page.grid(column=0,
                           row=2,
                           columnspan=6)
        button_switch_PvsA.grid(column=0,
                                row=0,
                                columnspan=6,
                                padx=5,
                                pady=5,
                                ipadx=100,
                                ipady=5)
        text_1.grid(column=0,
                    row=4,
                    sticky=tk.W,
                    columnspan=6,
                    padx=5,
                    pady=0,
                    ipadx=5,
                    ipady=0)
        self.init_Results(self.pages["PvsA"], 5)

    def init_IPA(self):
        sub_IPA_page = tk.Frame(self.pages["IPA"],
                                bg=self.background)
        self.pages_2["sub_IPA_page"] = sub_IPA_page
        self.IPA_v1.set(True)
        self.IPA_v2.set(True)
        self.IPA_v3.set(True)
        self.bar_change()
        check_1 = [self.IPA_v1, self.IPA_v2, self.IPA_v3]
        check_2 = [f"{self.t1}", f"{self.t2}", f"{self.t3}"]
        for i in range(0, 3):
            check = tk.Checkbutton(self.pages_2["sub_IPA_page"],
                                   text=check_2[i],
                                   variable=check_1[i],
                                   command=self.bar_change,
                                   font=(self.font, 20),
                                   bg=self.background,
                                   activebackground=self.background,
                                   activeforeground=self.main)
            check.grid(column=i,
                       row=0,
                       padx=30,
                       pady=10,
                       ipadx=5,
                       ipady=5)
        sub_IPA_page.grid(column=0,
                          row=2,
                          columnspan=6)
        self.init_Results(self.pages["IPA"], 4)

    def init_DSC(self):
        title_1 = tk.Label(self.pages["DSC"],
                           text="Descriptive Statistics",
                           font=(self.font, 25),
                           bg=self.background,
                           fg=self.main)
        title_2 = tk.Label(self.pages["DSC"],
                           text="Correlations",
                           font=(self.font, 25),
                           bg=self.background,
                           fg=self.main)
        sub_1 = tk.Frame(self.pages["DSC"],
                         bg=self.background)
        sub_2 = tk.Frame(self.pages["DSC"],
                         bg=self.background)
        description = self.d1.d.describe().transpose()
        filtered_des = description.loc[[f"{self.t1}",
                                        f"{self.t2}",
                                        f"{self.t3}"]].values.tolist()
        text_all_des = (["", "Count", "Mean", "STD", "Min",
                         "25%", "50%", "75%", "Max"]
                        + [f"{self.t1}"] + filtered_des[0]
                        + [f"{self.t2}"] + filtered_des[1]
                        + [f"{self.t3}"] + filtered_des[2])
        for i in text_all_des:
            try:
                float_i = float(i)
                index = text_all_des.index(i)
                if float_i.is_integer():
                    text_all_des[index] = f"{float_i:.0f}"
                else:
                    text_all_des[index] = f"{float_i:.4f}"
            except ValueError:
                continue
        count = 0
        for i in range(0, 4):
            for j in range(0, 9):
                bg_color = self.main
                fg_color = self.light
                if text_all_des[count] in ["Count", "Mean", "STD", "Min",
                                           "25%", "50%", "75%", "Max",
                                           f"{self.t1}",
                                           f"{self.t2}",
                                           f"{self.t3}"]:
                    bg_color = self.dark
                    fg_color = self.light
                elif text_all_des[count] == "":
                    bg_color = self.background
                des = tk.Label(sub_1,
                               text=text_all_des[count],
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
        filtered_cor = (self.d1.d[[f"{self.t1}", f"{self.t2}", f"{self.t3}"]]
                        .corr().values.tolist())
        filtered_cor = [[f"{val:.4f}" for val in row] for row in
                        filtered_cor]
        text_all_cor = ([""] + [f"{self.t1}", f"{self.t2}", f"{self.t3}"]
                        + [f"{self.t1}"] + filtered_cor[0]
                        + [f"{self.t2}"] + filtered_cor[1]
                        + [f"{self.t3}"] + filtered_cor[2])
        for i in text_all_cor:
            try:
                float_i = float(i)
                index = text_all_cor.index(i)
                if float_i.is_integer():
                    text_all_cor[index] = f"{float_i:.0f}"
                else:
                    text_all_cor[index] = f"{float_i:.4f}"
            except ValueError:
                continue
        count = 0
        for i in range(0, 4):
            for j in range(0, 4):
                bg_color = self.main
                fg_color = self.light
                if text_all_cor[count] in [f"{self.t1}",
                                           f"{self.t2}",
                                           f"{self.t3}"]:
                    bg_color = self.dark
                    fg_color = self.light
                elif text_all_cor[count] == "":
                    bg_color = self.background
                cor = tk.Label(sub_2,
                               text=text_all_cor[count],
                               font=(self.font, 15),
                               bg=bg_color,
                               fg=fg_color)
                cor.grid(column=j,
                         row=i,
                         sticky=tk.NSEW,
                         padx=5,
                         pady=5,
                         ipadx=5,
                         ipady=5)
                count += 1
        title_1.grid(column=0,
                     row=2,
                     sticky=tk.NSEW,
                     columnspan=2,
                     padx=20,
                     pady=5,
                     ipadx=30,
                     ipady=10)
        title_2.grid(column=0,
                     row=3,
                     sticky=tk.NSEW,
                     padx=20,
                     pady=5,
                     ipadx=30,
                     ipady=10)
        sub_1.grid(column=2,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=4,
                   padx=15,
                   pady=15,
                   ipadx=10,
                   ipady=0)
        sub_2.grid(column=1,
                   row=3,
                   sticky=tk.NSEW,
                   columnspan=5,
                   padx=15,
                   pady=15,
                   ipadx=10,
                   ipady=0)
        self.init_Results(self.pages["DSC"], 4)

    def init_final(self):
        I_P = f"{self.result_cor(self.t1, self.t2)}"
        I_A = f"{self.result_cor(self.t1, self.t3)}"
        P_A = f"{self.result_cor(self.t2, self.t3)}"
        title = tk.Label(self.pages["final"],
                         text="The story from the dataset",
                         font=(self.font, 50),
                         bg=self.background,
                         fg=self.main)
        sub_final = tk.Frame(self.pages["final"],
                             bg=self.dark)
        title_1 = tk.Label(sub_final,
                           text=f"\n{self.t1} And {self.t2}",
                           font=(self.font, 25),
                           bg=self.dark,
                           fg=self.light)
        text_1 = tk.Label(sub_final,
                          text=f"{I_P}\n",
                          font=(self.font, 20),
                          bg=self.dark,
                          fg=self.light,
                          wraplength=1250,
                          justify=tk.LEFT)
        title_2 = tk.Label(sub_final,
                           text=f"{self.t1} And {self.t3}",
                           font=(self.font, 25),
                           bg=self.dark,
                           fg=self.light)
        text_2 = tk.Label(sub_final,
                          text=f"{I_A}\n",
                          font=(self.font, 20),
                          bg=self.dark,
                          fg=self.light,
                          wraplength=1250,
                          justify=tk.LEFT)
        title_3 = tk.Label(sub_final,
                           text=f"{self.t2} And {self.t3}",
                           font=(self.font, 25),
                           bg=self.dark,
                           fg=self.light)
        text_3 = tk.Label(sub_final,
                          text=f"{P_A}\n",
                          font=(self.font, 20),
                          bg=self.dark,
                          fg=self.light,
                          wraplength=1250,
                          justify=tk.LEFT)
        title.grid(column=0,
                   row=2,
                   sticky=tk.NSEW,
                   columnspan=6,
                   padx=20,
                   pady=5,
                   ipadx=30,
                   ipady=5)
        sub_final.grid(column=0,
                       row=3,
                       sticky=tk.NSEW,
                       columnspan=6,
                       padx=10,
                       pady=10,
                       ipadx=10,
                       ipady=10)
        title_1.grid(column=0,
                     row=0,
                     padx=5,
                     pady=5,
                     ipadx=5,
                     ipady=5)
        text_1.grid(column=0,
                    row=1,
                    sticky=tk.W,
                    padx=5,
                    pady=0,
                    ipadx=20,
                    ipady=0)
        title_2.grid(column=0,
                     row=2,
                     padx=5,
                     pady=5,
                     ipadx=5,
                     ipady=5)
        text_2.grid(column=0,
                    row=3,
                    sticky=tk.W,
                    padx=5,
                    pady=0,
                    ipadx=20,
                    ipady=0)
        title_3.grid(column=0,
                     row=4,
                     padx=5,
                     pady=5,
                     ipadx=5,
                     ipady=5)
        text_3.grid(column=0,
                    row=5,
                    sticky=tk.W,
                    padx=5,
                    pady=0,
                    ipadx=20,
                    ipady=0)
        sub_final.columnconfigure(0, weight=1)
        self.init_Results(self.pages["final"], 4)

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
                            bg=self.background)
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
            web = self.d1.get_list("URL")
            dog_breed = {}
            for i in range(len(name_list)):
                dog_breed[name_list[i]] = web[i]
            webbrowser.open(f"{dog_breed[name]}")

    def order(self, name):
        list_name = [int(i) for i in self.d2.get_list(name)]
        o_level = {}
        count = 1
        for i in list_name:
            if i not in o_level:
                o_level[i] = f"{count}"
            else:
                o_level[i] += f", {count}"
            count += 1
        o_level_list = [i for i, j in o_level.items()]
        o_level_list.sort()
        order_list = []
        for i in o_level_list:
            order_list.append(o_level[i])
        return " < ".join(order_list)

    @staticmethod
    def focus_in(entry):
        entry.delete(0, tk.END)

    @staticmethod
    def focus_out(entry, word):
        entry.delete(0, tk.END)
        entry.insert(0, word)

    @staticmethod
    def skewed(skewness):
        if -0.5 < skewness < 0.5:
            return "Symmetric Distribution"
        elif -0.5 >= skewness:
            if -1 >= skewness:
                return "Highly Negative Skewed Distribution"
            return "Negative Skewed Distribution"
        elif 1 <= skewness:
            return "Highly Positive Skewed Distribution"
        return "Positive Skewed Distribution"

    @staticmethod
    def find_cor(cor):
        if cor == 0:
            return "No Linear Relationship"
        elif 0 < cor <= 0.1:
            return "Weak Positive Relationship"
        elif -0.1 <= cor < 0:
            return "Weak Negative Relationship"
        elif 0.1 < cor <= 0.4:
            return "Weak Positive Relationship"
        elif -0.4 <= cor < -0.1:
            return "Weak Negative Relationship"
        elif 0.4 < cor <= 0.7:
            return "Moderate Positive Relationship"
        elif -0.7 <= cor < -0.4:
            return "Moderate Negative Relationship"
        elif cor < 0.7:
            return "Strong Positive Relationship"
        return "Strong Negative Relationship"

    def result_cor(self, t1, t2):
        cor = self.d1.d[[t1, t2]].corr().iloc[0, 1]
        if cor == 0:
            return (f"   There is no linear relationship ({cor:.4f}) between "
                    f"{t1} and {t2}. This suggests that there is no "
                    f"relationship between these aspects.")
        elif 0 < cor <= 0.1:
            return (f"   There is a weak positive relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This is very close to zero, "
                    f"suggesting that there is no relationship between "
                    f"these aspects.")
        elif -0.1 <= cor < 0:
            return (f"   There is a weak negative relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This is very close to zero, "
                    f"suggesting that there is no relationship between "
                    f"these aspects.")
        elif 0.1 < cor <= 0.4:
            return (f"   There is a weak positive relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This suggests that there is a "
                    f"slight tendency for a dog breed with a higher {t1} "
                    f"level to also have a higher {t2} level.")
        elif -0.4 <= cor < -0.1:
            return (f"   There is a weak negative relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This suggests that there is a "
                    f"slight tendency for a dog breed with a higher {t1} "
                    f"level to have a lower {t2} level.")
        elif 0.4 < cor <= 0.7:
            return (f"   There is a moderate positive relationship ({cor:.4f})"
                    f" between {t1} and {t2}. This suggests that there is a "
                    f"clear tendency for a dog breed with a higher {t1} "
                    f"level to also have a higher {t2} level.")
        elif -0.7 <= cor < -0.4:
            return (f"   There is a moderate negative relationship ({cor:.4f})"
                    f" between {t1} and {t2}. This suggests that there is a "
                    f"clear tendency for a dog breed with a higher {t1} "
                    f"level to have a lower {t2} level.")
        elif cor < 0.7:
            return (f"   There is a strong positive relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This suggests that there is a "
                    f"strong tendency for a dog breed with a higher {t1} "
                    f"level to also have a higher {t2} level.")
        else:
            return (f"   There is a strong negative relationship ({cor:.4f}) "
                    f"between {t1} and {t2}. This suggests that there is a "
                    f"strong tendency for a dog breed with a higher {t1} "
                    f"level to have a lower {t2} level.")

    def histogram(self, name, page, column, row, span, df, x, x_name, y_name):
        fig, ax = plt.subplots()
        sns.histplot(data=df,
                     x=x,
                     binwidth=0.2,
                     kde=True,
                     color=self.pitch,
                     ax=ax)
        ax.set_xlabel(x_name,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel(y_name,
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"The histogram of all levels of\n{name}",
                     fontsize=10,
                     fontfamily=self.font_fam)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        ax.grid(True)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span,
                                    pady=15)
        plt.close(fig)

    def his_change(self):
        self.show_page_2("his_page", "histogram")
        all_list = []
        name_list = []
        self.text.grid_remove()
        if not self.v1.get() and not self.v2.get() and not self.v3.get():
            messagebox.showwarning(f"Can't uncheck all",
                                   f"You can't uncheck all three.")
            self.v1.set(True)
            self.v2.set(True)
            self.v3.set(True)
        if self.v1.get():
            all_list += self.d1.get_list(f"{self.m_t1}")
            name_list.append(f"{self.m_t1}")
        if self.v2.get():
            all_list += self.d1.get_list(f"{self.m_t2}")
            name_list.append(f"{self.m_t2}")
        if self.v3.get():
            all_list += self.d1.get_list(f"{self.m_t3}")
            name_list.append(f"{self.m_t3}")
        df = pd.DataFrame({"histogram_list": all_list})
        name = ", ".join(name_list)
        self.histogram(name,
                       self.pages_2["his_page"],
                       0,
                       0,
                       6,
                       df,
                       "histogram_list",
                       "Level",
                       "Frequency of level")
        skewness = stats.skew(df["histogram_list"])
        skewed = self.skewed(skewness)
        self.skew.set(f"The Distribution: {skewed}")
        self.text.grid()

    def scatter(self, page, column, row, span, df, x, y):
        fig, ax = plt.subplots()
        sns.regplot(data=df,
                    x=x,
                    y=y,
                    color=self.main,
                    line_kws={"color": self.background},
                    ax=ax)
        ax.set_xlabel(f"Levels of {x}",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel(f"Levels of {y}",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"{x} vs {y}",
                     fontsize=10,
                     fontfamily=self.font_fam)
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=span,
                                    padx=10,
                                    pady=15)
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

    def bar(self, name, page, column, row, c_span, r_span, df, color):
        self.melted_df = df.melt(id_vars="Level",
                                 var_name="Each Topic",
                                 value_name="val")
        fig, ax = plt.subplots()
        sns.barplot(data=self.melted_df,
                    x="Level",
                    y="val",
                    hue="Each Topic",
                    palette=color,
                    ax=ax)
        ax.set_xlabel("Level",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_ylabel("Frequency of Level",
                      fontsize=10,
                      fontfamily=self.font_fam)
        ax.set_title(f"The bar graph of levels of\n{name}",
                     fontsize=10,
                     fontfamily=self.font_fam)
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig,
                                   master=page)
        canvas.draw()
        canvas.get_tk_widget().grid(column=column,
                                    row=row,
                                    sticky=tk.NSEW,
                                    columnspan=c_span,
                                    rowspan=r_span)
        plt.close(fig)

    def bar_change(self):
        self.show_page_2("IPA_page", "IPA")
        name_dict = {}
        all_dict = {}
        color = []
        text_list = []
        text_val = []
        if (not self.IPA_v1.get()
                and not self.IPA_v2.get()
                and not self.IPA_v3.get()):
            messagebox.showwarning(f"Can't uncheck all",
                                   f"You can't uncheck all three.")
            self.IPA_v1.set(True)
            self.IPA_v2.set(True)
            self.IPA_v3.set(True)
        if self.IPA_v1.get():
            order = self.order(f"{self.t1}")
            name_dict[f"{self.t1}"] = f"{self.t1}"
            color.append(self.main)
            text_list.append(tk.Label(self.pages_2["IPA_page"],
                                      text=f"\n{self.t1}",
                                      font=(self.font, 20),
                                      bg=self.background,
                                      fg=self.dark))
            text_val.append(tk.Label(self.pages_2["IPA_page"],
                                     text=f"  {order}",
                                     font=(self.font, 20),
                                     bg=self.background,
                                     fg=self.dark))
        if self.IPA_v2.get():
            order = self.order(f"{self.t2}")
            name_dict[f"{self.t2}"] = f"{self.t2}"
            color.append(self.background)
            text_list.append(tk.Label(self.pages_2["IPA_page"],
                                      text=f"\n{self.t2}",
                                      font=(self.font, 20),
                                      bg=self.background,
                                      fg=self.dark))
            text_val.append(tk.Label(self.pages_2["IPA_page"],
                                     text=f"  {order}",
                                     font=(self.font, 20),
                                     bg=self.background,
                                     fg=self.dark))
        if self.IPA_v3.get():
            order = self.order(f"{self.t3}")
            name_dict[f"{self.t3}"] = f"{self.t3}"
            color.append(self.pitch)
            text_list.append(tk.Label(self.pages_2["IPA_page"],
                                      text=f"\n{self.t3}",
                                      font=(self.font, 20),
                                      bg=self.background,
                                      fg=self.dark))
            text_val.append(tk.Label(self.pages_2["IPA_page"],
                                     text=f"  {order}",
                                     font=(self.font, 20),
                                     bg=self.background,
                                     fg=self.dark))
        all_dict["Level"] = self.d2.get_list("Level")
        for i, j in name_dict.items():
            all_dict.update({i: self.d2.get_list(j)})
        df = pd.DataFrame(all_dict)
        name = ", ".join([i for i, j in name_dict.items()])
        self.bar(name,
                 self.pages_2["IPA_page"],
                 0,
                 0,
                 3,
                 6,
                 df,
                 color)
        count = 0
        count_val = 0
        for i in text_list:
            text = i
            val = text_val[count_val]
            text.grid(column=3,
                      row=count,
                      sticky="WN",
                      ipadx=20)
            count += 1
            val.grid(column=3,
                     row=count,
                     sticky="WN",
                     ipadx=20)
            count += 1
            count_val += 1

    def close_window_and_exit(self):
        self.destroy()
        self.quit()
