from tkinter import *
import webbrowser
from functools import partial
import tkinter
from tkinter import messagebox
import PIL
from PIL import Image, ImageSequence
from PIL import Image, ImageTk

def interfaceClient(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.minsize(915,690)
    root.maxsize(915,700)
    class livre :
        def __init__(self,nom,ref,prixD,prixM,quantité,path):
            self.nom=nom
            self.ref=ref
            self.prixD=prixD
            self.prixM=prixM
            self.quantité=quantité
            self.path=path


    stock=[]

    def sauvegarder():
        fic=open("mimo","w")
        fic.seek(0)
        for i in stock:
            fic.write("{}${}${}${}${}${}\n".format(i.nom,i.ref,i.prixD,i.prixM,i.quantité,i.path))
        fic.close()

    def load(la):
        fic = open("mimo", "r")
        fic.seek(0)
        l = fic.readlines()
        fic.close()
        for i in l:
            a = i.split("$")
            la.append(livre(a[0],int(a[1]),float(a[2]),float(a[3]),int(a[4]),a[-1][:-1]))


    def command1():
        global l
        for i in range(0,len(stock)):
            if stock[i].nom == entry[l].get() :
                afficherLivre(i)
                break
        else:
            messagebox.showerror("Oups!", "Ce livre n'éxiste pas")
    def creer(k):
        global l
        if k<len(stock):
            for widget in root.winfo_children():
                widget.destroy()

            for i in range(0, 12, 4):
                for j in range(6):
                    if (k < len(stock)):
                        dessin = Canvas(root, bg='white', height=140, width=150)
                        dessin.grid(row=i, column=j)

                            # Fichier dans le dossier de ce script
                        try:
                            img[k] = PhotoImage(file=stock[k].path)
                            chat = dessin.create_image(150, 150, image=img[k])
                        except:
                            img[k] = PhotoImage(file="erreur.gif")  # Création d'une image Tkinter
                            chat = dessin.create_image(150, 150, image=img[k])
                        lab2 = Label(root, bg="white")
                        lab2.grid(row=i + 1, column=j)
                        l1 = Label(lab2, text=stock[k].nom, bg="white", fg="red", font=("Times New Roman", 7,"bold"))
                        l1.grid(row=i + 2, column=j)
                        l11 = Label(lab2,
                                    text="Prix: " + str(stock[k].prixD) + "dh/jr et " + str(stock[k].prixM) + "dh/mois",
                                    bg="white", fg="black", font=("Times New Roman", 7))

                        l11.grid(row=i + 3, column=j)
                        b1 = Button(lab2, text="Choisir", fg="white", bg="black", width=19, cursor="pencil",
                                    font=("Helvetica Neue", 9, "bold"), command=partial(afficherLivre, k))
                        b1.grid(row=i + 4, column=j)
                        k += 1

            menubar = Menu(root)
            root.config(menu=menubar)
            menufichier = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Quitter", menu=menufichier)

            menufichier.add_command(label="Quitter", command=root.destroy)

            Button(root, width=10, text='<', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="right_ptr",
                   command=partial(gauche, k)).place(relx=0.01, rely=0.955, relwidth=0.047, relheight=0.035)
            Button(root, width=10, text='>', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="plus",
                   command=partial(creer, k)).place(relx=0.95, rely=0.955, relwidth=0.047, relheight=0.035)
            lable = Label(root, text="Recherche rapide :", bg="white", font=("Bookman Old Style", 10, "bold"),
                          anchor="center",
                          fg="#5F9EA0")
            lable.place(relx=0.059, rely=0.955, relwidth=0.2, relheight=0.035)
            root.config(bg="#5F9EA0")
            root.title("catalogue")
            l += 1
            entry[l] = Entry(root)
            bouton = Button(root, text="Chercher", font=("Bookman Old Style", 10, "bold"), cursor="pencil", bg="black",
                            fg="white", command=command1)
            entry[l].insert(0, 'inserer le nom de livre ici .......')
            entry[l].place(relx=0.27, rely=0.955, relwidth=0.5, relheight=0.035)

            bouton.place(relx=0.78, rely=0.955, relwidth=0.16, relheight=0.035)


    def gauche(k):
        if (k>18):
            for widget in root.winfo_children():
                widget.destroy()
            k-=36
            if k<0:
                k=0
            creer(k)

    def afficherLivre(k):

        Height = 600
        Width = 700
        app = Toplevel(root)
        app.resizable(width=False, height=False)

        canvas = Canvas(app, height=Height, width=Width)
        canvas.pack()
        global frame2

        def choisir(k):
            stock[k].quantité -= 1
            if stock[k].quantité <= 0:
                del stock[k]
            lable0 = Label(frame2, text=
                " Le livre vous est maintenant réservé  \n screenez cette page et visitez nous ", bg="white",
                           font=("Courier New", 12, "bold"), anchor="center",
                           fg="#0652DD")
            lable0.place(relx=0, rely=0.7, relwidth=1.01, relheight=0.4)
            sauvegarder()

        back_imag = PhotoImage(file='10.gif')
        back_labe = Label(app, image=back_imag, bg="#5F9EA0")
        back_labe.place(relwidth=1, relheight=1)
        frame = Frame(app, bg="#80c1ff")

        frame.place(rely=0.1, relx=0.20, relwidth=0.35, relheight=0.8, anchor="n")
        for j in range(0, len(stock)):
            try:
                img[j] = PhotoImage(file=stock[j].path)

            except:
                img[j] = PhotoImage(file="erreur.gif")  # Création d'une image Tkinter

        image = img[k]

        imag = Label(frame, image=image)

        imag.place(relwidth=1, relheight=1)

        frame2 = Frame(app, bg='white', bd=10)
        frame2.place(relx=0.7, rely=0.1, relwidth=0.6, relheight=0.8, anchor="n")
        lable = Label(frame2, text="Actuellement disponible", bg='white',
                      font=("Bookman Old Style", 8, "bold", "italic"), anchor="nw",
                      fg="green")
        lable.place(relx=0.31, rely=0.08, relwidth=1, relheight=0.35)

        lable1 = Label(frame2, text=str(stock[k].nom), bg='white', font=("Times New Roman", 20, "bold"),
                       anchor="nw", fg="black")
        lable1.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        lable2 = Label(frame2, text="Profitez de ce livre pour seulement " + str(stock[k].prixD) + " dh/jour et \n " + str(
            stock[k].prixM) + " dh/mois", bg='white', font=("Comic Sans MS", 10, "bold"), anchor="nw", fg="red")
        lable2.place(relx=0, rely=0.2, relwidth=1, relheight=1)

        lable3 = Label(frame2, text="Référence : " + str(stock[k].ref), bg='white', font=("Helvetica", 16, "bold"),
                       anchor="nw", fg="black")
        lable3.place(relx=0, rely=0.35, relwidth=1, relheight=0.35)
        lable4 = Label(frame2, text="Quantité disponible: " + str(stock[k].quantité), bg='white',
                       font=("Helvetica", 16, "bold"), anchor="nw", fg="black")
        lable4.place(relx=0, rely=0.45, relwidth=1, relheight=0.35)
        lable5 = Label(frame2,
                       text="“A reader lives a thousand lives before he dies,\n The man who never reads lives only one.”",
                       bg='white', font=("Bookman Old Style", 9, "bold", "italic"), anchor="nw", fg="#0984e3")
        lable5.place(relx=0, rely=0.7, relwidth=1, relheight=0.5)
        bt1 = Button(frame2, bg='black', fg="white", text="Choisir", font=("Helvetica", 20, "bold"), anchor="center",
                     cursor="pencil",
                     command=partial(choisir, k))
        bt1.place(relx=0, rely=0.9, relwidth=0.5, relheight=0.1)
        bt2 = Button(frame2, bg='black', fg="white", text="Quitter", font=("Helvetica", 20, "bold"), anchor="center",
                     cursor="pencil",
                     command=app.destroy)
        bt2.place(relx=0.51, rely=0.9, relwidth=0.5, relheight=0.1)




    try:
        load(stock)
    except:
        stock=[]
    img=[]
    entry=[]
    for i in range(10000):
        img.append("0")
        entry.append("0")


    print(len(stock))
    k=0
    l=0
    if(k<len(stock)):
        for i in range(0,12,4):
            for j in range(6):
                if (k < len(stock)):
                    dessin = Canvas(root, bg='white', height=140, width=150)
                    dessin.grid(row=i, column=j)

                    try:
                        img[k] = PhotoImage(file=stock[k].path)  # Création d'une image Tkinter
                        chat = dessin.create_image(150, 150, image=img[k])
                    except:
                        img[k] = PhotoImage(file="erreur.gif")  # Création d'une image Tkinter
                        chat = dessin.create_image(150, 150, image=img[k])
                    lab2 = Label(root, bg="white")
                    lab2.grid(row=i + 1, column=j)
                    l1 = Label(lab2, text=stock[k].nom, bg="white", fg="red", font=("Times New Roman", 7,"bold"))
                    l1.grid(row=i + 2, column=j)
                    l11 = Label(lab2,
                                text="Prix: " + str(stock[k].prixD) + "dh/jr et " + str(stock[k].prixM) + "dh/mois",
                                bg="white", fg="black", font=("Times New Roman", 7))

                    l11.grid(row=i + 3, column=j)
                    b1 = Button(lab2, text="Choisir", fg="white", bg="black", width=19, cursor="pencil",
                                font=("Helvetica Neue", 9, "bold"), command=partial(afficherLivre, k))
                    b1.grid(row=i + 4, column=j)
                    k += 1

    menubar = Menu(root)
    root.config(menu=menubar)
    menufichier = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Quitter", menu=menufichier)

    menufichier.add_command(label="Quitter", command=root.destroy)

    Button(root, width=10, text='<', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="right_ptr",
           command=partial(gauche, k)).place(relx=0.01, rely=0.955, relwidth=0.047, relheight=0.035)
    Button(root, width=10, text='>', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="plus",
           command=partial(creer, k)).place(relx=0.95, rely=0.955, relwidth=0.047, relheight=0.035)
    lable = Label(root, text="Recherche rapide :", bg="white", font=("Bookman Old Style", 10, "bold"),
                  anchor="center",
                  fg="#5F9EA0")
    lable.place(relx=0.059, rely=0.955, relwidth=0.2, relheight=0.035)
    root.config(bg="#5F9EA0")
    root.title("catalogue")




    entry[l] = Entry(root)
    bouton = Button(root, text="Chercher", font=("Bookman Old Style", 10, "bold"), cursor="pencil", bg="black",
                    fg="white", command=command1)
    entry[l].insert(0, 'inserer le nom de livre ici .....')
    entry[l].place(relx=0.27, rely=0.955, relwidth=0.5, relheight=0.035)

    bouton.place(relx=0.78, rely=0.955, relwidth=0.16, relheight=0.035)
    sauvegarder()
l=0


def Admin(old):
    old.destroy()
    class livre:
        def __init__(self, nom, ref, prixD, prixM, quantité, path):
            self.nom = nom
            self.ref = ref
            self.prixD = prixD
            self.prixM = prixM
            self.quantité = quantité
            self.path = path

    stock = []

    def sauvegarder():
        fic = open("mimo", "w")
        fic.seek(0)
        for i in stock:
            fic.write("{}${}${}${}${}${}\n".format(i.nom, i.ref, i.prixD, i.prixM, i.quantité, i.path))
        fic.close()

    def load(la):
        fic = open("mimo", "r")
        fic.seek(0)
        l = fic.readlines()
        fic.close()
        for i in l:
            a = i.split("$")
            la.append(livre(a[0], int(a[1]), float(a[2]), float(a[3]), int(a[4]), a[-1][:-1]))

    try:
        load(stock)
    except:
        stock = []

    def ajouterLivre(nom, ref, prixD, prixM, quantité, path):
        flag = True
        for i in stock:
            if i.nom == nom or i.ref == ref:
                flag = False
        if flag:
            l = livre(nom, ref, prixD, prixM, quantité, path)
            stock.append(l)
            sauvegarder()
            messagebox.showinfo("Yes", "Livre ajouté!")
            entrypath.insert(0, 'Exemple: photo1.gif')
            entrynom.delete(0, 'end')
            entryref.delete(0, 'end')
            entryquant.delete(0, 'end')
            entryprixd.delete(0, 'end')
            entryprixm.delete(0, 'end')
        else:
            messagebox.showerror("oups", "Ce livre existe déjà")
            entrypath.insert(0, 'Exemple: photo1.gif')
            entrynom.delete(0, 'end')
            entryref.delete(0, 'end')
            entryquant.delete(0, 'end')
            entryprixd.delete(0, 'end')
            entryprixm.delete(0, 'end')

    def ajouterLivre2(nom, ref, prixD, prixM, quantité, path):
        flag = True
        for i in stock:
            if i.nom == nom or i.ref == ref:
                flag = False
        if flag:
            l = livre(nom, ref, prixD, prixM, quantité, path)
            stock.append(l)
        else:
            print("ce livre existe déja essayer de modifier sa quantité ou son prix si vous voulez")

    print(stock)

    def image_size(a, b, c):
        size = (a, b)

        im = Image.open(c)
        frames = ImageSequence.Iterator(im)

        def thumbnails(frames):
            for frame in frames:
                thumbnail = frame.copy()
                thumbnail.thumbnail(size, Image.ANTIALIAS)
                yield thumbnail

        frames = thumbnails(frames)

        om = next(frames)  # Handle first frame separately
        om.info = im.info  # Copy sequence info
        om.save("out2.gif", save_all=True, append_images=list(frames))

    # -------------------------------------------------------------------------------#

    def login_command():
        if ((username_entry.get() == "iagi") and (password_entry.get() == "123")):
            main.deiconify()
            login.destroy()

    # main control
    def command_annuler1():
        label_recherche_par_ref.place_forget()
        entry1_recherche_par_ref.place_forget()
        boutton_recherche_par_ref.place_forget()
        boutton_recherche_par_ref2.place_forget()

        boutton1.place(relx=0.11, rely=0.07)
        boutton2.place(relx=0.11, rely=0.21)
        boutton3.place(relx=0.11, rely=0.35)
        boutton4.place(relx=0.11, rely=0.50)
        boutton5.place(relx=0.11, rely=0.64)
        boutton6.place(relx=0.11, rely=0.78)
        boutton7.place(relx=0.4, rely=0.91)

    def command_recherche():
        # if (boutton5.winfo_ismapped() and boutton4.winfo_ismapped() and boutton3.winfo_ismapped() and boutton2.winfo_ismapped() and boutton6.winfo_ismapped()):
        if (
                boutton_ajouter_annuler.winfo_ismapped() or boutton_supprimer_annuler.winfo_ismapped() or boutton_modificationQantite_annuler.winfo_ismapped() or boutton_modificationPrix_annuler.winfo_ismapped()):
            messagebox.showerror("erreur", "Terminer l'opération en cours")


        else:
            def rechercherLivre(arg):
                def command_retour1():
                    label_recherche_par_ref2.place_forget()
                    label_recherche_par_ref3.place_forget()
                    boutton_recherche_par_ref3_retour.place_forget()
                    boutton1.place(relx=0.11, rely=0.07)
                    boutton2.place(relx=0.11, rely=0.21)
                    boutton3.place(relx=0.11, rely=0.35)
                    boutton4.place(relx=0.11, rely=0.50)
                    boutton5.place(relx=0.11, rely=0.64)
                    boutton6.place(relx=0.11, rely=0.78)
                    boutton7.place(relx=0.4, rely=0.91)

                for i in stock:
                    if i.nom == arg or i.ref == arg:
                        label_recherche_par_ref.place_forget()
                        entry1_recherche_par_ref.place_forget()
                        boutton_recherche_par_ref.place_forget()
                        boutton_recherche_par_ref2.place_forget()
                        label_recherche_par_ref2 = tkinter.Label(main,
                                                                 text='{} exemplaires sont disponibles \n pour un prix de {} MAD / mois \n et {} MAD / jour'.format(
                                                                     i.quantité, i.prixM, i.prixD),
                                                                 font=("Bookman Old Style", 12, "italic"),
                                                                 fg="#011826", bg="cornsilk4", width=39, height=6)
                        boutton_recherche_par_ref3_retour = tkinter.Button(main, text="Retour", height=1, width=10,
                                                                           bg="bisque4", fg="black",
                                                                           font=(
                                                                           "Bookman Old Style", 11, "bold", "italic"),
                                                                           command=command_retour1)
                        label_recherche_par_ref3 = tkinter.Label(main,
                                                                 text=" “Think before you speak. Read before you think.”\n – Fran Lebowitz",
                                                                 font=("Bookman Old Style", 10, "italic"),
                                                                 fg="#011826", bg="cornsilk4", width=48, height=2)
                        label_recherche_par_ref2.place(relx=0.2, rely=0.08)
                        label_recherche_par_ref3.place(relx=0.205, rely=0.35)
                        boutton_recherche_par_ref3_retour.place(relx=0.585, rely=0.45)
                        break
                else:
                    messagebox.showerror("oups!", "Ce livre n'éxiste pas")

            if boutton1.winfo_ismapped():
                boutton1.place_forget()
                label_recherche_par_ref.place(relx=0.11, rely=0.07)
                entry1_recherche_par_ref.place(relx=0.11, rely=0.14)
                boutton_recherche_par_ref.place(relx=0.38, rely=0.132)
                boutton_recherche_par_ref2.place(relx=0.52, rely=0.132)
                entry1_recherche_par_ref.delete(0, 'end')
                boutton2.place_forget()
                boutton3.place_forget()
                boutton4.place_forget()
                boutton5.place_forget()
                boutton6.place_forget()


            elif boutton_recherche_par_ref.winfo_ismapped():
                rechercherLivre(entry1_recherche_par_ref.get())
                entry1_recherche_par_ref.delete(0, 'end')

            else:
                label_recherche_par_ref.place_forget()
                entry1_recherche_par_ref.place_forget()
                boutton_recherche_par_ref.place_forget()
                boutton_recherche_par_ref2.place_forget()
                entry1_recherche_par_ref.delete(0, 'end')
                boutton1.place(relx=0.11, rely=0.07)
                boutton2.place(relx=0.11, rely=0.21)
                boutton3.place(relx=0.11, rely=0.35)
                boutton4.place(relx=0.11, rely=0.50)
                boutton5.place(relx=0.11, rely=0.64)
                boutton6.place(relx=0.11, rely=0.78)
                boutton7.place(relx=0.4, rely=0.91)

    def command_annuler2():
        boutton1.place(relx=0.11, rely=0.07)
        boutton2.place(relx=0.11, rely=0.21)
        boutton3.place(relx=0.11, rely=0.35)
        boutton4.place(relx=0.11, rely=0.50)
        boutton5.place(relx=0.11, rely=0.64)
        boutton6.place(relx=0.11, rely=0.78)
        boutton7.place(relx=0.4, rely=0.91)
        label_modificationPrix.place_forget()
        entry1_modificationPrix.place_forget()
        entry1_modificationPrix2.place_forget()
        boutton1_modificationPrix.place_forget()
        boutton_modificationPrix_annuler.place_forget()
        boutton1_modificationPrix.config(command=command_modification_de_prix)

    def command_modification_de_prix():
        def on_entry_click1(event):
            if entry1_modificationPrix.get() == 'Prix de location par jour':
                entry1_modificationPrix.delete(0, "end")  # delete all the text in the entry
                entry1_modificationPrix.insert(0, '')  # Insert blank for user input
                entry1_modificationPrix.config(fg='black')

        def on_entry_click2(event):
            if entry1_modificationPrix2.get() == 'Prix de location par mois':
                entry1_modificationPrix2.delete(0, "end")  # delete all the text in the entry
                entry1_modificationPrix2.insert(0, '')  # Insert blank for user input
                entry1_modificationPrix2.config(fg='black')

        def on_focusout1(event):
            if entry1_modificationPrix.get() == '':
                entry1_modificationPrix.insert(0, 'Prix de location par jour')
                entry1_modificationPrix.config(fg='black')

        def on_focusout2(event):
            if entry1_modificationPrix2.get() == '':
                entry1_modificationPrix2.insert(0, 'Prix de location par mois')
                entry1_modificationPrix2.config(fg='black')

        def command_modification_de_prix2():
            d = entry1_modificationPrix.get()
            b = entry1_modificationPrix2.get()

            try:
                d = float(d)
                b = float(b)
            except:
                messagebox.showerror("oups", "Prix invalide")
                entry1_modificationPrix.delete(0, 'end')
                entry1_modificationPrix2.delete(0, 'end')
            else:
                i.prixD = d
                i.prixM = b
                sauvegarder()
                label_modificationPrix.config(text="Modifiation reussie!")
                boutton1_modificationPrix.place_forget()
                boutton_modificationPrix_annuler.config(text="retour")
                boutton1_modificationPrix.config(text="Chercher")
                boutton1_modificationPrix.config(command=command_modification_de_prix)
                entry1_modificationPrix.place_forget()
                entry1_modificationPrix2.place_forget()

        if boutton2.winfo_ismapped():
            entry1_modificationPrix.delete(0, 'end')
            entry1_modificationPrix2.delete(0, 'end')
            boutton2.place_forget()
            boutton1.place_forget()
            boutton3.place_forget()
            boutton4.place_forget()
            boutton5.place_forget()
            boutton6.place_forget()
            label_modificationPrix.config(text="Entrez le nom ou la réfèrence du livre")
            label_modificationPrix.place(relx=0.11, rely=0.07)
            entry1_modificationPrix.place(relx=0.11, rely=0.14)
            boutton1_modificationPrix.place(relx=0.38, rely=0.132)
            boutton_modificationPrix_annuler.place(relx=0.52, rely=0.132)


        else:

            for i in stock:
                if i.nom == entry1_modificationPrix.get() or i.ref == entry1_modificationPrix.get():
                    label_modificationPrix.config(text="Entrez les nouveaux prix")
                    boutton1_modificationPrix.config(text="Modifier")
                    boutton1_modificationPrix.place(relx=0.38, rely=0.15)
                    boutton_modificationPrix_annuler.place(relx=0.52, rely=0.15)
                    entry1_modificationPrix2.place(relx=0.11, rely=0.2)
                    boutton1_modificationPrix.config(command=command_modification_de_prix2)
                    entry1_modificationPrix.bind('<FocusIn>', on_entry_click1)
                    entry1_modificationPrix2.bind('<FocusIn>', on_entry_click2)
                    entry1_modificationPrix.bind('<FocusOut>', on_focusout1)
                    entry1_modificationPrix2.bind('<FocusOut>', on_focusout2)
                    entry1_modificationPrix.delete(0, 'end')
                    entry1_modificationPrix2.delete(0, 'end')
                    entry1_modificationPrix.insert(0, 'Prix de location par jour')
                    entry1_modificationPrix2.insert(0, 'Prix de location par mois')

                    break

            else:
                messagebox.showerror("oups", "Ce livre n'éxiste pas")
                entry1_modificationPrix.delete(0, 'end')
                entry1_modificationPrix2.delete(0, 'end')

    def command_annuler3():
        boutton1.place(relx=0.11, rely=0.07)
        boutton2.place(relx=0.11, rely=0.21)
        boutton3.place(relx=0.11, rely=0.35)
        boutton4.place(relx=0.11, rely=0.50)
        boutton5.place(relx=0.11, rely=0.64)
        boutton6.place(relx=0.11, rely=0.78)
        boutton7.place(relx=0.4, rely=0.91)
        label_modificationQantite.place_forget()
        entry1_modificationQantite.place_forget()
        boutton1_modificationQantite.place_forget()
        boutton_modificationQantite_annuler.place_forget()
        boutton1_modificationQantite.config(command=command_modification_de_qantite)

    def command_modification_de_qantite():
        def command_modification_de_qantite2():
            boutton1_modificationQantite.config(command=command_modification_de_qantite)
            e = entry1_modificationQantite.get()
            try:
                i.quantité = int(e)
            except:
                messagebox.showerror("oups", "Quantité invalide")
                entry1_modificationQantite.delete(0, 'end')
            else:
                sauvegarder()
                label_modificationQantite.config(text="Modifiation reussie!")
                boutton1_modificationQantite.place_forget()
                boutton_modificationQantite_annuler.config(text="retour")
                boutton1_modificationQantite.config(text="Chercher")
                boutton1_modificationQantite.config(command=command_modification_de_qantite)
                entry1_modificationQantite.place_forget()

        if boutton3.winfo_ismapped():
            entry1_modificationQantite.delete(0, 'end')
            boutton3.place_forget()
            boutton1.place_forget()
            boutton2.place_forget()
            boutton4.place_forget()
            boutton5.place_forget()
            boutton6.place_forget()
            label_modificationQantite.config(text="Entrez le nom ou la réfèrence du livre")
            label_modificationQantite.place(relx=0.11, rely=0.07)
            entry1_modificationQantite.place(relx=0.11, rely=0.14)
            boutton1_modificationQantite.place(relx=0.38, rely=0.132)
            boutton_modificationQantite_annuler.place(relx=0.52, rely=0.132)


        else:

            for i in stock:
                if i.nom == entry1_modificationQantite.get() or i.ref == entry1_modificationQantite.get():
                    label_modificationQantite.config(text="Entrez la nouvelle qantité")
                    boutton1_modificationQantite.config(text="Modifier")
                    boutton1_modificationQantite.config(command=command_modification_de_qantite2)
                    entry1_modificationQantite.delete(0, 'end')
                    break

            else:
                messagebox.showerror("oups", "Ce livre n'éxiste pas")
                entry1_modificationQantite.delete(0, 'end')

    def command_annuler4():
        label_supprimer.place_forget()
        entry1_supprimer.place_forget()
        boutton_supprimer.place_forget()
        boutton_supprimer_annuler.place_forget()
        boutton1.place(relx=0.11, rely=0.07)
        boutton2.place(relx=0.11, rely=0.21)
        boutton3.place(relx=0.11, rely=0.35)
        boutton4.place(relx=0.11, rely=0.50)
        boutton5.place(relx=0.11, rely=0.64)
        boutton6.place(relx=0.11, rely=0.78)

    def command_supprimer():
        def command_supprimer2():
            reponse = messagebox.askokcancel("Confirmation", "Etes-vous sûr de vouloir supprimer ce livre?")
            if reponse:
                del stock[i]
                sauvegarder()
                label_supprimer.config(text="Suppression réussie")
                boutton_supprimer_annuler.config(text="retour")
                boutton_supprimer.place_forget()
                boutton_supprimer.config(command=command_supprimer)
                entry1_supprimer.place_forget()
            else:
                boutton_supprimer.config(command=command_supprimer)
                entry1_supprimer.place_forget()
                boutton_supprimer.place_forget()
                boutton_supprimer_annuler.place_forget()
                label_supprimer.place_forget()
                boutton1.place(relx=0.11, rely=0.07)
                boutton2.place(relx=0.11, rely=0.21)
                boutton3.place(relx=0.11, rely=0.35)
                boutton4.place(relx=0.11, rely=0.50)
                boutton5.place(relx=0.11, rely=0.64)
                boutton6.place(relx=0.11, rely=0.78)

        if boutton4.winfo_ismapped():
            entry1_supprimer.delete(0, 'end')
            boutton5.place_forget()
            boutton4.place_forget()
            boutton3.place_forget()
            boutton2.place_forget()
            boutton1.place_forget()
            boutton6.place_forget()
            label_supprimer.config(text="Entrez le nom ou la réfèrence du livre")
            label_supprimer.place(relx=0.11, rely=0.07)
            entry1_supprimer.place(relx=0.11, rely=0.14)
            boutton_supprimer.place(relx=0.38, rely=0.132)
            boutton_supprimer_annuler.place(relx=0.52, rely=0.132)
        else:
            for i in range(0, len(stock)):
                if stock[i].nom == entry1_supprimer.get() or stock[i].ref == entry1_supprimer.get():
                    command_supprimer2()
                    break
            else:
                messagebox.showerror("oups", "Ce livre n'éxiste pas")
                entry1_supprimer.delete(0, 'end')

    def command_annuler5():
        labelnom.place_forget()
        entrynom.place_forget()
        labelref.place_forget()
        entryref.place_forget()
        labelprixd.place_forget()
        labelprixm.place_forget()
        entryprixd.place_forget()
        entryprixm.place_forget()
        labelquant.place_forget()
        entryquant.place_forget()
        labelpath.place_forget()
        entrypath.place_forget()
        boutton_ajouter.place_forget()
        boutton_ajouter_annuler.place_forget()
        boutton1.place(relx=0.11, rely=0.07)
        boutton2.place(relx=0.11, rely=0.21)
        boutton3.place(relx=0.11, rely=0.35)
        boutton4.place(relx=0.11, rely=0.50)
        boutton5.place(relx=0.11, rely=0.64)
        boutton6.place(relx=0.11, rely=0.78)

    def command_ajouter():
        def on_entry_click(event):
            if entrypath.get() == 'Exemple: photo1.gif':
                entrypath.delete(0, "end")  # delete all the text in the entry
                entrypath.insert(0, '')  # Insert blank for user input
                entrypath.config(fg='black')

        def on_focusout(event):
            if entrypath.get() == '':
                entrypath.insert(0, 'Exemple: photo1.gif')
                entrypath.config(fg='black')

        if boutton5.winfo_ismapped():
            entrypath.delete(0, 'end')
            entrypath.insert(0, 'Exemple: photo1.gif')
            entrynom.delete(0, 'end')
            entryref.delete(0, 'end')
            entryquant.delete(0, 'end')
            entryprixd.delete(0, 'end')
            entryprixm.delete(0, 'end')
            boutton5.place_forget()
            boutton2.place_forget()
            boutton3.place_forget()
            boutton4.place_forget()
            boutton1.place_forget()
            boutton6.place_forget()
            labelnom.place(relx=0.11, rely=0.07)
            entrynom.place(relx=0.30, rely=0.07)
            labelref.place(relx=0.11, rely=0.17)
            entryref.place(relx=0.30, rely=0.17)
            labelprixd.place(relx=0.11, rely=0.27)
            entryprixd.place(relx=0.30, rely=0.27)
            labelprixm.place(relx=0.11, rely=0.37)
            entryprixm.place(relx=0.30, rely=0.37)
            labelquant.place(relx=0.11, rely=0.47)
            entryquant.place(relx=0.30, rely=0.47)
            labelpath.place(relx=0.11, rely=0.57)
            entrypath.place(relx=0.30, rely=0.57)
            boutton_ajouter.place(rely=0.71, relx=0.2)
            boutton_ajouter_annuler.place(rely=0.71, relx=0.35)
            entrypath.bind('<FocusIn>', on_entry_click)
            entrypath.bind('<FocusOut>', on_focusout)
            entrypath.config(fg='black')
        else:
            try:
                int(entryquant.get())
                float(entryprixd.get())
                float(entryprixm.get())
            except:
                messagebox.showerror("oups", "Valeur(s) invalide(s)")
            else:
                ajouterLivre(entrynom.get(), entryref.get(), entryprixd.get(), entryprixm.get(), entryquant.get(),
                             entrypath.get())
                command_annuler5()

    def command_cata():
        root.deiconify()
        main.withdraw()

    def quit():
        main.destroy()

    main = tkinter.Tk()
    main.title("Library")
    main.config(bg='cornsilk4')
    main.minsize(640, 500)
    main.resizable(width=False, height=False)
    image_size(640,500,"back.gif") #fonction de modification de la taille d'image
    background_image=tkinter.PhotoImage(file="out2.gif")
    background_label = tkinter.Label(main, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    boutton1 = tkinter.Button(main, text="Rechercher un livre dans le stock", height=2, width=35, bg="#593622",
                              fg="#011826", font=("Bookman Old Style", 11, "bold", "italic"), command=command_recherche)
    label_recherche_par_ref = tkinter.Label(main, text="Entrez la réfèrence ou le nom du livre:", fg="#011826",
                                            font=("Bookman Old Style", 10, "bold", "italic"), width=37, height=1,
                                            bg="cornsilk4")
    entry1_recherche_par_ref = tkinter.Entry(main, width=25, bg="bisque4")
    boutton_recherche_par_ref = tkinter.Button(main, text="Chercher", height=1, width=8, bg="bisque4", fg="black",
                                               font=("Bookman Old Style", 9, "bold", "italic"),
                                               command=command_recherche)
    boutton_recherche_par_ref2 = tkinter.Button(main, text="Annuler", height=1, width=8, bg="bisque4", fg="black",
                                                font=("Bookman Old Style", 9, "bold", "italic"),
                                                command=command_annuler1)
    boutton2 = tkinter.Button(main, text="Modifier le prix d'un livre", height=2, width=35, bg="#593622", fg="#011826",
                              font=("Bookman Old Style", 11, "bold", "italic"), command=command_modification_de_prix)
    label_modificationPrix = tkinter.Label(main, text="Entrez la nom ou la réfèrence du livre:", fg="#011826",
                                           font=("Bookman Old Style", 10, "bold", "italic"), width=37, height=1,
                                           bg="cornsilk4")
    entry1_modificationPrix = tkinter.Entry(main, width=25, bg="bisque4")
    entry1_modificationPrix2 = tkinter.Entry(main, width=25, bg="bisque4")
    boutton1_modificationPrix = tkinter.Button(main, text="Chercher", height=1, width=8, bg="bisque4", fg="black",
                                               font=("Bookman Old Style", 9, "bold", "italic"),
                                               command=command_modification_de_prix)
    boutton_modificationPrix_annuler = tkinter.Button(main, text="Annuler", height=1, width=8, bg="bisque4", fg="black",
                                                      font=("Bookman Old Style", 9, "bold", "italic"),
                                                      command=command_annuler2)
    boutton3 = tkinter.Button(main, text="Modifier la quantité d'un livre", height=2, width=35, bg="#593622",
                              fg="#011826", font=("Bookman Old Style", 11, "bold", "italic"),
                              command=command_modification_de_qantite)
    label_modificationQantite = tkinter.Label(main, text="Entrez la nom ou la réfèrence du livre:", fg="#011826",
                                              font=("Bookman Old Style", 10, "bold", "italic"), width=37, height=1,
                                              bg="cornsilk4")
    entry1_modificationQantite = tkinter.Entry(main, width=25, bg="bisque4")
    boutton1_modificationQantite = tkinter.Button(main, text="Chercher", height=1, width=8, bg="bisque4", fg="black",
                                                  font=("Bookman Old Style", 9, "bold", "italic"),
                                                  command=command_modification_de_qantite)
    boutton_modificationQantite_annuler = tkinter.Button(main, text="Annuler", height=1, width=8, bg="bisque4",
                                                         fg="black", font=("Bookman Old Style", 9, "bold", "italic"),
                                                         command=command_annuler3)
    boutton4 = tkinter.Button(main, text="Supprimer un livre du stock", height=2, width=35, bg="#593622", fg="#011826",
                              font=("Bookman Old Style", 11, "bold", "italic"), command=command_supprimer)
    label_supprimer = tkinter.Label(main, text="Entrer la nom ou la réfèrence du livre à supprimer:", fg="#011826",
                                    font=("Bookman Old Style", 10, "bold", "italic"), width=37, height=1,
                                    bg="cornsilk4")
    entry1_supprimer = tkinter.Entry(main, width=25, bg="bisque4")
    boutton_supprimer = tkinter.Button(main, text="Supprimer", height=1, width=8, bg="bisque4", fg="black",
                                       font=("Bookman Old Style", 9, "bold", "italic"), command=command_supprimer)
    boutton_supprimer_annuler = tkinter.Button(main, text="Annuler", height=1, width=8, bg="bisque4", fg="black",
                                               font=("Bookman Old Style", 9, "bold", "italic"),
                                               command=command_annuler4)
    boutton5 = tkinter.Button(main, text="Ajouter un livre au stock", height=2, width=35, bg="#593622", fg="#011826",
                              font=("Bookman Old Style", 11, "bold", "italic"), command=command_ajouter)
    labelnom = tkinter.Label(main, text="Le nom :", fg="#011826", font=("Bookman Old Style", 10, "bold", "italic"),
                             width=12, height=1, bg="cornsilk4", anchor="e")
    entrynom = tkinter.Entry(main, width=25, bg="bisque4")
    labelref = tkinter.Label(main, text="La référence :", fg="#011826",
                             font=("Bookman Old Style", 10, "bold", "italic"), width=12, height=1, bg="cornsilk4")
    entryref = tkinter.Entry(main, width=25, bg="bisque4")
    labelprixd = tkinter.Label(main, text="Le prix / jour :", fg="#011826",
                               font=("Bookman Old Style", 10, "bold", "italic"), width=12, height=1, bg="cornsilk4",
                               anchor="e")
    entryprixd = tkinter.Entry(main, width=25, bg="bisque4")
    labelquant = tkinter.Label(main, text="La quantité :", fg="#011826",
                               font=("Bookman Old Style", 10, "bold", "italic"), width=12, height=1, bg="cornsilk4",
                               anchor="e")
    entryquant = tkinter.Entry(main, width=25, bg="bisque4")
    labelpath = tkinter.Label(main, text="L'image :", fg="#011826", font=("Bookman Old Style", 10, "bold", "italic"),
                              width=12, height=1, bg="cornsilk4", anchor="e")
    entrypath = tkinter.Entry(main, width=25, bg="bisque4")
    labelprixm = tkinter.Label(main, text="Le prix / mois :", fg="#011826",
                               font=("Bookman Old Style", 10, "bold", "italic"), width=12, height=1, bg="cornsilk4",
                               anchor="e")
    entryprixm = tkinter.Entry(main, width=25, bg="bisque4")
    boutton_ajouter = tkinter.Button(main, text="Ajouter", height=1, width=8, bg="bisque4", fg="black",
                                     font=("Bookman Old Style", 9, "bold", "italic"), command=command_ajouter)
    boutton_ajouter_annuler = tkinter.Button(main, text="Annuler", height=1, width=8, bg="bisque4", fg="black",
                                             font=("Bookman Old Style", 9, "bold", "italic"), command=command_annuler5)
    boutton6 = tkinter.Button(main, text="Consulter le stock des livres", height=2, width=35, bg="#593622",
                              fg="#011826", font=("Bookman Old Style", 11, "bold", "italic"), command=command_cata)
    boutton7 = tkinter.Button(main, text="Quitter", height=1, width=10, bg="bisque4", fg="black",
                              font=("Bookman Old Style", 11, "bold", "italic"), command=quit)
    boutton1.place(relx=0.11, rely=0.07)
    boutton2.place(relx=0.11, rely=0.21)
    boutton3.place(relx=0.11, rely=0.35)
    boutton4.place(relx=0.11, rely=0.50)
    boutton5.place(relx=0.11, rely=0.64)
    boutton6.place(relx=0.11, rely=0.78)
    boutton7.place(relx=0.4, rely=0.91)

    # login interface control

    login = tkinter.Toplevel(main)
    login.title("Login")
    login.config(bg="royalblue4")
    login.minsize(400, 360)
    login.resizable(width=False, height=False)
    frame1 = tkinter.Frame(login, bg="black")
    username_lbl = tkinter.Label(login, text="Username", font=("Bookman Old Style", 11, "italic"), bg='LightSkyBlue4')
    username_entry = tkinter.Entry(login)
    password_lbl = tkinter.Label(login, text="password", font=("Bookman Old Style", 11, "italic"), bg='LightSkyBlue4')
    password_entry = tkinter.Entry(login, show="*")
    cancel_but = tkinter.Button(login, text="Cancel", bg="LightSkyBlue4", font=("times", 10, "italic"),
                                command=login.quit)
    go_but = tkinter.Button(login, text="Login", bg="LightSkyBlue4", font=("times", 10, "italic"),
                            command=login_command)
    image_size(150,250,"9fel.gif") #fonction de modification de la taille de l'image
    photo=tkinter.PhotoImage(file="out2.gif")
    photolabel=tkinter.Label(frame1,image=photo,bg='royalblue4')
    photolabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    frame1.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.3)

    username_lbl.place(relx=0.4, rely=0.44)
    username_entry.place(relx=0.34, rely=0.54)
    password_lbl.place(relx=0.4, rely=0.64)
    password_entry.place(relx=0.34, rely=0.74)
    cancel_but.place(relx=0.325, rely=0.83)
    go_but.place(relx=0.56, rely=0.83)

    # catalogue interface control
    root = Toplevel(main)

    root.minsize(950, 650)
    root.resizable(width=False, height=False)

    def command1():
        root.withdraw()
        main.deiconify()

    def creer(k):
        global l
        if k < len(stock):
            for widget in root.winfo_children():
                widget.destroy()

            for i in range(0, 12, 4):
                for j in range(6):
                    if (k < len(stock)):
                        dessin = Canvas(root, bg='white', height=140, width=150)
                        dessin.grid(row=i, column=j)

                        # Fichier dans le dossier de ce script
                        try:
                            img[k] = PhotoImage(file=stock[k].path)
                            chat = dessin.create_image(150, 150, image=img[k])
                        except:
                            img[k] = PhotoImage(file="erreur.gif")  # Création d'une image Tkinter
                            chat = dessin.create_image(150, 150, image=img[k])
                        lab2 = Label(root, bg="white")
                        lab2.grid(row=i + 1, column=j)
                        l1 = Label(lab2, text=stock[k].nom, bg="white", fg="black", font=("Times New Roman", 7))
                        l1.grid(row=i + 2, column=j)
                        l11 = Label(lab2,
                                    text="PRIX: " + str(stock[k].prixD) + "dh/jr et " + str(stock[k].prixM) + "dh/mois",
                                    bg="white", fg="black", width=28, font=("Times New Roman", 7))

                        l11.grid(row=i + 3, column=j)
                        k += 1
            Button(root, width=10, text='<', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="right_ptr",
                   command=partial(gauche, k)).place(relx=0.01, rely=0.955, relwidth=0.047, relheight=0.035)
            Button(root, width=10, text='>', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="plus",
                   command=partial(creer, k)).place(relx=0.95, rely=0.955, relwidth=0.047, relheight=0.035)
            bouton = Button(root, text="Retour", font=("Bookman Old Style", 10, "bold"), bg="bisque4", fg="black",
                            command=command1)
            bouton.place(relx=0.78, rely=0.955, relwidth=0.16, relheight=0.035)

    def gauche(k):
        if (k > 18):
            for widget in root.winfo_children():
                widget.destroy()
            k -= 36
            if k < 0:
                k = 0
            creer(k)

    img = []
    entry = []
    for i in range(10000):
        img.append("0")
        entry.append("0")

    print(len(stock))
    k = 0
    l = 0
    if (k < len(stock)):
        for i in range(0, 12, 4):
            for j in range(6):
                if (k < len(stock)):
                    dessin = Canvas(root, bg='white', height=140, width=150)
                    dessin.grid(row=i, column=j)

                    try:
                        img[k] = PhotoImage(file=stock[k].path)  # Création d'une image Tkinter
                        chat = dessin.create_image(150, 150, image=img[k])
                    except:
                        img[k] = PhotoImage(file="erreur.gif")  # Création d'une image Tkinter
                        chat = dessin.create_image(150, 150, image=img[k])
                    lab2 = Label(root, bg="white")
                    lab2.grid(row=i + 1, column=j)
                    l1 = Label(lab2, text=stock[k].nom, bg="white", fg="black", font=("Times New Roman", 7))
                    l1.grid(row=i + 2, column=j)
                    l11 = Label(lab2,
                                text="PRIX: " + str(stock[k].prixD) + "dh/jr et " + str(stock[k].prixM) + "dh/mois",
                                width=28,
                                bg="white", fg="black", font=("Times New Roman", 7))

                    l11.grid(row=i + 3, column=j)

                    k += 1

    Button(root, width=10, text='<', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="right_ptr",
           command=partial(gauche, k)).place(relx=0.01, rely=0.955, relwidth=0.047, relheight=0.035)
    Button(root, width=10, text='>', bg='#34ace0', fg='white', font=("arial", 10, "bold"), cursor="plus",
           command=partial(creer, k)).place(relx=0.95, rely=0.955, relwidth=0.047, relheight=0.035)
    root.title("catalogue")
    bouton = Button(root, text="Retour", font=("Bookman Old Style", 10, "bold"), cursor="pencil", bg="bisque4",
                    fg="black", command=command1)
    bouton.place(relx=0.78, rely=0.955, relwidth=0.16, relheight=0.035)

    root.withdraw()

    main.withdraw()
    main.iconbitmap("icon2.ico")
    main.mainloop()


def open_() :
    webbrowser.open_new("http://ensam-casa.ma/")
Height=600
Width=700
root=Tk()
root.resizable(width=False,height=False)
canvas=Canvas(root,height=Height,width=Width)
canvas.pack()
back_imag=PhotoImage(file='yarebitkhdem.gif')
back_labe=Label(root,image=back_imag,bg="#5F9EA0")
back_labe.place(relwidth=1,relheight=1)

frame=Frame(root,bg="#80c1ff")
frame.place(rely=0.1,relx=0.5,relwidth=0.8,relheight=0.1,anchor="n")

lable=Label(frame,text=" ENSAM BIBLIOTHEQUE",bg="black",fg="white",font=("Helvetica",20,"bold","italic"),anchor="center")
lable.place(relwidth=0.8,relheight=1)
botton=Button(frame,text="CONTACTER NOUS",bg="#5F9EA0",fg="white",font=("Helvetica",8,"bold"),anchor="center",command=open_)
botton.place(relx=0.8,relwidth=0.2,relheight=1)

frame2=Frame(root,bg='black',bd=10)
frame2.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor="n")
back_ima=PhotoImage(file='9.gif')
back_lab=Label(frame2,image=back_ima)
back_lab.place(relwidth=1,relheight=1)
lable2=Label(frame2,text="Vous êtes : ",bg='black',font=("Bookman Old Style",25,"bold","italic"),anchor="center",fg="white")
lable2.place(relx=0,rely=0,relwidth=1,relheight=0.25)
able=Label(frame2,bg='black')


button1=Button(frame2,text="Admin",bg='black',fg="white",font=("Bookman Old Style",20,"bold","italic"),anchor="center",command=partial(Admin,root))
button1.place(relx=0.01,rely=0.4,relwidth=0.98,relheight=0.1)

button2=Button(frame2,bg='black',fg="white",text="Client",font=("Bookman Old Style",20,"bold","italic"),anchor="center" ,command=partial(interfaceClient,root))
button2.place(relx=0.01,rely=0.6,relwidth=0.98,relheight=0.1)

lab=Label(root,text="Tous les droits sont réservés © ",bg="#5F9EA0",fg="white",font=("Helvetica Neue",11,"bold"))
root.title("accueil")
lab.pack()

root.iconbitmap("icon2.ico")
root.mainloop()