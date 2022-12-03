from os import system  
from data import *
import csv
import sys
filename='berletek.csv'
filename='idopontok.csv'




def menu():
    system('cls')
    print('-----Menu-----')
    print('0-Kilépés')
    print('1-Bérlet választás')
    print('2-Bérlet tulajdonságok')
    print('3-Legkedveltebb edző')
    print('4-Csoportos edzés')
    return input('Kérem válasszon: ')


def berlethozzaadas():
    system('cls')
    print('-------Új tag-------')
    nev=input('Adja meg a nevét: ')
    fajta=input('Válasszon egy bérletet(Bronz,Silver,Gold): ')
    edzo=input('Edzők: \nTóth Zalán \nTakács Dániel\nVági-Strausz Botond\nVálasszon egy edzőt:')
    azeedzo(edzo)
    edzok.append(edzo)
    adatokmentese(nev,fajta,edzo)
    input('Sikeres felvétel.Tovább..')


def azeedzo(edzo):
    options2=['Tóth Zalán', 'Takács Dániel', 'Vági-Strausz Botond']
    if edzo == options2[0]:
            pass
    elif edzo== options2[1]:
            pass
    elif edzo == options2[2]:
           pass
    else:
        sys.exit()






def adatokmentese(nev,fajta,edzo):
    file=open('berletek.csv', 'a', encoding='utf-8')
    file.write(f'{nev};{fajta};{edzo}\n')
    file.close


def tulajdonsagok():
    system('cls')
    print('-----Bérlet információk-----')
    print('0-Vissza')
    print('1-Bronz')
    print('2-Silver')
    print('3-Gold')
    return input ('Kérem válasszon: ')




def fajlBeolvasas():
    file=open('idopontok.csv','r',encoding='utf-8')
    file.readline() 
    for egysor in file:
        darabolt=egysor.strip().split(',') 
        idopontok.append(darabolt[0])
        csoportedzo.append((darabolt[1]))
    file.close()

def Kiir():
    system('cls')
    print('------IDŐPONTOK-------\n')
    for ido in idopontok:
        print(f'\t{ido}')
    

def vaneedzes(ido):
    system('cls')
    while ido in idopontok:
        if ido==idopontok:
            print('Jó edzést')
        else:
            print('Sajns nincs ilyen időpont')

def search():
    ido=(input('Adjon meg egy időpontot: '))
    if ido in idopontok:
        system('cls')
        print('Jó edzést')
    else:
        system('cls')
        print('Sajnos nincs ilyen időpont')



def menu2(choice2):
    while choice2!='0':
        choice2=tulajdonsagok()
        if choice2=='1':
            system('cls')
            print('------BRONZ-------\n')
            print('Sajnos nincs semmi előny')
        elif choice2=='2':
            system('cls')
            print('------SILVER-------\n')
            print('-sauna \n-protein shake')
        elif choice2=='3':
            system('cls')
            print('------GOLD-------\n')
            print(' -sauna \n-protein shake \n-private parkoló és autó takarítás')
        elif choice2=='0':
            menu1('0')
        input()

def menu1(choice):
    while choice!='0':
        choice=menu()
        if choice=='1':
            berlethozzaadas()
        elif choice=='2':
            menu2('')
        elif choice=='3':
            fajlBeolvasas2()
            system('cls')
            print('------Leggyakoribb-------\n')
            kialeggyakoribb()
        elif choice=='4':
            system('cls')
            fajlBeolvasas()
            Kiir()
            search()
            input()


def kialeggyakoribb():
    TZ = 0    
    TD = 0
    VSB = 0
    options=['Tóth Zalán', 'Takács Dániel', 'Vági-Strausz Botond']
    for i in range(len(edzok)):
        if edzok[i] == options[0]:
            TZ += 1
        elif edzok[i] == options[1]:
            TD += 1
        elif edzok[i] == options[2]:
            VSB +=1 
        else:
            continue
        
    if TZ > TD:
        print(f'{options[0]} a leggyakoribb személyi edző')
    elif TZ > VSB:
        print(f'{options[0]} a leggyakoribb személyi edző')
    elif TD > TZ:
        print(f'{options[1]} a leggyakoribb személyi edző')
    elif TD > VSB:
        print(f'{options[1]} a leggyakoribb személyi edző')
    elif TZ < VSB:
        print(f'{options[2]} a leggyakoribb személyi edző')
    elif TD < VSB:
        print(f'{options[2]} a leggyakoribb személyi edző')
    else:
        print('buggos a script')
    
    input('')

        


def fajlBeolvasas2():
    file=open('berletek.csv','r',encoding='utf-8')
    file.readline() 
    for egysor in file:
        darabolt=egysor.strip().split(';') 
        edzok.append((darabolt[2]))
    file.close()