import customtkinter


class AppTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        self.add("Overview")
        self.add("Armor Piece")
        self.add("Talent")

        self.tab("Overview").grid_columnconfigure(0, weight=1)
        self.tab("Overview").grid_rowconfigure(0, weight=1)


class OverviewMainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class SkillTable:
    def __init__(self, root, data):
        skillMaxLenght = max([len(j) for j in [i[0] for i in data]])
        active_Skill_Max_Lenght = max([len(j) for j in [i[1] for i in data]])


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MHFU Set Builder")
        self.geometry("1000x562")
        self.minsize(480, 180)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tabview = AppTabView(master=self)
        self.overviewMainframe = OverviewMainFrame(master=self.tabview.tab("Overview"))

        self.skillgrid = customtkinter.CTkFrame(master=self.overviewMainframe, border_color="red", border_width=10)
        self.skillgrid.grid(row=0, column=0, sticky="nsew")

        self.miscgrid = customtkinter.CTkFrame(master=self.overviewMainframe)
        self.miscgrid.grid(row=1, column=0, sticky="nsew")
        self.miscgrid.grid_columnconfigure(0, weight=1)
        self.miscgrid.grid_columnconfigure(1, weight=1)
        self.miscgrid.grid_rowconfigure(0, weight=1)

        self.defgrid = customtkinter.CTkFrame(master=self.miscgrid, border_color="darkblue", border_width=5)
        self.defgrid.grid(row=0, column=0, sticky="nsew")

        self.objectgrid = customtkinter.CTkFrame(master=self.miscgrid, border_color="lightblue", border_width=5)
        self.objectgrid.grid(row=0, column=1, sticky="nsew")

        self.piecelist = customtkinter.CTkFrame(master=self.overviewMainframe, border_color="black", border_width=10)
        self.piecelist.grid(row=0, column=1, rowspan=2, sticky="nsew")


if __name__ == '__main__':
    app = App()
    app.mainloop()
