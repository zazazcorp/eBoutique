#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 25, 2018 10:35:39 PM

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

import About_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = A_Propos (root)
    About_support.init(root, top)
    root.mainloop()

w = None
def create_A_Propos(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = A_Propos (w)
    About_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_A_Propos():
    global w
    w.destroy()
    w = None


class A_Propos:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("769x614+301+61")
        top.title("A Propos")
        top.configure(background="#c14915")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.08, rely=0.05, height=31, width=154)
        self.Label1.configure(background="#c14915")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#605b54")
        self.Label1.configure(text='''Aide''')
        self.Label1.configure(width=154)

        self.Label1_1 = Label(top)
        self.Label1_1.place(relx=0.74, rely=0.05, height=31, width=154)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#c14915")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font9)
        self.Label1_1.configure(foreground="#605b54")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''A Propos''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.11, height=111, width=154)
        self.Label2.configure(background="#c14915")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = PhotoImage(file="../image/Help_96px.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(width=154)

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.6, rely=0.11, height=101, width=254)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="white")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="../image/eBoutique.png")
        self.Label2_2.configure(image=self._img2)
        self.Label2_2.configure(width=254)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.03, rely=0.31, relheight=0.27, relwidth=0.44)
        self.Message1.configure(background="#0b0b1c")
        self.Message1.configure(cursor="boat")
        self.Message1.configure(font=font10)
        self.Message1.configure(foreground="white")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(relief=RAISED)
        self.Message1.configure(text='''Pour une utilisation optimale de cette platte forme , voir le fichier README.TXT , ou aller sur le site de www.zcorp.inc''')
        self.Message1.configure(width=340)

        self.Message1_3 = Message(top)
        self.Message1_3.place(relx=0.48, rely=0.31, relheight=0.49
                , relwidth=0.51)
        self.Message1_3.configure(aspect="1000")
        self.Message1_3.configure(background="#0b0b1c")
        self.Message1_3.configure(cursor="boat")
        self.Message1_3.configure(font=font10)
        self.Message1_3.configure(foreground="white")
        self.Message1_3.configure(highlightbackground="#d9d9d9")
        self.Message1_3.configure(highlightcolor="black")
        self.Message1_3.configure(relief=RAISED)
        self.Message1_3.configure(text='''eBoutique v1.0 est une application de gestion simple de stock, d'une boutique de vente d'article  Open Source
                                          Copyrights python3 by zcorp Issouf ZANNE alias zcorp  developpeur Web , Mobile et Logiciel   : issoufzanne52@gmail.com 
                                          , l'Ingenieur Informaticien M. Fayçal DOUAMBA''')
        self.Message1_3.configure(width=390)






if __name__ == '__main__':
    vp_start_gui()


