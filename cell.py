from tkinter import Button

class Cell:
    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None

    def create_button_object(self, location):
        btn = Button(
            location,
            text = 'Text'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        print(event)
        print("I have been left clicked")

    def right_click_actions(self, event):
        print(event)
        print("I have been right clicked")