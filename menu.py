import tkinter as tk
from minesweeper import Minesweeper
from utils import center_window

def show_menu(master):
    for widget in master.winfo_children():
        widget.destroy()
    
    master.geometry("688x230")
    master.resizable(False, False)
    
    canvas = tk.Canvas(master, width=688, height=230)
    canvas.pack(fill="both", expand=True)
    
    bg_image = tk.PhotoImage(file="Background.png")
    canvas.create_image(0, 0, anchor="nw", image=bg_image)
    
    title = tk.Label(master, text="Minesweeper", font=("Helvetica", 24), bg="#ffffff")
    canvas.create_window(344, 50, window=title)
    
    subtitle = tk.Label(master, text="Thực hiện: Nhóm 16", font=("Helvetica", 12), bg="#ffffff")
    canvas.create_window(344, 90, window=subtitle)
    
    play_button = tk.Button(master, text="Chơi thôi", command=lambda: show_difficulty_selection(master))
    canvas.create_window(244, 180, window=play_button)
    
    exit_button = tk.Button(master, text="Thoát", command=master.quit)
    canvas.create_window(444, 180, window=exit_button)
    
    master.bg_image = bg_image
def show_difficulty_selection(master):
    for widget in master.winfo_children():
        widget.destroy()
    
    master.geometry("688x230")
    master.resizable(False, False)
    
    canvas = tk.Canvas(master, width=688, height=230)
    canvas.pack(fill="both", expand=True)
    
    bg_image = tk.PhotoImage(file="Background.png")
    canvas.create_image(0, 0, anchor="nw", image=bg_image)
    
    title = tk.Label(master, text="Chọn độ khó", font=("Helvetica", 18), bg="#ffffff")
    canvas.create_window(344, 50, window=title)
    
    easy_button = tk.Button(master, text="Dễ", command=lambda: start_game(master, size=6, mines=6))
    canvas.create_window(100, 100, window=easy_button)
    
    medium_button = tk.Button(master, text="Thường", command=lambda: start_game(master, size=12, mines=24))
    canvas.create_window(100, 130, window=medium_button)
    
    hard_button = tk.Button(master, text="Khó", command=lambda: start_game(master, size=24, mines=96))
    canvas.create_window(100, 160, window=hard_button)
    
    master_button = tk.Button(master, text="💀💀💀", command=lambda: start_game(master, size=32, mines=256))
    canvas.create_window(100, 190, window=master_button)
    
    master.bg_image = bg_image

def start_game(master, size, mines):
    for widget in master.winfo_children():
        widget.destroy()
    game = Minesweeper(master, size=size, mines=mines)
    adjust_window_size(master, size)

def adjust_window_size(master, size):
    button_size = 30
    control_height = 50
    window_width = size * button_size
    window_height = size * button_size + control_height
    
    if size == 6:
        window_width += 160
        window_height -= 72
    elif size == 12:
        window_width -= 60
        window_height -= 120
    elif size == 24:
        window_width -= 240
        window_height -= 216
    elif size == 32:
        window_width -= 320
        window_height -= 280
    
    master.geometry(f"{window_width}x{window_height}")
    master.resizable(False, False)
    center_window(master)