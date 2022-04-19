from tkinter import *
from cell import Cell
import settings
import util


root = Tk()

#Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black', # Change to black later
    width=1440,
    height=util.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='black',
    width=util.width_prct(25),
    height=settings.HEIGHT - util.height_prct(25)

)

left_frame.place(x=0, y=util.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=util.width_prct(75),
    height=util.height_prct(75) 
)

center_frame.place(x = util.width_prct(25), y = util.height_prct(25))

for x in range(settings.ROWS):
    for y in range(settings.COLUMNS):
        cell = Cell(x,y)
        cell.create_button_object(center_frame)

        cell.cell_btn_obj.grid(
            column = y,
            row = x
        )

Cell.randomise_mines()

#Run the window
root.mainloop()