import customtkinter


class AppTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Overview")
        self.add("Armor Piece")
        self.add("Talent")
        # self.set("Overview")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1000x562")
        self.minsize(480, 180)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = AppTabView(master=self)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.mainframe = customtkinter.CTkFrame(master=self.tabview.tab("Overview"))
        self.mainframe.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.defgrid = customtkinter.CTkFrame(master=self.mainframe, border_color="blue", border_width=10)
        self.defgrid.grid(row=0, column=0)
        self.skillgrid = customtkinter.CTkFrame(master=self.mainframe, border_color="red", border_width=10)
        self.skillgrid.grid(row=1, column=0)
        self.piecelist = customtkinter.CTkFrame(master=self.mainframe, border_color="black", border_width=10)
        self.piecelist.grid(row=0, column=1, rowspan=2, sticky="ns")


app = App()
app.mainloop()
