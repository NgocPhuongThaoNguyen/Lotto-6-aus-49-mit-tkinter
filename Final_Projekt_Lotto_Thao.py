import tkinter as tk
import pygame
from random import randint
import mouse
# import win32api
import time

# ----------------------------------------------------------------------------------------
cordinate_list = {
        "1": [(4, 35), (4, 35)],
        "2": [(56, 83), (4, 35)],
        "3": [(104, 136), (4, 35)],
        "4": [(153, 186), (4, 35)],
        "5": [(206, 237), (4, 35)],
        "6": [(255, 287), (4, 35)],
        "7": [(305, 335), (4, 35)],
        "8": [(4, 35), (62, 81)],
        "9": [(56, 83), (62, 81)],
        "10": [(104, 136), (62, 81)],
        "11": [(153, 186), (62, 81)],
        "12": [(206, 237), (62, 81)],
        "13": [(255, 287), (62, 81)],
        "14": [(305, 335), (62, 81)],
        "15": [(4, 35), (97, 136)],
        "16": [(56, 83), (97, 136)],
        "17": [(104, 136), (97, 136)],
        "18": [(153, 186), (97, 136)],
        "19": [(206, 237), (97, 136)],
        "20": [(255, 287), (97, 136)],
        "21": [(305, 335), (97, 136)],
        "22": [(4, 35), (147, 181)],
        "23": [(56, 83), (147, 181)],
        "24": [(104, 136), (147, 181)],
        "25": [(153, 186), (147, 181)],
        "26": [(206, 237), (147, 181)],
        "27": [(255, 287), (147, 181)],
        "28": [(305, 335), (147, 181)],
        "29": [(4, 35), (197, 232)],
        "30": [(56, 83), (197, 232)],
        "31": [(104, 136), (197, 232)],
        "32": [(153, 186), (197, 232)],
        "33": [(206, 237), (197, 232)],
        "34": [(255, 287), (197, 232)],
        "35": [(305, 335), (197, 232)],
        "36": [(4, 35), (248, 283)],
        "37": [(56, 83), (248, 283)],
        "38": [(104, 136), (248, 283)],
        "39": [(153, 186), (248, 283)],
        "40": [(206, 237), (248, 283)],
        "41": [(255, 287), (248, 283)],
        "42": [(305, 335), (248, 283)],
        "43": [(4, 35), (299, 332)],
        "44": [(56, 83), (299, 332)],
        "45": [(104, 136), (299, 332)],
        "46": [(153, 186), (299, 332)],
        "47": [(206, 237), (299, 332)],
        "48": [(255, 287), (299, 332)],
        "49": [(305, 335), (299, 332)]
    }

kugel_matrix = [[1, 2, 3, 4, 5, 6, 7],
                [8, 9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21],
                [22, 23, 24, 25, 26, 27, 28],
                [29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42],
                [43, 44, 45, 46, 47, 48, 49]
                ]

kugel_draw = {
        1: (5, 5),
        2: (55, 5),
        3: (105, 5),
        4: (155, 5),
        5: (205, 5),
        6: (255, 5),
        7: (305, 5),
        8: (5, 50),
        9: (55, 50),
        10: (105, 50),
        11: (155, 50),
        12: (205, 50),
        13: (255, 50),
        14: (305, 50),
        15: (5, 100),
        16: (55, 100),
        17: (105, 100),
        18: (155, 100),
        19: (205, 100),
        20: (255, 100),
        21: (305, 100),
        22: (5, 150),
        23: (55, 150),
        24: (105, 150),
        25: (155, 150),
        26: (205, 150),
        27: (255, 150),
        28: (305, 150),
        29: (5, 200),
        30: (55, 200),
        31: (105, 200),
        32: (155, 200),
        33: (205, 200),
        34: (255, 200),
        35: (305, 200),
        36: (5, 250),
        37: (55, 250),
        38: (105, 250),
        39: (155, 250),
        40: (205, 250),
        41: (255, 250),
        42: (305, 250),
        43: (5, 300),
        44: (55, 300),
        45: (105, 300),
        46: (155, 300),
        47: (205, 300),
        48: (255, 300),
        49: (305, 300)
    }

