from os import system  
from data import *
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
    print('1-Silver')
    print('3-Gold')
    return input ('Kérem válasszon: ')



def edzokkiir():
    legkedveltebb_szemelyi_edzo=''
    for i in range(0,len(edzok)):
        print(f'\t{i+1}. {emberek[i]} {berlet[i]} {edzok[i]}')
    input('Tovább...')


def fajlBeolvasas():
    file=open(filename,'r', encoding='utf-8')
    file.readline() 
    for egysor in file:
        darabolt=egysor.strip().split(';')
        emberek.append(darabolt[0])
        berlet.append(darabolt[1])
        edzok.append(darabolt[2])

    file.close()

def menu2(choice2):
    while choice2!='0':
        choice2=tulajdonsagok()
        if choice2=='1':
            print('asd')
        elif choice2=='2':
            print('m')
        elif choice2=='3':
            print('ne')
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
            fajlBeolvasas()
            edzokkiir()
        elif choice=='4':
            pass


