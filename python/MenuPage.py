import sys
from tkinter import messagebox as tkMessageBox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import MenuPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    MenuPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    MenuPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    
    def Exit(self):
        msg= tkMessageBox.askyesno("Exit","Are you sure, you want to Exit?");
        if(msg):
            root.destroy()

    def Stockview(self):
        import StockPage
        root.destroy()
        StockPage.vp_start_gui()

    def Tranview(self):
        import TransactionPage
        root.destroy()
        TransactionPage.vp_start_gui()
            
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("855x618+510+206")
        top.minsize(120, 1)
        top.maxsize(3804, 1901)
        top.resizable(1,  1)
        top.title("I-ventory")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.035, rely=-0.016, relheight=1.028
                , relwidth=1.05)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#0000a0")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")

        self.BtnViewStock = tk.Button(self.Frame1)
        self.BtnViewStock.place(relx=0.045, rely=0.031, height=50, width=150)
        self.BtnViewStock.configure(activebackground="#ececec")
        self.BtnViewStock.configure(activeforeground="#000000")
        self.BtnViewStock.configure(background="#d9d9d9")
        self.BtnViewStock.configure(disabledforeground="#a3a3a3")
        self.BtnViewStock.configure(foreground="#000000")
        self.BtnViewStock.configure(highlightbackground="#d9d9d9")
        self.BtnViewStock.configure(highlightcolor="black")
        self.BtnViewStock.configure(pady="0")
        self.BtnViewStock.configure(text='''View Stock''')
        self.BtnViewStock.configure(command= self.Stockview)

        self.BtnViewTransaction = tk.Button(self.Frame1)
        self.BtnViewTransaction.place(relx=0.223, rely=0.031, height=50
                , width=150)
        self.BtnViewTransaction.configure(activebackground="#ececec")
        self.BtnViewTransaction.configure(activeforeground="#000000")
        self.BtnViewTransaction.configure(background="#d9d9d9")
        self.BtnViewTransaction.configure(disabledforeground="#a3a3a3")
        self.BtnViewTransaction.configure(foreground="#000000")
        self.BtnViewTransaction.configure(highlightbackground="#d9d9d9")
        self.BtnViewTransaction.configure(highlightcolor="black")
        self.BtnViewTransaction.configure(pady="0")
        self.BtnViewTransaction.configure(text='''View Transaction''')
        self.BtnViewTransaction.configure(command= self.Tranview)
        
        

        self.BtnExit = tk.Button(self.Frame1)
        self.BtnExit.place(relx=0.401, rely=0.031, height=50, width=150)
        self.BtnExit.configure(activebackground="#ececec")
        self.BtnExit.configure(activeforeground="#000000")
        self.BtnExit.configure(background="#d9d9d9")
        self.BtnExit.configure(disabledforeground="#a3a3a3")
        self.BtnExit.configure(foreground="#000000")
        self.BtnExit.configure(highlightbackground="#d9d9d9")
        self.BtnExit.configure(highlightcolor="black")
        self.BtnExit.configure(pady="0")
        self.BtnExit.configure(text='''Exit''')
        self.BtnExit.configure(command= self.Exit)

        self.LabelWel = tk.Label(self.Frame1)
        self.LabelWel.place(relx=0.2, rely=0.3, height=100, width=524)
        self.LabelWel.configure(background="#0000a0")
        self.LabelWel.configure(disabledforeground="#a3a3a3")
        self.LabelWel.configure(font="-family {Segoe UI Variable Small} -size 50 -weight bold")
        self.LabelWel.configure(foreground="#ffffff")
        self.LabelWel.configure(text='''Welcome''')

        self.LabelTo = tk.Label(self.Frame1)
        self.LabelTo.place(relx=0.2, rely=0.5, height=100, width=524)
        self.LabelTo.configure(background="#0000a0")
        self.LabelTo.configure(disabledforeground="#a3a3a3")
        self.LabelTo.configure(font="-family {Segoe UI Variable Small} -size 50 -weight bold")
        self.LabelTo.configure(foreground="#ffffff")
        self.LabelTo.configure(text='''To''')

        self.LabelI = tk.Label(self.Frame1)
        self.LabelI.place(relx=0.2, rely=0.7, height=100, width=524)
        self.LabelI.configure(background="#0000a0")
        self.LabelI.configure(disabledforeground="#a3a3a3")
        self.LabelI.configure(font="-family {Segoe UI Variable Small} -size 50 -weight bold")
        self.LabelI.configure(foreground="#ffffff")
        self.LabelI.configure(text='''I-ventory''')



if __name__ == '__main__':
    vp_start_gui()





