##a=int(input())
##L=[]
##for i in range(a):
##    L.append(int(input()))
##
##print(L)

import os
L=[]



if os.path.exists("os.txt"):
    with open("os.txt", "r", encoding="utf-8") as f:
        next (f)
        for line in f:
            x, y = line.strip().split(",")
            L.append([x,y])
            


print("Witaj w bazie danych telefnicznych, dostępne komendy to: dodaj, edytuj, usun, ilosc, szukaj, wyswietl, koniec, help")

while True:
    a=input("Co chcesz zrobic? ").lower()
    if a==("dodaj"):
        x=input("Podaj imie: ")
        y=input("Podaj numer: ")
        L.append([x,y])
        
        print("Dodano ",x," z numerem ",y)
    elif a==("help"):
        print("Dostepne komendy to: dodaj, edytuj, usun, ilosc, szukaj, wyswietl, koniec, help")
    
    elif a==("edytuj"):
        b=input("Podaj imie: ")
        for i in range(len(L)):
            if L[i][0]==b:
                x=input("Podaj zmienione imie: ")
                y=input("Podaj zmieniony numer: ")
                L[i][0]= x
                L[i][1]= y
        
                print("Zmieniono na ",x," z numerem ",y)
                break
        else:
            print("Kontakt nie isnieje")

        

    elif a == ("ilosc"):
        print("masz ",len(L)," zapisane numery")
        
    elif a==("szukaj"):
        n=0
        b=input("Podaj imie: ")
        for i in range(len(L)):
            if b.lower() in L[i][0].lower():
                print("Na pozycji: ",i+1, " ",L[i][0], "-", L[i][1])
        for i in range(len(L)):
            if b.lower() not in L[i][0].lower():
                n+=1
        if n==len(L):
            print("Kontakt nie isnieje")
        n=0
        
    elif a==("wyswietl"):
        if L:
            for i in range(len(L)):
                print(i+1," ",L[i][0], "-", L[i][1])
                
                
        else:
            print("Lista kotaktów pusta")
            
    elif a==("usun"):
        b = input("Podaj imię do usunięcia: ")
        for i in range(len(L)):
            if L[i][0]==b:
                print("Czy napewno chcesz usunąć kontakt: ",L[i][0], "-", L[i][1])
                u=input("Podaj: y/n ...")
                if u=="y":
                  del L[i]
                  print("Usunięto kontakt ",b)
                  break
                elif u=="n":
                    print("ok, nie usuwam")
                    break
                else:
                    print("miałes jedno zadanie")
                    break
        else:
            print("Kontakt nie istnieje")
            
    elif a==("koniec"):
        if L:
            with open("os.txt", "w", encoding="utf-8") as f:
                f.write(f"imie,numer\n")
                for x, y in L :
                    f.write(f"{x},{y}\n")
                print("Do widzenia!")
                break
        else:
            print("txt. nie wczytany, nie zapisze danych, podaj komende wyswietl dla bezpieczenstwa")
            
    else:
        print("nie ma takiej komendy")


        
        
