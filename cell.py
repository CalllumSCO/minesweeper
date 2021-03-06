from tkinter import Button
import settings
import random

class Cell:
    all = []

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        # Append cell to list
        Cell.all.append(self)

    def create_button_object(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_obj = btn


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost!
        self.cell_btn_obj.configure(bg='red')
    
    def get_cell_by_axis(self, x, y):
        # Return a cell based on axis
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        self.cell_btn_obj.configure(text=self.surrounded_cells_mines_length)

    def right_click_actions(self, event):
        print(event)
        print("I have been right clicked")
    
    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
