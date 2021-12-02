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

import LoginPage_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    LoginPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    LoginPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    
    def cancelLogin(self):
        msg= tkMessageBox.askyesno("Login page","Are you sure, you want to cancel login?");
        if(msg):
            root.destroy()
            
    def LoginUser(self):
        name = self.txtUsername.get();
        password = self.txtPassword.get();
        
        with open("members.txt")as f:
            if name and password in f.read():
                print("Login Successfull")
                root.destroy()
                import MenuPage
                MenuPage.vp_start_gui()
            else:
                print("Login Fail")
                             
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+300+300")
        top.minsize(120, 1)
        top.maxsize(3804, 1901)
        top.resizable(1,  1)
        top.title("I-ventory")
        top.configure(background="#d9d9d9")

        self.Frame_LoginPage = tk.Frame(top)
        self.Frame_LoginPage.place(relx=-0.033, rely=-0.022, relheight=1.033
                , relwidth=1.058)
        self.Frame_LoginPage.configure(relief='groove')
        self.Frame_LoginPage.configure(borderwidth="2")
        self.Frame_LoginPage.configure(relief="groove")
        self.Frame_LoginPage.configure(background="#0000a0")

        self.Label_LoginImage = tk.Label(self.Frame_LoginPage)
        self.Label_LoginImage.place(relx=0.016, rely=0.0, height=471, width=334)
        self.Label_LoginImage.configure(background="#ffffff")
        self.Label_LoginImage.configure(disabledforeground="#a3a3a3")
        self.Label_LoginImage.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"LPimage.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label_LoginImage.configure(image=_img0)
        self.Label_LoginImage.configure(text='''Label''')

        self.Label_LoginPage = tk.Label(self.Frame_LoginPage)
        self.Label_LoginPage.place(relx=0.646, rely=0.108, height=41, width=155)
        self.Label_LoginPage.configure(background="#0000a0")
        self.Label_LoginPage.configure(disabledforeground="#00ffff")
        self.Label_LoginPage.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label_LoginPage.configure(foreground="#ffffff")
        self.Label_LoginPage.configure(text='''Login Page''')

        self.Label_Username = tk.Label(self.Frame_LoginPage)
        self.Label_Username.place(relx=0.63, rely=0.323, height=21, width=165)
        self.Label_Username.configure(background="#0000a0")
        self.Label_Username.configure(disabledforeground="#a3a3a3")
        self.Label_Username.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Label_Username.configure(foreground="#ffffff")
        self.Label_Username.configure(text='''Username''')

        self.Label_Password = tk.Label(self.Frame_LoginPage)
        self.Label_Password.place(relx=0.63, rely=0.452, height=21, width=165)
        self.Label_Password.configure(background="#0000a0")
        self.Label_Password.configure(disabledforeground="#a3a3a3")
        self.Label_Password.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Label_Password.configure(foreground="#ffffff")
        self.Label_Password.configure(text='''Password''')

        self.txtUsername = tk.Entry(self.Frame_LoginPage)
        self.txtUsername.place(relx=0.646, rely=0.387, height=20, relwidth=0.243)

        self.txtUsername.configure(background="white")
        self.txtUsername.configure(disabledforeground="#a3a3a3")
        self.txtUsername.configure(font="TkFixedFont")
        self.txtUsername.configure(foreground="#000000")
        self.txtUsername.configure(insertbackground="black")

        self.txtPassword = tk.Entry(self.Frame_LoginPage)
        self.txtPassword.place(relx=0.646, rely=0.516, height=20, relwidth=0.243)

        self.txtPassword.configure(background="white")
        self.txtPassword.configure(disabledforeground="#a3a3a3")
        self.txtPassword.configure(font="TkFixedFont")
        self.txtPassword.configure(foreground="#000000")
        self.txtPassword.configure(insertbackground="black")
        self.txtPassword.configure(show="*")

        self.Btn_Login = tk.Button(self.Frame_LoginPage)
        self.Btn_Login.place(relx=0.724, rely=0.645, height=24, width=47)
        self.Btn_Login.configure(activebackground="#ececec")
        self.Btn_Login.configure(activeforeground="#000000")
        self.Btn_Login.configure(background="#d9d9d9")
        self.Btn_Login.configure(disabledforeground="#a3a3a3")
        self.Btn_Login.configure(foreground="#000000")
        self.Btn_Login.configure(highlightbackground="#d9d9d9")
        self.Btn_Login.configure(highlightcolor="black")
        self.Btn_Login.configure(pady="0")
        self.Btn_Login.configure(text='''Login''')
        self.Btn_Login.configure(command= self.LoginUser)

        self.Btn_Cancel = tk.Button(self.Frame_LoginPage)
        self.Btn_Cancel.place(relx=0.724, rely=0.753, height=24, width=47)
        self.Btn_Cancel.configure(activebackground="#ececec")
        self.Btn_Cancel.configure(activeforeground="#000000")
        self.Btn_Cancel.configure(background="#d9d9d9")
        self.Btn_Cancel.configure(disabledforeground="#a3a3a3")
        self.Btn_Cancel.configure(foreground="#000000")
        self.Btn_Cancel.configure(highlightbackground="#d9d9d9")
        self.Btn_Cancel.configure(highlightcolor="black")
        self.Btn_Cancel.configure(pady="0")
        self.Btn_Cancel.configure(text='''Cancel''')
        self.Btn_Cancel.configure(command= self.cancelLogin)

if __name__ == '__main__':
    vp_start_gui()





