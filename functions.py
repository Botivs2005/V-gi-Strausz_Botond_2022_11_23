from os import system  
from data import *
import csv
filename='berletek.csv'




def menu():
    system('cls')
    print('-----Menu-----')
    print('0-Kilépés')
    print('1-Bérlet választás')
    print('2-Bérlet tulajdonságok')
    print('3-Személyi edzés')
    print('4-Csoportos edzés')
    return input('Kérem válasszon: ')


def berlethozzaadas():
    system('cls')
    print('-------Új tag-------')
    nev=input('Adja meg a nevét: ')
    fajta=input('Válasszon egy bérletet(Bronz,Silver,Gold): ')
    edzo=input('Edzők: \nTóth Zalán \nTakács Dániel\nVági-Strausz Botond\nVálasszon egy edzőt:')
    adatokmentese(nev,fajta,edzo)
    input('Sikeres felvétel.Tovább..')

def adatokmentese(nev,fajta,edzo):
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{nev};{fajta};{edzo}')
    file.close


def tulajdonsagok():
    system('cls')
    print('-----Bérlet információk-----')
    print('0-Vissza')
    print('1-Bronz')
    print('2-Silver')
    print('3-Gold')
    return input ('Kérem válasszon: ')



def idopontokkiir():
    with open('idopontok.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)

        for line in csv_reader:
            print(line[0])
    melyikedzes(input('Melyik edzésre szeretne menni: '))


def melyikedzes(line,csv_file):
    for line in csv_file:
        if melyikedzes==line:
            print('Sikeres felvétel jó edzést')
        else:
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
            pass
        elif choice=='4':
            idopontokkiir()
            melyikedzes()
            input()


