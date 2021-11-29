import sys

#rozwiazanie problemu Suma
def suma():
    suma = 0
    while True:
        try:
            input_liczba = int(input())
            suma+= input_liczba
            print(suma)
        except EOFError:
            break

#rozwiazanie problemu rownanie kwadratowe
def kwadratowe():
    for linia in sys.stdin:
            linia = str.split(linia)
            delta = float(linia[1])**2-4*float(linia[0])*float(linia[2])
            if delta>0:
                print(2)
            elif delta ==0:
                print(1)
            else:
                print(0)
#rozwiazanie problemu  tablica
def tablica():
    for linia in sys.stdin:
        linia = str.split(linia)
        linia = [linia[-i-1] for i in range(len(linia))]
        print(*linia)

#rozwiazanie problemu Gra Euklidesa
def Euklides():
    n = int(input())
    for i in range(n):
        linia = str.split(sys.stdin.readline())
        A, B = int(linia[0]), int(linia[1])
        while A != B:
            if(A < B):
                B= B - A
            else:
                A= A - B
        print(A+B)    

#rozwiazanie problemu polowa
def polowa():
    n = int(input())
    for i in range(n):
        x = input()
        print(x[:len(x)//2])

#Podzielnosc
def podzielnosc():
    n = int(input())
    for i in range(n):
        rozwiazania = []
        linia = str.split(sys.stdin.readline())
        for x in range(1,int(linia[0])):
            linia[1],linia[2]=int(linia[1]),int(linia[2])
            if(x%linia[1]==0 and x%linia[2]!=0):
                rozwiazania.append(x)
        print(*rozwiazania)
#test 3
def test_3():
    while(True):
        line = int(input())
        if line!=42:
            prev = line
            print(line)
            break
        else:
            print(line)
    ilosc = 0
    while True:
        try:
            if ilosc == 3:
                break
            actual = int(input())
            print(actual)
            if actual==prev==42:
                pass
            elif actual==42 and prev !=42:
                ilosc+=1
                prev = actual
            elif actual !=42:
                prev = actual
        except EOFError:
            break
# Problem Collatza
def Collatz():
    n = int(input())
    for i in range(n):
        xn = int(input())
        if xn == 1:
            print(0)
        else:
            i = 0
            while(xn != 1):
                if(xn%2):
                    xn = 3*xn+1
                    i+=1
                else:
                    xn = xn/2
                    i+=1
            print(i)

# Transpozycja maceirzy:
def Transpose():
    for linia in sys.stdin:
        linia = str.split(linia)
        macierz = []
        for i in range(int(linia[0])):
            wiersz_macierzy = str.split(sys.stdin.readline())
            macierz.append(wiersz_macierzy)
        transpozycja = []
        for i in range(int(linia[1])):
            print(*[macierz[j][i] for j in range(int(linia[0]))])

#Parzyste nieparzyste
def Parzyste_nieparzyste():
    n = int(input())
    for i in range(n):
        linia = str.split(sys.stdin.readline())[1:]
        nieparzyste = [linia[2*x] for x in range(len(linia)//2)]
        parzyste = [linia[2*x+1] for x in range(len(linia)//2)]
        if(len(linia)%2):
            print(*parzyste,*nieparzyste,linia[len(linia)-1])
        else:
            print(*parzyste,*nieparzyste)

#zliczacz liter
def Zliczacz():
    n = int(input())
    mapa = dict()
    podzielone = []
    for i in range(n):
        slowo = str.split(str.strip(sys.stdin.readline()))
        for x in slowo:
            podzielone = list(x)
            for literka in podzielone:
                if literka not in mapa:
                    mapa[literka] = 1
                else:
                    mapa[literka] += 1
    mapa = sorted(mapa.items(), key = lambda x:(ord(x[0]) +x[0].isupper()*100))
    for key,value in mapa:
        print(key,value)
#PESEL
def PESEL():
    mnozniki = [1,3,7,9,1,3,7,9,1,3,1]
    for i in range(int(input())):
        suma_cyfr = 0
        liczby = str.strip(sys.stdin.readline())
        liczby = [int(x) for x in liczby]
        print(liczby)
        for x in range(len(liczby)):
            suma_cyfr += liczby[x]*mnozniki[x]
        if(suma_cyfr%10 ==0 and suma_cyfr !=0):
            print('D')
        else:
            print('N')

