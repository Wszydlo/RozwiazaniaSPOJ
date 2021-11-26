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
