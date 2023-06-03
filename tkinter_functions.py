import tkinter as tk
from tkinter import ttk

import csv_functions as csv

header_text = "Set List App"

setlist_dict = csv.getRandomSongDict()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Setlist App")

        # the geometry preperation bit:
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 600
        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()
        CENTER_X = int(SCREEN_WIDTH / 2 - WINDOW_WIDTH / 2)
        CENTERY_Y = int(SCREEN_HEIGHT / 2 - WINDOW_HEIGHT / 2)
        GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{CENTER_X}+{CENTERY_Y}"
        # end of the geometry preperation bit

        self.geometry(GEOMETRY)

        # header section
        self.header = tk.Label(self, text=header_text)
        self.header.pack()

        # output section
        self.output = tk.Label(self)
        self.output.pack()

        # btn placement section
        self.btn_container = ttk.Frame()
        self.btn_container.pack()

        # btn section

        # give random song btn with complete information

        self.random_song_btn = ttk.Button(
            self.btn_container, text="Give random song!", command=self.handle_click
        )
        self.random_song_btn.pack()

    def handle_click(self):
        self.output["text"] = csv.wholeString(setlist_dict)
