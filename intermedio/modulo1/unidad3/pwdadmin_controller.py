from tkinter import Tk
import pwdadmin_view

class Controller():
    def __init__(self, root_tk):
        self.root_tk = root_tk
        self.view = pwdadmin_view.View(self.root_tk)

if __name__ == "__main__":
    master = Tk()                    # INICIO Loop de TKinter
    miapp = Controller(master)
    master.mainloop()                # FINALIZO Loop de TKinter
