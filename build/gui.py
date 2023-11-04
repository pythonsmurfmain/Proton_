from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Chatbot\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1147x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1147,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    573.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    710.5,
    254.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#ffffff",
    fg="#ffffff",
    highlightthickness=0
)
entry_1.place(
    x=377.0,
    y=98.0,
    width=667.0,
    height=311.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    661.5,
    518.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#000000",
    fg="#ffffff",
    highlightthickness=0
)
entry_2.place(
    x=384.0,
    y=494.0,
    width=555.0,
    height=46.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=995.0,
    y=473.0,
    width=98.0,
    height=92.0
)
window.resizable(False, False)
window.mainloop()
