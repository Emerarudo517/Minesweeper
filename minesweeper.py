import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master, size=10, mines=10):
        self.master = master
        self.size = size
        self.mines = mines
        self.flags = 0
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[' ' for _ in range(size)] for _ in range(size)]
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self.place_mines()
        self.calculate_numbers()
        self.create_widgets()

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in self.mine_positions:
                self.mine_positions.add((x, y))
                self.board[x][y] = 'M'

    def calculate_numbers(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 'M':
                    continue
                count = 0
                for i in range(max(0, x - 1), min(self.size, x + 2)):
                    for j in range(max(0, y - 1), min(self.size, y + 2)):
                        if self.board[i][j] == 'M':
                            count += 1
                self.board[x][y] = str(count)

    def create_widgets(self):
        control_frame = tk.Frame(self.master)
        control_frame.grid(row=0, column=0, columnspan=self.size, sticky='we')
        
        restart_button = tk.Button(control_frame, text="Chơi lại", command=self.restart_game)
        restart_button.pack(side=tk.LEFT)
        
        return_button = tk.Button(control_frame, text="Quay về Menu", command=self.return_to_menu)
        return_button.pack(side=tk.LEFT, padx=10)
        
        self.flag_label = tk.Label(control_frame, text=f"Cờ: {self.flags}")
        self.flag_label.pack(side=tk.LEFT, padx=10)
        
        self.mine_label = tk.Label(control_frame, text=f"Mìn: {self.mines - self.flags}")
        self.mine_label.pack(side=tk.LEFT, padx=10)

        game_frame = tk.Frame(self.master)
        game_frame.grid(row=1, column=0, columnspan=self.size, sticky='we')
        
        for x in range(self.size):
            for y in range(self.size):
                button = tk.Button(game_frame, width=2, height=1, command=lambda x=x, y=y: self.reveal_cell(x, y), borderwidth=0)
                button.bind('<Button-3>', lambda e, x=x, y=y: self.mark_mine(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button
                self.set_button_color(x, y, opened=False)

    def set_button_color(self, x, y, opened):
        if opened:
            color1, color2 = '#d8b99d', '#e7c4a2'
        else:
            color1, color2 = '#a5d95d', '#9dd356'
        self.buttons[x][y].config(bg=color1 if (x + y) % 2 == 0 else color2)

    def reveal_cell(self, x, y):
        if self.board[x][y] == 'M':
            self.buttons[x][y].config(text='💣', bg='red')
            self.game_over()
            return
        self.revealed[x][y] = self.board[x][y]
        text = self.board[x][y] if self.board[x][y] != '0' else ''
        self.buttons[x][y].config(text=text, state='disabled', disabledforeground=self.get_color(self.board[x][y]))
        self.set_button_color(x, y, opened=True)
        if self.board[x][y] == '0':
            for i in range(max(0, x - 1), min(self.size, x + 2)):
                for j in range(max(0, y - 1), min(self.size, y + 2)):
                    if self.revealed[i][j] == ' ':
                        self.reveal_cell(i, j)
        if self.check_win():
            self.win_game()

    def mark_mine(self, x, y):
        if self.revealed[x][y] != ' ':
            return
        if self.buttons[x][y]['text'] == '🚩':
            self.buttons[x][y].config(text='')
            self.flags -= 1
        else:
            self.buttons[x][y].config(text='🚩', fg='red')
            self.flags += 1
        self.update_labels()

    def update_labels(self):
        self.flag_label.config(text=f"Flags: {self.flags}")
        self.mine_label.config(text=f"Mines: {self.mines - self.flags}")

    def check_win(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.revealed[x][y] == ' ' and self.board[x][y] != 'M':
                    return False
        return True

    def game_over(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 'M':
                    self.buttons[x][y].config(text='💣', bg='red')
        messagebox.showinfo("Game Over", "Bạn dẫm phải mìn rồi, gà quá!!")

    def win_game(self):
        response = messagebox.askquestion("Congratulation", "Bạn đã thắng!! :3 Bạn có muốn chơi tiếp không?")
        if response == 'yes':
            self.restart_game()
        else:
            self.master.quit()

    def restart_game(self):
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.revealed = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.mine_positions = set()
        self.flags = 0
        self.place_mines()
        self.calculate_numbers()
        for x in range(self.size):
            for y in range(self.size):
                self.buttons[x][y].config(text='', state='normal')
                self.set_button_color(x, y, opened=False)
        self.update_labels()

    def return_to_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        from menu import show_menu
        show_menu(self.master)

    def get_color(self, value):
        colors = {
            '1': 'blue',
            '2': 'green',
            '3': 'red',
            '4': 'darkblue',
            '5': 'darkred',
            '6': 'cyan',
            '7': 'black',
            '8': 'gray'
        }
        return colors.get(value, 'black')