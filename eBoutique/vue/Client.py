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

import Client_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gerer_les_Clients (root)
    Client_support.init(root, top)
    root.mainloop()

w = None
def create_Gerer_les_Clients(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gerer_les_Clients (w)
    Client_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Gerer_les_Clients():
    global w
    w.destroy()
    w = None


class Gerer_les_Clients:
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
        top.title("Gerer les Clients")
        top.configure(background="#0b0b1c")
        top.resizable(0,0)



        

        

        self.labClient = Label(top)
        self.labClient.place(relx=0.0, rely=0.39, height=131, width=154)
        self.labClient.configure(activebackground="#f9f9f9")
        self.labClient.configure(activeforeground="black")
        self.labClient.configure(background="#c14915")
        self.labClient.configure(borderwidth="1")
        self.labClient.configure(cursor="hand2")
        self.labClient.configure(disabledforeground="#a3a3a3")
        self.labClient.configure(font=font9)
        self.labClient.configure(foreground="white")
        self.labClient.configure(highlightbackground="#d9d9d9")
        self.labClient.configure(highlightcolor="black")
        self.labClient.configure(text='''Clients''')


        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.21, rely=0.0, relheight=0.79, relwidth=0.72)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#c14915")
        self.Frame1.configure(width=435)

        self.labList = Label(self.Frame1)
        self.labList.place(relx=0.04, rely=0.1, height=191, width=214)
        self.labList.configure(background="#c14915")
        self.labList.configure(borderwidth="1")
        self.labList.configure(cursor="hand2")
        self.labList.configure(disabledforeground="#a3a3a3")
        self.labList.configure(foreground="#000000")
        self._img1 = PhotoImage(file="../image/User Groups_96px.png")
        self.labList.configure(image=self._img1)
        self.labList.configure(relief=RAISED)
        self.labList.configure(width=234)

        self.labGere = Label(self.Frame1)
        self.labGere.place(relx=0.55, rely=0.1, height=191, width=214)
        self.labGere.configure(activebackground="#f9f9f9")
        self.labGere.configure(activeforeground="black")
        self.labGere.configure(background="#c14915")
        self.labGere.configure(borderwidth="1")
        self.labGere.configure(cursor="hand2")
        self.labGere.configure(disabledforeground="#a3a3a3")
        self.labGere.configure(foreground="#000000")
        self.labGere.configure(highlightbackground="#d9d9d9")
        self.labGere.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="../image/Stack_96px.png")
        self.labGere.configure(image=self._img2)
        self.labGere.configure(relief=RAISED)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.08, rely=0.04, height=31, width=164)
        self.Label3.configure(background="#c14915")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#605b54")
        self.Label3.configure(text='''Liste des Clients''')
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
        self.Label3_5.configure(text='''Bilan Client''')










if __name__ == '__main__':
    vp_start_gui()


