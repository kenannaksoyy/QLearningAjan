from tkinter import *
from tkinter.ttk import *
import numpy as np
import random
from random import randint, choice


class Ajan:
    ajan_isim = "James Bond"
    ajan_id = "007"
    ajan_x = 0
    ajan_y = 0

    def ajan_bilgileri(self):
        print("Ajan Bilgileri")
        print(self.ajan_isim, self.ajan_id)
        print("Ajan Kordinat Bilgileri")
        print("X:", self.ajan_x, "Y:", self.ajan_y)

    def ajan_hareket_x(self, x):
        self.ajan_x += x

    def ajan_hareket_y(self, y):
        self.ajan_y += y


class Kutular:

    def kutular_renk(self, boyut, engel_sayısı):
        kutular = [["S" for x in range(boyut)] for y in range(boyut)]
        sayı_liste = range(0, boyut)
        for y in range(0, boyut):
            kırmızı_kutular = random.sample(sayı_liste, engel_sayısı)
            for x in range(0, boyut):
                for eleman in kırmızı_kutular:
                    if eleman == x:
                        kutular[y][x] = "K"
        kutular[0][0] = "M"
        kutular[boyut - 1][boyut - 1] = "Y"
        return kutular

    def kutular_ödül(self, gelen_kutular, boyut):
        kutular = [[3 for x in range(boyut)] for y in range(boyut)]
        for y in range(0, boyut):
            for x in range(0, boyut):
                if gelen_kutular[y][x] == "K":
                    kutular[y][x] = -3
        kutular[0][0] = 0
        kutular[boyut - 1][boyut - 1] = 5
        return kutular

    def kutular_no(self, boyut):
        kutular = [[0 for x in range(boyut)] for y in range(boyut)]
        sayac_no = 0
        for y in range(0, boyut):
            for x in range(0, boyut):
                kutular[y][x] = sayac_no
                sayac_no += 1
        return kutular


class Arayuz():

    def Arayuz_olustur(self, gelen_kutular_renk, gelen_kutular_no, boyut, Ajan_referans):
        pencere = Tk()
        pencere.title("James Bond Q Learning")
        pencere.geometry("600x450")
        uygulama = Frame(pencere)
        uygulama.grid()
        sayac_x = 0
        sayac_y = -40

        for y in range(0, boyut):
            sayac_y += 25
            sayac_x = 0
            for x in range(0, boyut):
                if gelen_kutular_renk[y][x] == "K":
                    kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="red", width=3).place(
                        x=20 + sayac_x, y=20 + sayac_y)
                    sayac_x += 25

                elif gelen_kutular_renk[y][x] == "M":
                    kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="blue", width=3).place(
                        x=20 + sayac_x, y=20 + sayac_y)
                    sayac_x += 25

                elif gelen_kutular_renk[y][x] == "Y":
                    kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="green", width=3).place(
                        x=20 + sayac_x, y=20 + sayac_y)
                    sayac_x += 25

                else:
                    kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="yellow", width=3).place(
                        x=20 + sayac_x, y=20 + sayac_y)
                    sayac_x += 25

        ajan_konum_kutucuk_text = Label(pencere, text=(
        "Ajan Bilgisi", Ajan_referans.ajan_isim, Ajan_referans.ajan_id, " X konumu ", Ajan_referans.ajan_x,
        " Y konumu ", Ajan_referans.ajan_y), background="yellow").place(x=20, y=60 + sayac_y)
        ajan_hedef_kutucuk_text = Label(pencere, text=(
        " Ajan Hedef Kutu  ", boyut * boyut - 1, "Kutu Konum Bilgisi", "X", boyut - 1, "Y", boyut - 1),
                                        background="yellow").place(x=20, y=80 + sayac_y)

        pencere.mainloop()
    def Arayuz_olustur_son(self, gelen_kutular_renk, gelen_kutular_no, boyut, Ajan_referans,gelen_yol_kutular):
        pencere = Tk()
        pencere.title("James Bond Q Learning")
        pencere.geometry("600x450")
        uygulama = Frame(pencere)
        uygulama.grid()
        sayac_x = 0
        sayac_y = -40

        for y in range(0, boyut):
            sayac_y += 25
            sayac_x = 0
            for x in range(0, boyut):
                if gelen_kutular_renk[y][x] == "K":
                    yol_kontrol = 0
                    for z in gelen_yol_kutular:
                        if gelen_kutular_no[y][x] == z:
                            yol_kontrol=1
                    if yol_kontrol == 1:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="black", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25
                        yol_kontrol = 0
                    else:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="red", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25


                elif gelen_kutular_renk[y][x] == "M":
                    yol_kontrol = 0
                    for z in gelen_yol_kutular:
                        if gelen_kutular_no[y][x] == z:
                            yol_kontrol=1
                    if yol_kontrol == 1:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="black", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25
                        yol_kontrol = 0
                    else:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="blue", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25

                elif gelen_kutular_renk[y][x] == "Y":
                    yol_kontrol = 0
                    for z in gelen_yol_kutular:
                        if gelen_kutular_no[y][x] == z:
                            yol_kontrol = 1
                    if yol_kontrol == 1:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="black", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25
                        yol_kontrol = 0
                    else:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="green", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25

                else:
                    yol_kontrol = 0
                    for z in gelen_yol_kutular:
                        if gelen_kutular_no[y][x] == z:
                            yol_kontrol = 1
                    if yol_kontrol == 1:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="black", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25
                        yol_kontrol = 0
                    else:
                        kutucuk = Label(pencere, text=gelen_kutular_no[y][x], background="yellow", width=3).place(
                            x=20 + sayac_x, y=20 + sayac_y)
                        sayac_x += 25

        kutucuk = Label(pencere, text="Ajanın Yol Çizgisi", background="yellow", ).place(x=20, y=40+sayac_y)
        sayac_z = 40
        kutucuk = Label(pencere, text=gelen_yol_kutular, background="yellow",).place(
        x=20 , y=60+sayac_y)

        pencere.mainloop()


