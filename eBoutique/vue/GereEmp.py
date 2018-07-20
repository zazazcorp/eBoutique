#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 25, 2018 05:36:12 PM

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

import GereEmp_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gestion_des_Employes (root)
    GereEmp_support.init(root, top)
    root.mainloop()

w = None
def create_Gestion_des_Employes(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gestion_des_Employes (w)
    GereEmp_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Gestion_des_Employes():
    global w
    w.destroy()
    w = None


class Gestion_des_Employes:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font11 = "-family {Courier New} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("1129x668+81+11")
        top.title("Gestion des Employes")
        top.configure(borderwidth="1")
        top.configure(background="#c14915")
        top.resizable(0,0)



        self.Label1 = Label(top)
        self.Label1.place(relx=0.38, rely=0.01, height=41, width=304)
        self.Label1.configure(background="#c14915")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#605b54")
        self.Label1.configure(text='''Gerer les Employes''')
        self.Label1.configure(width=304)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.07, height=141, width=174)
        self.Label2.configure(background="#c14915")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = PhotoImage(file="../image/Add User Group Man Man_96px.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(width=174)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.02, rely=0.31, height=31, width=164)
        self.Label3.configure(background="#0b0b1c")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#c14915")
        self.Label3.configure(relief=RAISED)
        self.Label3.configure(text='''Nom Utilisateur''')
        self.Label3.configure(width=164)

        self.Label3_1 = Label(top)
        self.Label3_1.place(relx=0.17, rely=0.3, height=41, width=224)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#0b0b1c")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font=font10)
        self.Label3_1.configure(foreground="#c14915")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(relief=RAISED)
        self.Label3_1.configure(text='''Nom Complet''')
        self.Label3_1.configure(width=224)

        self.listUser = Listbox(top)
        self.listUser.place(relx=0.02, rely=0.36, relheight=0.59, relwidth=0.15)
        self.listUser.configure(background="#c14915")
        self.listUser.configure(cursor="hand2")
        self.listUser.configure(disabledforeground="#a3a3a3")
        self.listUser.configure(font=font11)
        self.listUser.configure(foreground="#0b0b1c")
        self.listUser.configure(justify=CENTER)
        self.listUser.configure(relief=RAISED)
        self.listUser.configure(selectbackground="#0b0b1c")
        self.listUser.configure(selectforeground="#c14915")
        self.listUser.configure(width=164)

        self.listName = Listbox(top)
        self.listName.place(relx=0.17, rely=0.36, relheight=0.59, relwidth=0.2)
        self.listName.configure(background="#c14915")
        self.listName.configure(cursor="hand2")
        self.listName.configure(disabledforeground="#a3a3a3")
        self.listName.configure(font=font11)
        self.listName.configure(foreground="#0b0b1c")
        self.listName.configure(highlightbackground="#d9d9d9")
        self.listName.configure(highlightcolor="black")
        self.listName.configure(justify=CENTER)
        self.listName.configure(relief=RAISED)
        self.listName.configure(selectbackground="#0b0b1c")
        self.listName.configure(selectforeground="#c14915")
        self.listName.configure(width=224)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.56, rely=0.31, height=31, width=184)
        self.Label4.configure(background="#0b0b1c")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#c14915")
        self.Label4.configure(text='''Nom Entier :''')
        self.Label4.configure(width=184)

        self.Label4_3 = Label(top)
        self.Label4_3.place(relx=0.56, rely=0.41, height=31, width=184)
        self.Label4_3.configure(activebackground="#f9f9f9")
        self.Label4_3.configure(activeforeground="black")
        self.Label4_3.configure(background="#0b0b1c")
        self.Label4_3.configure(disabledforeground="#a3a3a3")
        self.Label4_3.configure(font=font9)
        self.Label4_3.configure(foreground="#c14915")
        self.Label4_3.configure(highlightbackground="#d9d9d9")
        self.Label4_3.configure(highlightcolor="black")
        self.Label4_3.configure(text='''Email''')

        self.Label4_4 = Label(top)
        self.Label4_4.place(relx=0.56, rely=0.5, height=31, width=184)
        self.Label4_4.configure(activebackground="#f9f9f9")
        self.Label4_4.configure(activeforeground="black")
        self.Label4_4.configure(background="#0b0b1c")
        self.Label4_4.configure(disabledforeground="#a3a3a3")
        self.Label4_4.configure(font=font9)
        self.Label4_4.configure(foreground="#c14915")
        self.Label4_4.configure(highlightbackground="#d9d9d9")
        self.Label4_4.configure(highlightcolor="black")
        self.Label4_4.configure(text='''Adresse''')

        self.Label4_5 = Label(top)
        self.Label4_5.place(relx=0.56, rely=0.59, height=31, width=184)
        self.Label4_5.configure(activebackground="#f9f9f9")
        self.Label4_5.configure(activeforeground="black")
        self.Label4_5.configure(background="#0b0b1c")
        self.Label4_5.configure(disabledforeground="#a3a3a3")
        self.Label4_5.configure(font=font9)
        self.Label4_5.configure(foreground="#c14915")
        self.Label4_5.configure(highlightbackground="#d9d9d9")
        self.Label4_5.configure(highlightcolor="black")
        self.Label4_5.configure(text='''Contacts''')

        self.Label4_6 = Label(top)
        self.Label4_6.place(relx=0.56, rely=0.68, height=31, width=184)
        self.Label4_6.configure(activebackground="#f9f9f9")
        self.Label4_6.configure(activeforeground="black")
        self.Label4_6.configure(background="#0b0b1c")
        self.Label4_6.configure(disabledforeground="#a3a3a3")
        self.Label4_6.configure(font=font9)
        self.Label4_6.configure(foreground="#c14915")
        self.Label4_6.configure(highlightbackground="#d9d9d9")
        self.Label4_6.configure(highlightcolor="black")
        self.Label4_6.configure(text='''Nom Utilisateur''')

        self.Label4_7 = Label(top)
        self.Label4_7.place(relx=0.56, rely=0.76, height=31, width=184)
        self.Label4_7.configure(activebackground="#f9f9f9")
        self.Label4_7.configure(activeforeground="black")
        self.Label4_7.configure(background="#0b0b1c")
        self.Label4_7.configure(disabledforeground="#a3a3a3")
        self.Label4_7.configure(font=font9)
        self.Label4_7.configure(foreground="#c14915")
        self.Label4_7.configure(highlightbackground="#d9d9d9")
        self.Label4_7.configure(highlightcolor="black")
        self.Label4_7.configure(text='''Mot de passe''')

        self.Label4_8 = Label(top)
        self.Label4_8.place(relx=0.56, rely=0.85, height=31, width=184)
        self.Label4_8.configure(activebackground="#f9f9f9")
        self.Label4_8.configure(activeforeground="black")
        self.Label4_8.configure(background="#0b0b1c")
        self.Label4_8.configure(disabledforeground="#a3a3a3")
        self.Label4_8.configure(font=font9)
        self.Label4_8.configure(foreground="#c14915")
        self.Label4_8.configure(highlightbackground="#d9d9d9")
        self.Label4_8.configure(highlightcolor="black")
        self.Label4_8.configure(text='''Privileges''')

        self.txtNom = Entry(top)
        self.txtNom.place(relx=0.75, rely=0.31,height=30, relwidth=0.22)
        self.txtNom.configure(background="#c14915")
        self.txtNom.configure(disabledforeground="#a3a3a3")
        self.txtNom.configure(font=font11)
        self.txtNom.configure(foreground="#0b0b1c")
        self.txtNom.configure(insertbackground="#0b0b1c")
        self.txtNom.configure(justify=CENTER)
        self.txtNom.configure(relief=RAISED)
        self.txtNom.configure(width=244)

        self.txtMail = Entry(top)
        self.txtMail.place(relx=0.75, rely=0.41,height=30, relwidth=0.22)
        self.txtMail.configure(background="#c14915")
        self.txtMail.configure(disabledforeground="#a3a3a3")
        self.txtMail.configure(font=font11)
        self.txtMail.configure(foreground="#0b0b1c")
        self.txtMail.configure(highlightbackground="#d9d9d9")
        self.txtMail.configure(highlightcolor="black")
        self.txtMail.configure(insertbackground="#0b0b1c")
        self.txtMail.configure(justify=CENTER)
        self.txtMail.configure(relief=RAISED)
        self.txtMail.configure(selectbackground="#c4c4c4")
        self.txtMail.configure(selectforeground="black")

        self.txtAdr = Entry(top)
        self.txtAdr.place(relx=0.75, rely=0.5,height=30, relwidth=0.22)
        self.txtAdr.configure(background="#c14915")
        self.txtAdr.configure(disabledforeground="#a3a3a3")
        self.txtAdr.configure(font=font11)
        self.txtAdr.configure(foreground="#0b0b1c")
        self.txtAdr.configure(highlightbackground="#d9d9d9")
        self.txtAdr.configure(highlightcolor="black")
        self.txtAdr.configure(insertbackground="#0b0b1c")
        self.txtAdr.configure(justify=CENTER)
        self.txtAdr.configure(relief=RAISED)
        self.txtAdr.configure(selectbackground="#c4c4c4")
        self.txtAdr.configure(selectforeground="black")

        self.txtTel = Entry(top)
        self.txtTel.place(relx=0.75, rely=0.59,height=30, relwidth=0.22)
        self.txtTel.configure(background="#c14915")
        self.txtTel.configure(disabledforeground="#a3a3a3")
        self.txtTel.configure(font=font11)
        self.txtTel.configure(foreground="#0b0b1c")
        self.txtTel.configure(highlightbackground="#d9d9d9")
        self.txtTel.configure(highlightcolor="black")
        self.txtTel.configure(insertbackground="#0b0b1c")
        self.txtTel.configure(justify=CENTER)
        self.txtTel.configure(relief=RAISED)
        self.txtTel.configure(selectbackground="#c4c4c4")
        self.txtTel.configure(selectforeground="black")

        self.txtUser = Entry(top)
        self.txtUser.place(relx=0.75, rely=0.68,height=30, relwidth=0.22)
        self.txtUser.configure(background="#c14915")
        self.txtUser.configure(disabledforeground="#a3a3a3")
        self.txtUser.configure(font=font11)
        self.txtUser.configure(foreground="#0b0b1c")
        self.txtUser.configure(highlightbackground="#d9d9d9")
        self.txtUser.configure(highlightcolor="black")
        self.txtUser.configure(insertbackground="#0b0b1c")
        self.txtUser.configure(justify=CENTER)
        self.txtUser.configure(relief=RAISED)
        self.txtUser.configure(selectbackground="#c4c4c4")
        self.txtUser.configure(selectforeground="black")

        self.txtPass = Entry(top)
        self.txtPass.place(relx=0.75, rely=0.76,height=30, relwidth=0.22)
        self.txtPass.configure(background="#c14915")
        self.txtPass.configure(disabledforeground="#a3a3a3")
        self.txtPass.configure(font=font11)
        self.txtPass.configure(foreground="#0b0b1c")
        self.txtPass.configure(highlightbackground="#d9d9d9")
        self.txtPass.configure(highlightcolor="black")
        self.txtPass.configure(insertbackground="#0b0b1c")
        self.txtPass.configure(justify=CENTER)
        self.txtPass.configure(relief=RAISED)
        self.txtPass.configure(selectbackground="#c4c4c4")
        self.txtPass.configure(selectforeground="black")
        self.txtPass.configure(show="*")

        self.txtPriv = Entry(top)
        self.txtPriv.place(relx=0.75, rely=0.85,height=30, relwidth=0.22)
        self.txtPriv.configure(background="#c14915")
        self.txtPriv.configure(disabledforeground="#a3a3a3")
        self.txtPriv.configure(font=font11)
        self.txtPriv.configure(foreground="#0b0b1c")
        self.txtPriv.configure(highlightbackground="#d9d9d9")
        self.txtPriv.configure(highlightcolor="black")
        self.txtPriv.configure(insertbackground="#0b0b1c")
        self.txtPriv.configure(justify=CENTER)
        self.txtPriv.configure(relief=RAISED)
        self.txtPriv.configure(selectbackground="#c4c4c4")
        self.txtPriv.configure(selectforeground="black")

        self.btnAjou = Button(top)
        self.btnAjou.place(relx=0.56, rely=0.93, height=34, width=107)
        self.btnAjou.configure(activebackground="#0b0b1c")
        self.btnAjou.configure(activeforeground="white")
        self.btnAjou.configure(activeforeground="#c14915")
        self.btnAjou.configure(background="#c14915")
        self.btnAjou.configure(cursor="hand2")
        self.btnAjou.configure(disabledforeground="#a3a3a3")
        self.btnAjou.configure(font=font9)
        self.btnAjou.configure(foreground="#0b0b1c")
        self.btnAjou.configure(highlightbackground="#d9d9d9")
        self.btnAjou.configure(highlightcolor="black")
        self.btnAjou.configure(pady="0")
        self.btnAjou.configure(text='''Ajouter''')
        self.btnAjou.configure(width=107)

        self.btnMod = Button(top)
        self.btnMod.place(relx=0.66, rely=0.93, height=34, width=107)
        self.btnMod.configure(activebackground="#0b0b1c")
        self.btnMod.configure(activeforeground="white")
        self.btnMod.configure(activeforeground="#c14915")
        self.btnMod.configure(background="#c14915")
        self.btnMod.configure(cursor="hand2")
        self.btnMod.configure(disabledforeground="#a3a3a3")
        self.btnMod.configure(font=font9)
        self.btnMod.configure(foreground="#0b0b1c")
        self.btnMod.configure(highlightbackground="#d9d9d9")
        self.btnMod.configure(highlightcolor="black")
        self.btnMod.configure(pady="0")
        self.btnMod.configure(text='''Modifier''')
        self.btnMod.configure(width=107)

        self.btnSup = Button(top)
        self.btnSup.place(relx=0.77, rely=0.93, height=34, width=117)
        self.btnSup.configure(activebackground="#0b0b1c")
        self.btnSup.configure(activeforeground="white")
        self.btnSup.configure(activeforeground="#c14915")
        self.btnSup.configure(background="#c14915")
        self.btnSup.configure(cursor="hand2")
        self.btnSup.configure(disabledforeground="#a3a3a3")
        self.btnSup.configure(font=font9)
        self.btnSup.configure(foreground="#0b0b1c")
        self.btnSup.configure(highlightbackground="#d9d9d9")
        self.btnSup.configure(highlightcolor="black")
        self.btnSup.configure(pady="0")
        self.btnSup.configure(text='''Supprimer''')

        self.btnEn = Button(top)
        self.btnEn.place(relx=0.89, rely=0.93, height=34, width=117)
        self.btnEn.configure(activebackground="#0b0b1c")
        self.btnEn.configure(activeforeground="white")
        self.btnEn.configure(activeforeground="#c14915")
        self.btnEn.configure(background="#c14915")
        self.btnEn.configure(cursor="hand2")
        self.btnEn.configure(disabledforeground="#a3a3a3")
        self.btnEn.configure(font=font9)
        self.btnEn.configure(foreground="#0b0b1c")
        self.btnEn.configure(highlightbackground="#d9d9d9")
        self.btnEn.configure(highlightcolor="black")
        self.btnEn.configure(pady="0")
        self.btnEn.configure(text='''Enregistrer''')






if __name__ == '__main__':
    vp_start_gui()



