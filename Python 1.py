##a=int(input())
##L=[]
##for i in range(a):
##    L.append(int(input()))
##
##print(L)

import os
L=[]
P=[]
i=0

if os.path.exists("os.txt"):
    with open("os.txt", "r", encoding="utf-8") as f:
        for line in f:
            imie, numer = line.strip().split(" ")
            L.append(imie)
            P.append(numer)
            l=len(L)



while True:
    a=input("Co chcesz zrobic? ").lower()
    if a==("dodaj"):
        x=input("Podaj imie: ")
        y=input("Podaj numer: ")
        L.append(x)
        P.append(y)
        print("Dodano ",x," z numerem ",y)
        l=len(L)
    elif a==("szukaj"):
        b=input("Podaj imie: ")
        if b in L:
            c=L.index(b)
            print(L[c],P[c])
        else:
            print("Kontakt nie isnieje")
        
    elif a==("wyswietl"):
        if L:
            for i in range (l):
                print(L[i],P[i])
                i+=1
                i=0
        else:
            print("Lista kotaktów pusta")
    elif a==("usun"):
        b = input("Podaj imię do usunięcia: ")
        if b in L:
            c = L.index(b)
            L.pop(c)
            P.pop(c)
            print("Usunięto kontakt ",b)
            l=len(L)
    elif a==("koniec"):
        with open("os.txt", "w", encoding="utf-8") as f:
            for imie, numer in zip(L, P):
                f.write(f"{imie} {numer}\n")
        print("Do widzenia!")
        break
    
    else:
        print("nie ma takiej komendy")


        
        
