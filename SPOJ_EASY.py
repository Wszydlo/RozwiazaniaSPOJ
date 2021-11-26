import sys

def suma():
    suma = 0
    while True:
        try:
            input_liczba = int(input())
            suma+= input_liczba
            print(suma)
        except EOFError:
            break

