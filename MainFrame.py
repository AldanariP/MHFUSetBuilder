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


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1000x562")
        self.minsize(480, 180)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tabview = AppTabView(master=self)
        self.mainframe = MainFrame(master=self.tabview.tab("Overview"))

        self.defgrid = customtkinter.CTkFrame(master=self.mainframe, border_color="blue", border_width=10)
        self.defgrid.grid(row=0, column=0, sticky="nsew")
        self.skillgrid = customtkinter.CTkFrame(master=self.mainframe, border_color="red", border_width=10)
        self.skillgrid.grid(row=1, column=0, sticky="nsew")
        self.piecelist = customtkinter.CTkFrame(master=self.mainframe, border_color="black", border_width=10)
        self.piecelist.grid(row=0, column=1, rowspan=2, sticky="nsew")


app = App()
app.mainloop()
