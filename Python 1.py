##
##import os
##L=[]
##
##
##
##if os.path.exists("os.txt"):
##    with open("os.txt", "r", encoding="utf-8") as f:
##        next (f)
##        for line in f:
##            x, y = line.strip().split(",")
##            L.append([x,y])
##            
##
##
##print("Witaj w bazie danych telefnicznych, dostępne komendy to: dodaj, edytuj, usun, ilosc, szukaj, wyswietl, koniec, help")
##
##while True:
##    a=input("Co chcesz zrobic? ").lower()
##    if a==("dodaj"):
##        x=input("Podaj imie: ")
##        y=input("Podaj numer: ")
##        L.append([x,y])
##        
##        print("Dodano ",x," z numerem ",y)
##    elif a==("help"):
##        print("Dostepne komendy to: dodaj, edytuj, usun, ilosc, szukaj, wyswietl, koniec, help")
##    
##    elif a==("edytuj"):
##        b=input("Podaj imie: ")
##        for i in range(len(L)):
##            if L[i][0]==b:
##                x=input("Podaj zmienione imie: ")
##                y=input("Podaj zmieniony numer: ")
##                L[i][0]= x
##                L[i][1]= y
##        
##                print("Zmieniono na ",x," z numerem ",y)
##                break
##        else:
##            print("Kontakt nie isnieje")
##
##        
##
##    elif a == ("ilosc"):
##        print("masz ",len(L)," zapisane numery")
##        
##    elif a==("szukaj"):
##        n=0
##        b=input("Podaj imie: ")
##        for i in range(len(L)):
##            if b.lower() in L[i][0].lower():
##                print("Na pozycji: ",i+1, " ",L[i][0], "-", L[i][1])
##        for i in range(len(L)):
##            if b.lower() not in L[i][0].lower():
##                n+=1
##        if n==len(L):
##            print("Kontakt nie isnieje")
##        n=0
##        
##    elif a==("wyswietl"):
##        if L:
##            for i in range(len(L)):
##                print(i+1," ",L[i][0], "-", L[i][1])
##                
##                
##        else:
##            print("Lista kotaktów pusta")
##            
##    elif a==("usun"):
##        b = input("Podaj imię do usunięcia: ")
##        for i in range(len(L)):
##            if L[i][0]==b:
##                print("Czy napewno chcesz usunąć kontakt: ",L[i][0], "-", L[i][1])
##                u=input("Podaj: y/n ...")
##                if u=="y":
##                  del L[i]
##                  print("Usunięto kontakt ",b)
##                  break
##                elif u=="n":
##                    print("ok, nie usuwam")
##                    break
##                else:
##                    print("miałes jedno zadanie")
##                    break
##        else:
##            print("Kontakt nie istnieje")
##    elif a==("czysc"):
##        k=input("Czy chcesz wyczyscic kontakty? Podaj y/n:..")
##        if k==("y"):
##            for i in L:
##                L.clear()
##                print("Wyczyszczono wszystkie kontakty")
##        else:
##            print("nie usuwam")
##            
##            
##            
##    elif a==("koniec"):
##        if L:
##            with open("os.txt", "w", encoding="utf-8") as f:
##                f.write(f"imie,numer\n")
##                for x, y in L :
##                    f.write(f"{x},{y}\n")
##                print("Do widzenia!")
##                break
##        else:
##            k=input("Lista jest pusta, możliwe że txt. nie został załadowany, czy chcesz zapisać? Podaj y/n: ...")
##            if k==("n"):
##                print("ok")
##                
##            elif k==("y"):
##                print("zapisane")
##                with open("os.txt", "w", encoding="utf-8") as f:
##                    f.write(f"imie,numer\n")
##                    for x, y in L :
##                        f.write(f"{x},{y}\n")
##                    print("Do widzenia!")
##                    break
##        
##    else:
##        print("nie ma takiej komendy")


import tkinter as tk
from tkinter import messagebox
import os

L = []
P = []

# WCZYTYWANIE
if os.path.exists("os.txt"):
    with open("os.txt", "r", encoding="utf-8") as f:
        next(f, None)
        for line in f:
            x, y = line.strip().split(",")
            L.append([x, y])
        
# Funkcja do automatycznego ustawiania statusu
def set_status(msg, delay=1500):
    status_text.set(msg)
    root.after(delay, lambda: status_text.set("Gotowe"))

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="#F9FF40")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#F9FF40")  

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#9797AB")  

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# ZAPIS
def zapisz():
    with open("os.txt", "w", encoding="utf-8") as f:
        f.write("imie,numer\n")
        for x, y in L:
            f.write(f"{x},{y}\n")


# ODSWIEŻ LISTĘ
def odswiez():
    lista.delete(0, tk.END)
    for i, (x, y) in enumerate(L):
        lista.insert(tk.END, f"{i+1}. {x} - {y}")

        

#Czyszczenie
def czysc():
    if messagebox.askyesno("Czyść", f"Wyczyscić liste?"):
        for i in range(len(L)):
            P.append([L[i][0], L[i][1]])
        L.clear()
        odswiez()
        set_status(f"Wyczyszczono liste")
    
# DODAJ
def dodaj():
    imie = entry_imie.get()
    numer = entry_numer.get()
    if (imie and numer) and (imie!=("Imie") and numer!=("Numer")):
        L.append([imie, numer])
        odswiez()
        entry_imie.delete(0, tk.END)
        entry_numer.delete(0, tk.END)
        set_status(f"Dodano kontakt: {imie} - {numer}")
    else:
        messagebox.showwarning("Błąd", "Podaj imię i numer!")
        set_status("Błąd: brak imienia lub numeru")


