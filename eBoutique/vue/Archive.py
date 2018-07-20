#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 23, 2018 10:43:56 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Archive_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gerer_les_Archives(root)
    Archive_support.init(root, top)
    root.mainloop()

w = None
def create_Gerer_les_Archives(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gerer_les_Archives (w)
    Archive_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Gerer_les_Archives():
    global w
    w.destroy()
    w = None


class Gerer_les_Archives:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Cambria Math} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Showcard Gothic} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("700x668+263+4")
        top.title("Gerer les Archives")
        top.configure(background="#0b0b1c")
        top.resizable(0,0)


        self.labArch = Label(top)
        self.labArch.place(relx=0.0, rely=0.58, height=131, width=154)
        self.labArch.configure(activebackground="#f9f9f9")
        self.labArch.configure(activeforeground="black")
        self.labArch.configure(background="#c14915")
        self.labArch.configure(borderwidth="1")
        self.labArch.configure(cursor="hand2")
        self.labArch.configure(disabledforeground="#a3a3a3")
        self.labArch.configure(font=font9)
        self.labArch.configure(foreground="white")
        self.labArch.configure(highlightbackground="#d9d9d9")
        self.labArch.configure(highlightcolor="black")
        self.labArch.configure(text='''Archives''')

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.21, rely=0.0, relheight=0.79, relwidth=0.72)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#c14915")
        self.Frame1.configure(width=435)

        self.labVente = Label(self.Frame1)
        self.labVente.place(relx=0.04, rely=0.1, height=191, width=214)
        self.labVente.configure(background="#c14915")
        self.labVente.configure(borderwidth="1")
        self.labVente.configure(cursor="hand2")
        self.labVente.configure(disabledforeground="#a3a3a3")
        self.labVente.configure(foreground="#000000")
        self._img1 = PhotoImage(file="../image/Shopping Cart Loaded_96px.png")
        self.labVente.configure(image=self._img1)
        self.labVente.configure(relief=RAISED)
        self.labVente.configure(width=234)

        self.labCompte = Label(self.Frame1)
        self.labCompte.place(relx=0.55, rely=0.1, height=191, width=214)
        self.labCompte.configure(activebackground="#f9f9f9")
        self.labCompte.configure(activeforeground="black")
        self.labCompte.configure(background="#c14915")
        self.labCompte.configure(borderwidth="1")
        self.labCompte.configure(cursor="hand2")
        self.labCompte.configure(disabledforeground="#a3a3a3")
        self.labCompte.configure(foreground="#000000")
        self.labCompte.configure(highlightbackground="#d9d9d9")
        self.labCompte.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="../image/Coins_96px.png")
        self.labCompte.configure(image=self._img2)
        self.labCompte.configure(relief=RAISED)

        self.labFact = Label(self.Frame1)
        self.labFact.place(relx=0.04, rely=0.61, height=191, width=214)
        self.labFact.configure(activebackground="#f9f9f9")
        self.labFact.configure(activeforeground="black")
        self.labFact.configure(background="#c14915")
        self.labFact.configure(borderwidth="1")
        self.labFact.configure(cursor="hand2")
        self.labFact.configure(disabledforeground="#a3a3a3")
        self.labFact.configure(foreground="#000000")
        self.labFact.configure(highlightbackground="#d9d9d9")
        self.labFact.configure(highlightcolor="black")
        self._img3 = PhotoImage(file="../image/Pricing Structure_96px.png")
        self.labFact.configure(image=self._img3)
        self.labFact.configure(relief=RAISED)

        self.labBilan = Label(self.Frame1)
        self.labBilan.place(relx=0.53, rely=0.61, height=191, width=214)
        self.labBilan.configure(activebackground="#f9f9f9")
        self.labBilan.configure(activeforeground="black")
        self.labBilan.configure(background="#c14915")
        self.labBilan.configure(borderwidth="1")
        self.labBilan.configure(cursor="hand2")
        self.labBilan.configure(disabledforeground="#a3a3a3")
        self.labBilan.configure(foreground="#000000")
        self.labBilan.configure(highlightbackground="#d9d9d9")
        self.labBilan.configure(highlightcolor="black")
        self._img4 = PhotoImage(file="../image/Money Bag_96px.png")
        self.labBilan.configure(image=self._img4)
        self.labBilan.configure(relief=RAISED)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.08, rely=0.04, height=31, width=164)
        self.Label3.configure(background="#c14915")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#605b54")
        self.Label3.configure(text='''Vente Realises''')
        self.Label3.configure(width=164)

        self.Label3_5 = Label(self.Frame1)
        self.Label3_5.place(relx=0.59, rely=0.04, height=31, width=164)
        self.Label3_5.configure(activebackground="#f9f9f9")
        self.Label3_5.configure(activeforeground="black")
        self.Label3_5.configure(background="#c14915")
        self.Label3_5.configure(disabledforeground="#a3a3a3")
        self.Label3_5.configure(font=font10)
        self.Label3_5.configure(foreground="#605b54")
        self.Label3_5.configure(highlightbackground="#d9d9d9")
        self.Label3_5.configure(highlightcolor="black")
        self.Label3_5.configure(text='''Chiffre d'Affaire ''')

        self.Label3_6 = Label(self.Frame1)
        self.Label3_6.place(relx=0.08, rely=0.55, height=31, width=174)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#c14915")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font10)
        self.Label3_6.configure(foreground="#605b54")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="black")
        self.Label3_6.configure(text='''Factures ''')

        self.Label3_7 = Label(self.Frame1)
        self.Label3_7.place(relx=0.57, rely=0.55, height=31, width=174)
        self.Label3_7.configure(activebackground="#f9f9f9")
        self.Label3_7.configure(activeforeground="black")
        self.Label3_7.configure(background="#c14915")
        self.Label3_7.configure(disabledforeground="#a3a3a3")
        self.Label3_7.configure(font=font10)
        self.Label3_7.configure(foreground="#605b54")
        self.Label3_7.configure(highlightbackground="#d9d9d9")
        self.Label3_7.configure(highlightcolor="black")
        self.Label3_7.configure(text='''Bilan Global ''')







if __name__ == '__main__':
    vp_start_gui()



