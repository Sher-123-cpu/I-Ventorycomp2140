import sys
import pandas as pd
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog, ttk

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

import StockPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    StockPage_support.init(root, top)
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
    StockPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def add(self):
        CP = int(self.EntryCP.get())
        SP = int(self.EntrySP.get())
        P=CP-SP
        table = (self.EntryPro.get(), self.EntryQua.get(),self.EntryCP.get(),self.EntrySP.get(),P,self.EntryEx.get(),"0")
        self.frame.insert(parent='', index=0,values=table)
        f = open("stock.txt", "a")
        f.write(self.EntryPro.get()+"\n",)
        f.write(self.EntryQua.get()+"\n",)
        f.write(self.EntryCP.get()+"\n",)
        f.write(self.EntrySP.get()+"\n",)
        f.write(str(P)+"\n",)
        f.write(self.EntryEx.get()+"\n",)
        f.write("0\n",)
        f.close()

    def update(self):
        f = open("stock.txt", "r")
        ls=['','','','','','','',]
        count=0
        for line in f:
            ls[count]= line
            if (count==6):
                count=0
                table = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6])
                self.frame.insert(parent='', index=0,values=table)
            else:
                count+=1
                       
    def Exit(self):
        msg= tkMessageBox.askyesno("Exit","Are you sure, you want to Exit?");
        if(msg):
            root.destroy()
            
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

        cols = ('Product','Quantity','Cost Price','Selling Price','Profit/Loss','Expiration','Amount Sold')
        self.frame = ttk.Treeview(self.Frame1, columns = cols, show='headings')
        self.frame.place(relx=0.045, rely=0.22, relheight=0.463, relwidth=0.931)
        self.scrolly = tk.Scrollbar(self.frame, orient= "vertical", command=self.frame.yview)
        self.scrollx = tk.Scrollbar(self.frame, orient= "horizontal", command=self.frame.xview)
        self.frame.configure(xscrollcommand= self.scrollx.set, yscrollcommand= self.scrolly.set)
        self.scrollx.pack(side="bottom",fill="x")
        self.scrolly.pack(side="right",fill="y")
        for col in cols:
            self.frame.heading(col,text=col)      

        self.Label_ViewTran = tk.Label(self.Frame1)
        self.Label_ViewTran.place(relx=0.401, rely=0.157, height=31, width=184)
        self.Label_ViewTran.configure(activebackground="#f9f9f9")
        self.Label_ViewTran.configure(activeforeground="black")
        self.Label_ViewTran.configure(background="#0000a0")
        self.Label_ViewTran.configure(disabledforeground="#a3a3a3")
        self.Label_ViewTran.configure(font="-family {Segoe UI} -size 20")
        self.Label_ViewTran.configure(foreground="#ffffff")
        self.Label_ViewTran.configure(highlightbackground="#d9d9d9")
        self.Label_ViewTran.configure(highlightcolor="black")
        self.Label_ViewTran.configure(text='''View Stock''')

        self.BtnAdd = tk.Button(self.Frame1)
        self.BtnAdd.place(relx=0.423, rely=0.709, height=40, width=150)
        self.BtnAdd.configure(activebackground="#ececec")
        self.BtnAdd.configure(activeforeground="#000000")
        self.BtnAdd.configure(background="#d9d9d9")
        self.BtnAdd.configure(disabledforeground="#a3a3a3")
        self.BtnAdd.configure(foreground="#000000")
        self.BtnAdd.configure(highlightbackground="#d9d9d9")
        self.BtnAdd.configure(highlightcolor="black")
        self.BtnAdd.configure(pady="0")
        self.BtnAdd.configure(text='''Add Stock''')
        self.BtnAdd.configure(command=self.add)

        self.BtnDelete = tk.Button(self.Frame1)
        self.BtnDelete.place(relx=0.423, rely=0.787, height=40, width=150)
        self.BtnDelete.configure(activebackground="#ececec")
        self.BtnDelete.configure(activeforeground="#000000")
        self.BtnDelete.configure(background="#d9d9d9")
        self.BtnDelete.configure(disabledforeground="#a3a3a3")
        self.BtnDelete.configure(foreground="#000000")
        self.BtnDelete.configure(highlightbackground="#d9d9d9")
        self.BtnDelete.configure(highlightcolor="black")
        self.BtnDelete.configure(pady="0")
        self.BtnDelete.configure(text='''Delete Stock''')

        self.BtnUpdate = tk.Button(self.Frame1)
        self.BtnUpdate.place(relx=0.423, rely=0.866, height=40, width=150)
        self.BtnUpdate.configure(activebackground="#ececec")
        self.BtnUpdate.configure(activeforeground="#000000")
        self.BtnUpdate.configure(background="#d9d9d9")
        self.BtnUpdate.configure(disabledforeground="#a3a3a3")
        self.BtnUpdate.configure(foreground="#000000")
        self.BtnUpdate.configure(highlightbackground="#d9d9d9")
        self.BtnUpdate.configure(highlightcolor="black")
        self.BtnUpdate.configure(pady="0")
        self.BtnUpdate.configure(text='''Update''')
        self.BtnUpdate.configure(command=self.update)

        self.EntryPro = tk.Entry(self.Frame1)
        self.EntryPro.place(relx=0.145, rely=0.724, height=20, relwidth=0.171)
        self.EntryPro.configure(background="white")
        self.EntryPro.configure(disabledforeground="#a3a3a3")
        self.EntryPro.configure(font="TkFixedFont")
        self.EntryPro.configure(foreground="#000000")
        self.EntryPro.configure(insertbackground="black")

        self.EntryQua = tk.Entry(self.Frame1)
        self.EntryQua.place(relx=0.145, rely=0.772, height=20, relwidth=0.171)
        self.EntryQua.configure(background="white")
        self.EntryQua.configure(disabledforeground="#a3a3a3")
        self.EntryQua.configure(font="TkFixedFont")
        self.EntryQua.configure(foreground="#000000")
        self.EntryQua.configure(insertbackground="black")

        self.EntryCP = tk.Entry(self.Frame1)
        self.EntryCP.place(relx=0.145, rely=0.819, height=20, relwidth=0.171)
        self.EntryCP.configure(background="white")
        self.EntryCP.configure(disabledforeground="#a3a3a3")
        self.EntryCP.configure(font="TkFixedFont")
        self.EntryCP.configure(foreground="#000000")
        self.EntryCP.configure(insertbackground="black")
         
        self.EntrySP = tk.Entry(self.Frame1)
        self.EntrySP.place(relx=0.145, rely=0.866, height=20, relwidth=0.171)
        self.EntrySP.configure(background="white")
        self.EntrySP.configure(disabledforeground="#a3a3a3")
        self.EntrySP.configure(font="TkFixedFont")
        self.EntrySP.configure(foreground="#000000")
        self.EntrySP.configure(insertbackground="black")

        self.EntryEx = tk.Entry(self.Frame1)
        self.EntryEx.place(relx=0.145, rely=0.913, height=20, relwidth=0.171)
        self.EntryEx.configure(background="white")
        self.EntryEx.configure(disabledforeground="#a3a3a3")
        self.EntryEx.configure(font="TkFixedFont")
        self.EntryEx.configure(foreground="#000000")
        self.EntryEx.configure(insertbackground="black")
 
        self.Labelproduct = tk.Label(self.Frame1)
        self.Labelproduct.place(relx=0.056, rely=0.724, height=21, width=70)
        self.Labelproduct.configure(background="#d9d9d9")
        self.Labelproduct.configure(disabledforeground="#a3a3a3")
        self.Labelproduct.configure(foreground="#000000")
        self.Labelproduct.configure(text='''Product''')

        self.LabelQuantity = tk.Label(self.Frame1)
        self.LabelQuantity.place(relx=0.056, rely=0.772, height=21, width=70)
        self.LabelQuantity.configure(background="#d9d9d9")
        self.LabelQuantity.configure(disabledforeground="#a3a3a3")
        self.LabelQuantity.configure(foreground="#000000")
        self.LabelQuantity.configure(text='''Quantity''')

        self.LabelCP = tk.Label(self.Frame1)
        self.LabelCP.place(relx=0.056, rely=0.819, height=21, width=70)
        self.LabelCP.configure(background="#d9d9d9")
        self.LabelCP.configure(disabledforeground="#a3a3a3")
        self.LabelCP.configure(foreground="#000000")
        self.LabelCP.configure(text='''Cost Price''')

        self.LabelSP = tk.Label(self.Frame1)
        self.LabelSP.place(relx=0.056, rely=0.866, height=21, width=70)
        self.LabelSP.configure(background="#d9d9d9")
        self.LabelSP.configure(disabledforeground="#a3a3a3")
        self.LabelSP.configure(foreground="#000000")
        self.LabelSP.configure(text='''Selling Price''')

        self.LabelEx = tk.Label(self.Frame1)
        self.LabelEx.place(relx=0.056, rely=0.913, height=21, width=70)
        self.LabelEx.configure(background="#d9d9d9")
        self.LabelEx.configure(disabledforeground="#a3a3a3")
        self.LabelEx.configure(foreground="#000000")
        self.LabelEx.configure(text='''Expiration''')

if __name__ == '__main__':
    vp_start_gui()





