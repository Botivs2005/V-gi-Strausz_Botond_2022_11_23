from os import system  
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