# USUŃ
def usun():
    try:
        index = lista.curselection()[0]
        imie, numer = L[index]
        if messagebox.askyesno("Usuń", f"Usunąć {imie} - {numer}?"):
            P.append(L[index])
            del L[index]
            odswiez()
            set_status(f"Usunięto kontakt: {imie} - {numer}")
    except:
        messagebox.showwarning("Błąd", "Zaznacz kontakt!")
        set_status("Błąd: brak zaznaczonego imienia lub numeru")

# Przywróć
def przyw():
    try:
        index = lista.curselection()[0]
        imie, numer = P[index]
        if messagebox.askyesno("Przywróć", f"Przywrócić {imie} - {numer}?"):
            L.append(P[index])
            del P[index]
            odswiez()
            set_status(f"Przywrócono kontakt: {imie} - {numer}")
    except:
        messagebox.showwarning("Błąd", "Zaznacz kontakt!")
        set_status("Błąd: brak zaznaczonego imienia lub numeru")
        


# EDYTUJ
def edytuj():
    try:
        index = lista.curselection()[0]
        imie = entry_imie.get()
        numer = entry_numer.get()
        if imie and numer:
            L[index] = [imie, numer]
            odswiez()
            set_status(f"Edytowano kontakt: {imie} - {numer}")
        else:
            messagebox.showwarning("Błąd", "Podaj nowe dane!")
            set_status("Błąd: brak imienia lub numeru")
            
    except:
        messagebox.showwarning("Błąd", "Zaznacz kontakt!")
        set_status("Błąd: brak zaznaczonego imienia lub numeru")


# SZUKAJ
def szukaj():
    szukane = entry_szukaj.get().lower()
    lista.delete(0, tk.END)
    for i, (x, y) in enumerate(L):
        if szukane in x.lower():
            lista.insert(tk.END, f"{i+1}. {x} - {y}")
            set_status(f"Wyszukano kontakt: {imie} - {numer}")
#Kosz
def kosz():
    lista.delete(0, tk.END)
    for i, (x, y) in enumerate(P):
        lista.insert(tk.END, f"{i+1}. {x} - {y}")
    set_status(f"Przeszłeś do kosza")
    
#Cofnij
def cofnij():
    if messagebox.askyesno("Cofnij", f"Cofnąć liste?"):
        for i in range(len(P)):
            L.append([P[i][0], P[i][1]])
        P.clear()
        odswiez()
        set_status(f"Przywrócono kontakty")


# OKNO
root = tk.Tk()
root.configure(bg="#66141D")
root.title("Baza Kontaktów")
root.geometry("700x700")


# FRAME SEKCJE
top = tk.Frame(root, bg="#66141D")
top.grid(row=0, column=0, pady=10)

middle = tk.Frame(root, bg="#66141D")
middle.grid(row=1, column=0, pady=10)

bottom = tk.Frame(root, bg="#66141D")
bottom.grid(row=2, column=0, pady=10)

#SCROL BAR
list_frame = tk.Frame(top, bg="#1A6466")
list_frame.pack(fill="both", expand=True)
lista = tk.Listbox(top, width=60, height=15, bg="#1A6466", fg="#F9FF40")


scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

lista = tk.Listbox(list_frame, width=60, height=15, bg="#1A6466", fg="#F9FF40",
                   yscrollcommand=scrollbar.set)
lista.pack(side="left", fill="both", expand=True)

scrollbar.config(command=lista.yview)



# POLA
entry_imie = tk.Entry(middle, bg="#1A6466", fg="#F9FF40")
entry_imie.grid(row=0, column=0, padx=5)
add_placeholder(entry_imie, "Imię")

entry_numer = tk.Entry(middle, bg="#1A6466", fg="#F9FF40")
entry_numer.grid(row=0, column=1, padx=5)
add_placeholder(entry_numer, "Numer")

entry_szukaj = tk.Entry(middle, bg="#1A6466", fg="#F9FF40")
entry_szukaj.grid(row=1, column=0, columnspan=2, pady=5)
add_placeholder(entry_szukaj, "Szukaj imie")

# PRZYCISKI
tk.Button(bottom, text="Dodaj", command=dodaj, bg="#1A6466", fg="#F9FF40").grid(row=0, column=0, padx=4)
tk.Button(bottom, text="Edytuj", command=edytuj,bg="#1A6466", fg="#F9FF40").grid(row=0, column=1, padx=4)
tk.Button(bottom, text="Usuń", command=usun, bg="#1A6466", fg="#F9FF40").grid(row=0, column=2, padx=4)
tk.Button(bottom, text="Czyść", command=czysc, bg="#1A6466", fg="#F9FF40").grid(row=0, column=3, padx=4)
tk.Button(bottom, text="Kosz", command=kosz, bg="#1A6466", fg="#F9FF40").grid(row=0, column=4, padx=4)
tk.Button(bottom, text="Cofnij", command=cofnij, bg="#1A6466", fg="#F9FF40").grid(row=0, column=5, padx=4)
tk.Button(bottom, text="Odśwież", command=odswiez, bg="#1A6466", fg="#F9FF40").grid(row=0, column=6, padx=4)
tk.Button(bottom, text="Przywróć", command=przyw, bg="#1A6466", fg="#F9FF40").grid(row=0, column=6, padx=4)

# STATUS BAR
status_text = tk.StringVar()
status_text.set("Gotowe")

status_frame = tk.Frame(root, bg="#66141D")
status_frame.grid(row=3, column=0, sticky="we")

status_bar = tk.Label(status_frame, textvariable=status_text, bg="#1A6466", fg="#F9FF40", anchor="w", padx=10)
status_bar.pack(fill="x")

# ZAPISYWANIE
def zamknij():
    zapisz()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", zamknij)

odswiez()
root.mainloop()





















        
        
