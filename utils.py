def center_window(root, width=None, height=None):
    if width and height:
        root.geometry(f'{width}x{height}')
    root.update_idletasks()
    width = width or root.winfo_width()
    height = height or root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')