def dosya_yazdır(gelen_kutular_renk, boyut):
    engel_dosya = open("engel.txt", "w")
    for y in range(0, boyut):
        engel_dosya.write("\n")
        for x in range(0, boyut):
            str_x = str(x)
            str_x1 = str_x + ","
            str_y = str(y)
            str_y1 = str_y + ","
            if (gelen_kutular_renk[y][x] == "K"):
                yazılacak = "( " + str_y1 + str_x1 + gelen_kutular_renk[y][x] + " )"
                engel_dosya.write(yazılacak)


def R_matrix(gelen_kutular_renk, gelen_kutular_no, boyut):
    R = [[-1 for x in range(boyut * boyut)] for y in range(boyut * boyut)]
    for y in range(0, boyut):
        for x in range(0, boyut):
            if (gelen_kutular_renk[y][x] != "K"):
                if x - 1 != -1 and gelen_kutular_renk[y][x - 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y][x - 1]] = 0
                if x + 1 != boyut and gelen_kutular_renk[y][x + 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y][x + 1]] = 0
                if y - 1 != -1 and gelen_kutular_renk[y - 1][x] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y - 1][x]] = 0
                if y + 1 != boyut and gelen_kutular_renk[y + 1][x] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y + 1][x]] = 0
                if y - 1 != -1 and x - 1 != -1 and gelen_kutular_renk[y - 1][x - 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y - 1][x - 1]] = 0
                if y - 1 != -1 and x + 1 != boyut and gelen_kutular_renk[y - 1][x + 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y - 1][x + 1]] = 0
                if y + 1 != boyut and x - 1 != -1 and gelen_kutular_renk[y + 1][x - 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y + 1][x - 1]] = 0
                if y + 1 != boyut and x + 1 != boyut and gelen_kutular_renk[y + 1][x + 1] != "K":
                    R[gelen_kutular_no[y][x]][gelen_kutular_no[y + 1][x + 1]] = 0

    if (gelen_kutular_renk[boyut - 2][boyut - 1] != "K"):
        R[gelen_kutular_no[boyut - 2][boyut - 1]][gelen_kutular_no[boyut - 1][boyut - 1]] = 100
    if (gelen_kutular_renk[boyut - 1][boyut - 2] != "K"):
        R[gelen_kutular_no[boyut - 1][boyut - 2]][gelen_kutular_no[boyut - 1][boyut - 1]] = 100
    if (gelen_kutular_renk[boyut - 2][boyut - 2] != "K"):
        R[gelen_kutular_no[boyut - 2][boyut - 2]][gelen_kutular_no[boyut - 1][boyut - 1]] = 100
    return R


JamesBond = Ajan()
kutular_referans = Kutular()
boyut = 10
engel_sayısı = 4
kutular_renk = kutular_referans.kutular_renk(boyut, engel_sayısı)
kutular_ödül = kutular_referans.kutular_ödül(kutular_renk, boyut)
kutular_no = kutular_referans.kutular_no(boyut)

dosya_yazdır(kutular_renk, boyut)
r_matrix = R_matrix(kutular_renk, kutular_no, boyut)

arayuz_referans = Arayuz()
arayuz_referans.Arayuz_olustur(kutular_renk, kutular_no, boyut, JamesBond)


class Yol_Bulucu:
    def __init__(self, r_matrix, no_episodes=1000, gamma=0.9):

        self.r = r_matrix
        self.current_q = np.zeros_like(r_matrix)
        self.no_episodes = no_episodes
        self.gamma = gamma

    def Ulaşılabilenler(self, row):

        for idx, col in enumerate(self.r[row]):
            if col != -1:
                yield idx

    def Bellmann(self, src, dest):

        return self.r[src][dest] + self.gamma * max(
            [self.current_q[dest][reachable] for reachable in self.Ulaşılabilenler(dest)])

    def Çözümleyici(self, init, final):
        number_nodes = len(self.current_q)
        for episode in range(self.no_episodes):
            current = init
            temp_q = np.copy(self.current_q)
            while True:
                dest = choice([element for element in self.Ulaşılabilenler(current)])
                temp_q[current][dest] = self.Bellmann(current, dest)
                if current == final:
                    self.current_q = temp_q
                    break
                current = dest
        return 100 * self.current_q / np.max(self.current_q)

    def Yol(self, init, final):

        res = self.Çözümleyici(init, final)
        current = init
        yol = [init]
        while current != final:
            m = max(res[current])
            for el in range(len(res)):
                if res[current][el] == m:
                    current = el
                    break
            yol.append(current)
        print("Yol Hazır")
        return yol


Ajan_Yolcu = Yol_Bulucu(r_matrix)
print("Q learning bulduğu en kısa yol hazırlanıyor")
yol_kutuları=Ajan_Yolcu.Yol(0, boyut * boyut - 1)
print(yol_kutuları)
arayuz_referans = Arayuz()
arayuz_referans.Arayuz_olustur_son(kutular_renk, kutular_no, boyut, JamesBond,yol_kutuları)
