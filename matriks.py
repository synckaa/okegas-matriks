from fractions import Fraction
import os


def matriks2():
    print("=== Matriks 2x2 ===")
    a = [[Fraction(input("masukan nilai matriks A11 : ")), Fraction(input("masukan nilai matriks A12 : "))],
         [Fraction(input("masukan nilai matriks A21 : ")),Fraction(input("masukan nilai matriks A22 : "))]]


    det = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

    if det == 0:
        print("Matriks tidak valid!")
        return

    invers = [
        [Fraction(a[1][1], det), Fraction(-a[0][1], det)],
        [Fraction(-a[1][0], det), Fraction(a[0][0], det)]
    ]

    os.system("clear")
    print("Determinan =", det)
    print("Invers :")
    print(f"[ {invers[0][0]}   {invers[0][1]} ]")
    print(f"[ {invers[1][0]}   {invers[1][1]} ]")


def matriks3():
    a = [[Fraction(input("masukan nilai matriks A11 :")), Fraction(input("masukan nilai matriks A12 :")),
          Fraction(input("masukan nilai matriks A13 :"))],
         [Fraction(input("masukan nilai matriks A21 :")), Fraction(input("masukan nilai matriks A22 :")),
          Fraction(input("masukan nilai matriks A23 :"))],
         [Fraction(input("masukan nilai matriks A31 :")), Fraction(input("masukan nilai matriks A32 :")),
          Fraction(input("masukan nilai matriks A33 :"))]]


    det = (
            a[0][0] * a[1][1] * a[2][2] +
            a[0][1] * a[1][2] * a[2][0] +
            a[0][2] * a[1][0] * a[2][1] -
            a[0][2] * a[1][1] * a[2][0] -
            a[0][0] * a[1][2] * a[2][1] -
            a[0][1] * a[1][0] * a[2][2]
    )

    if det == 0 :
        print("Matriks tidak valid!")

    kof = [
        [(a[1][1] * a[2][2] - a[1][2] * a[2][1]),
         (a[1][0] * a[2][2] - a[1][2] * a[2][0]) * -1,
         (a[1][0] * a[2][1] - a[1][1] * a[2][0])],

        [(a[0][1] * a[2][2] - a[0][2] * a[2][1]) * -1,
         (a[0][0] * a[2][2] - a[0][2] * a[2][0]),
         (a[0][0] * a[2][1] - a[0][1] * a[2][0]) * -1],

        [(a[0][1] * a[1][2] - a[0][2] * a[1][1]),
         (a[0][0] * a[1][2] - a[0][2] * a[1][0]) * -1,
         (a[0][0] * a[1][1] - a[0][1] * a[1][0])]
    ]
    invers = []

    for row in range(3):
        for col in range(3):
            invers.append(Fraction(kof[row][col],det))

    os.system("clear")
    print(f"determinan : {det}")
    print(f"Invers :")
    print(f"[ {invers[0]} {invers[3]} {invers[6]} ]")
    print(f"[ {invers[1]} {invers[4]} {invers[7]} ]")
    print(f"[ {invers[2]} {invers[5]} {invers[8]} ]")



if __name__ == "__main__" :
    while True:
        os.system("clear")
        print("=== My Matriks ===")
        print("1. Matriks 2x2")
        print("2. Matriks 3x3")
        print("0. Keluar")
        pilih = input("Pilih menu : ")

        if pilih == "1":
            matriks2()
        elif pilih == "2":
            matriks3()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")

        ulang = input("\nUlang ke menu? (y/n) : ")
        if ulang.lower() != "y":
            break