class Graphik:
    __fenster: tk.Tk
    __x: int = 100
    __y: int = 100
    __breite: int = 530
    __hoehe: int = 440
    __list_k = []  # the global list beinhalt die eingetippte Kugeln von Benutzer

    # -----------------------------------------------------------------------------------

    def __init__(self):

        self.__fenster = tk.Tk()
        position = f"+{self.__x}+{self.__y}"  # +2100+100 nur 2 variable
        groess = f"{self.__breite}x{self.__hoehe}"
        geometrie = groess + position  # 800x600+2100+100
        self.__fenster.geometry(geometrie)

    # ------------------------------------------------------------------------

    def __lottoziehung(self):
        ziehung = list()
        while (len(ziehung) < 6):
            zufall = randint(1, 49)
            if (not zufall in ziehung):
                ziehung.append(zufall)
        ziehung.sort()
        return ziehung

    # -----------------------------------------------------------------------------------------
    # Hier ist die Funktion, um die Kugel Nummer zu finden und markieren (Benutzer eintippen auf Lottoschein)
    def __kugeln_finden(self, xval, yval):
        kugel = -1  # -1 bedeutet kein Kugeln gefunden unter dem [x, y] Koordinaten
        m_kugel = kugel_matrix
        kugel_cordinate_value = cordinate_list.values()
        # Suchen in die Kugel_codinate_value liste, ob xval und yval im interval Bereich sind.
        for i in kugel_cordinate_value:
            x1 = i[0][0]  # x_min von Kugeln Bereich
            x2 = i[0][1]  # x_max von Kugel Bereich
            y1 = i[1][0]  # y_min
            y2 = i[1][1]  # y_max
            if (xval in range(x1, x2)) and (yval in range(y1,y2)):
                # Wenn es gefunden ist, rechnen wir die Spalte und Zeile, um die Kugel Number in matrix 7x7 zu finden
                x12 = round(((x1 + x2) / 2)/50)
                y12 = round(((y1 + y2) / 2)/50)
                kugel = m_kugel[y12][x12]  # hier ist die Number von Kugel gefunden
                # Finden im kugel_draw dict, um die Koordination zu markieren
                x = kugel_draw[kugel][0]
                y = kugel_draw[kugel][1]
                self.__draw_circle_eingeben(x, y, kugel)
        return kugel

    # ----------------------------------------------------------------------------------------
    # es handelt sich Mouse event
    def __kugeln_select(self, event):
        xval = event.x
        yval = event.y
        global __list_k

        if len(self.__list_k) == 6:
            self.__text_label.set("6 Kugeln hat schon ausgewählt! <Spielen> / <Stop> / <Exit>")
            button_2.config(state='active')
            button_3.config(state='active')
            return

        kugel = self.__kugeln_finden(xval, yval)
        # Liste Kugeln append
        if kugel != -1:
            if kugel in self.__list_k:
                self.__text_label.set("Diese Kugeln ist doppelt. Nochmal auswählen")
            else:
                self.__list_k.append(kugel)
                self.__text_label.set("Bitte 6 Kugeln auswählen")

        # 6 ausgewählte von User wird auf canvas_tippen darstellen
        self.__list_k.sort()
        x = 10
        y = 5
        for i in self.__list_k:
            self.__draw_circle_tippen(x, y, i)
            y += 50
        canvas_tippen.update()

        # -----------------------------------------------------------------------------------------

    def __draw_circle(self, x, y, label):
        canvas.create_oval(x, y, x + 30, y + 30, fill="#00ffff", outline="#00bfff", width=5)
        canvas.create_text(x + 15, y + 15, text=label)

    def __draw_circle_eingeben(self, x, y, label):
        canvas.create_oval(x, y, x + 30, y + 30, fill="#99ff99", outline="#00e600", width=5)
        canvas.create_text(x + 15, y + 15, text=label)

    def __draw_circle_ergebnis(self, x, y, label):
        canvas_result.create_oval(x, y, x + 30, y + 30, fill="#00ffff", outline="#00bfff", width=5)
        canvas_result.create_text(x + 15, y + 15, text=label)

    def __draw_circle_tippen(self, x, y, label):
        canvas_tippen.create_oval(x, y, x + 30, y + 30, fill="#99ff99", outline="#00e600", width=5)
        canvas_tippen.create_text(x + 15, y + 15, text=label)


    def __marked_circle(self, x, y, label):
        canvas.create_oval(x, y, x + 30, y + 30, fill="#ff3333", outline="#ff8080", width=5)
        canvas.create_text(x + 15, y + 15, text=label)

    def __marked_circle_ergebnis(self, x, y, label):
        canvas_result.create_oval(x, y, x + 30, y + 30, fill="#ff3333", outline="#ff8080", width=5)
        canvas_result.create_text(x + 15, y + 15, text=label)

    # ------------------------------------------------------------------------

    def __bubble_ergebnis(self):
        xval = 10
        yval = 5
        i = 1
        while i < 7:
            self.__draw_circle_ergebnis(xval, yval, '-')
            yval += 50
            i += 1
        canvas_result.update()

        # ------------------------------------------------------------------------
    # Hier sind die Music Funktionen für jede Buttons angewendet
    def __play_win(self):
        pygame.mixer.music.load('c:/gui/small_win.wav')
        pygame.mixer.music.play(loops=0)

    def __play_lotto_balls(self):
        pygame.mixer.music.load('c:/gui/lotto_ball.mp3')
        pygame.mixer.music.play(loops=1)

    def __play_clean_up(self):
        pygame.mixer.music.load('c:/gui/clean_up.mp3')
        pygame.mixer.music.play(loops=1)

    def __play_goodbye(self):
        pygame.mixer.music.load('c:/gui/woman_bye.mp3')
        pygame.mixer.music.play(loops=0)

        # ------------------------------------------------------------------------
    # von <Beginnen/ Neue Start> Button wird gerufen
    def __bubble(self):
        pygame.mixer.init()
        canvas.delete("all")
        canvas_tippen.delete("all")
        canvas_result.delete("all")
        self.__list_k = []  # Refresh __list_k von letzten gespeichert liste
        self.__text_label.set("Bitte 6 Kugeln auswählen")
        self.__play_lotto_balls()
        xval = 5
        yval = 5
        i = 1
        while i < 50:
            self.__draw_circle(xval, yval, i)
            xval += 50
            if ((i % 7) == 0) and (i < 14):
                i += 1
                xval = 5
                yval = 50
                self.__draw_circle(5, 50, i)
                xval += 50
            elif ((i % 7) == 0) and (i < 21):
                i += 1
                xval = 5
                yval = 100
                self.__draw_circle(xval, yval, i)
                xval += 50
            elif ((i % 7) == 0) and (i < 28):
                i += 1
                xval = 5
                yval = 150
                self.__draw_circle(xval, yval, i)
                xval += 50
            elif ((i % 7) == 0) and (i < 35):
                i += 1
                xval = 5
                yval = 200
                self.__draw_circle(xval, yval, i)
                xval += 50
            elif ((i % 7) == 0) and (i < 42):
                i += 1
                xval = 5
                yval = 250
                self.__draw_circle(xval, yval, i)
                xval += 50
            elif ((i % 7) == 0) and (i < 49):
                i += 1
                xval = 5
                yval = 300
                self.__draw_circle(xval, yval, i)
                xval += 50
            i += 1
        canvas.update()
        # hier Lottoschein (canvas) wird Mouse event anfangen
        canvas.bind("<Button-1>", self.__kugeln_select)

        # -----------------------------------------------------------------------
    # Button <Spielen> wird aufgerufen
    def __lotto_spielen(self):
        pygame.mixer.init()
        self.__bubble_ergebnis()
        self.__play_lotto_balls()

        ziehungen = self.__lottoziehung()
        # Hier rote markierte Kugeln in der Ziehung
        for i in ziehungen:
            xval = kugel_draw[i][0]
            yval = kugel_draw[i][1]
            self.__marked_circle(xval, yval, i)

        # ---------------------------------
        # Nochmal das Ergebnisse and canva_result darstellen
        x = 10
        y = 5
        for i in ziehungen:
            self.__marked_circle_ergebnis(x, y, i)
            y += 50
        canvas_result.update()
        self.__play_win()


        # hier wird die beide eingetippte Liste und Ziehung Liste vergleichen
        count = 0
        list_gewonnen = []
        list_kugel = self.__list_k
        if ziehungen != list_kugel:
            for i in ziehungen:
                if i in list_kugel:
                    count += 1
                    list_gewonnen.append(i)
            if count > 0:
                self.__text_label.set(f"Schade!!! Nur {count} Kugel {list_gewonnen} sind richtig!!")
            else:
                self.__text_label.set("Schade!!! Versuchen nochmal beim näschten Mal!!")
        else:
            self.__text_label.set("Gratulieren!!! Jackpot Gewonnen!!!")
        canvas.unbind("<Button-1>")
        button_2.config(state='disable')
        return ziehungen

        # ------------------------------------------------------------------------

    def __quit(self):
        pygame.mixer.init()
        self.__play_goodbye()
        time.sleep(2)
        self.__fenster.destroy()

    def __stop_game(self):
        button_2.config(state='disable')
        canvas.unbind("<Motion>")
        # self.__list_k = []
        #canvas.config(state='disable')

        pygame.mixer.init()
        canvas.delete("all")
        canvas_tippen.delete("all")
        canvas_result.delete("all")
        self.__text_label.set("Entweder <Beginnen/Neue Start> oder <Exit>")
        self.__play_clean_up()

        button_3.config(state='disable')
        # ------------------------------------------------------------------------

    def fenster_mit_canvas_button(self):
        global canvas
        global canvas_result
        global canvas_tippen
        global button_2
        global button_3
        self.__text_label = tk.StringVar()
        self.__text_label.set("Willkommen zum Lotto 6 aus 49 spielen")
        self.__fenster.title("Lotto 6 aus 49 - Thao Nguyen")

        # -------------------------------------
        canvas = tk.Canvas(self.__fenster,
                           width=350,
                           height=340,
                           bg='#afeeee')
        canvas.grid(row=0, column=0, padx=5, pady=5, columnspan=4)

        # -------------------------------------
        canvas_tippen = tk.Canvas(self.__fenster, width=50, height=340, bg='#afeeee')
        canvas_tippen.grid(row=0, column=4, padx=5, pady=5, columnspan=1)

        # -------------------------------------
        canvas_result = tk.Canvas(self.__fenster, width=50, height=340, bg='#afeeee')
        canvas_result.grid(row=0, column=5, padx=5, pady=5, columnspan=1)

        # -------------------------------------
        text_inform = tk.Label(self.__fenster, textvariable=self.__text_label, font=("Arial", 10), fg="#0000ff")
        text_inform.grid(row=1, column=0, padx=5, pady=5, columnspan=4, sticky="w")
        # -------------------------------------
        button_1 = tk.Button(self.__fenster,
                             text="Beginnen/ Neue Start",
                             width=16,
                             command=self.__bubble)
        button_1.grid(row=2, column=0, sticky="w", columnspan=1)
        # -------------------------------------
        button_2 = tk.Button(self.__fenster,
                             text="Spielen",
                             width=10,
                             command=self.__lotto_spielen)
        button_2.grid(row=2, column=1, sticky="w", columnspan=1)
        button_2.config(state='disable')
        # -------------------------------------
        button_3 = tk.Button(self.__fenster,
                             text="Ausräumen",
                             width=10,
                             command=self.__stop_game)
        button_3.grid(row=2, column=2, sticky="w", columnspan=1)
        button_3.config(state='disable')
        # -------------------------------------
        button_4 = tk.Button(self.__fenster,
                             text="Exit",
                             width=10,
                             command=self.__quit)

        button_4.grid(row=2, column=3, sticky="w", columnspan=1)
        # -------------------------------------
        lbl_1 = tk.Label(self.__fenster, text="Eingetippt", font=("Arial", 8))
        lbl_1.grid(row=2, column=4, padx=5, pady=5, ipadx=15, ipady=10, sticky='w', columnspan=1)
        # -------------------------------------
        lbl_2 = tk.Label(self.__fenster, text="Ergebnis", font=("Arial", 8))
        lbl_2.grid(row=2, column=5, padx=5, pady=5, ipadx=5, ipady=5, sticky='w', columnspan=1)
        # canvas.mainloop()
        # canvas_result.mainloop()
        self.__fenster.mainloop()
        # ==========================================================================================

def graphik_lotto():
    g = Graphik()
    g.fenster_mit_canvas_button()

# ======================================================================================================

if (__name__ == "__main__"):
    graphik_lotto()
