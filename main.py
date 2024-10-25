import tkinter as tk
from menu import show_menu
from utils import center_window

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    center_window(root, 688, 230)
    root.resizable(False, False)
    show_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()