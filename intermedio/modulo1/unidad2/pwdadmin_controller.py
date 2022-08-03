from tkinter import Tk
import pwdadmin_view

if __name__ == "__main__":
    master = Tk()                    # INICIO Loop de TKinter
    pwdadmin_view.show_view(master)
    master.mainloop()                # FINALIZO Loop de TKinter
