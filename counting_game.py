import tkinter as tk
import random

class Frame:
    def __init__(self):
        #frame variables and creation
        self.tk_root = tk.Tk()

        global tk_width, tk_height 
        tk_width, tk_height = self.tk_root.winfo_screenwidth(), self.tk_root.winfo_screenheight()
        self.tk_canvas = tk.Canvas(self.tk_root, width=tk_width, height=tk_height, bg="white")
        self.tk_canvas.pack()

class Plus_sign:
    def __init__(self, frame):
        #creating addition sprite
        self.plus_size = 20
        self.plus_x = 300
        self.plus_y = 200
        self.tk_plus = [
            frame.tk_canvas.create_line(self.plus_x - self.plus_size, self.plus_y, self.plus_x + self.plus_size, self.plus_y, width=10, fill="black"),
            frame.tk_canvas.create_line(self.plus_x, self.plus_y - self.plus_size, self.plus_x, self.plus_y + self.plus_size, width=10, fill="black")
        ]
    
    def tk_move_plus(self, frame):
        self.plus_x = random.randint(self.plus_size, tk_width - 2 * self.plus_size)
        self.plus_y = random.randint(self.plus_size, tk_height - 2 * self.plus_size)
        frame.tk_canvas.coords(self.tk_plus[0], self.plus_x - self.plus_size, self.plus_y, self.plus_x + self.plus_size, self.plus_y)
        frame.tk_canvas.coords(self.tk_plus[1], self.plus_x, self.plus_y - self.plus_size, self.plus_x, self.plus_y + self.plus_size)

class Rectangle:
    def __init__(self, frame):
        #rectangle and rectangle label
        self.rect_size = 50
        self.number = 0
        self.tk_rect = frame.tk_canvas.create_rectangle(0, 0, self.rect_size, self.rect_size, fill="blue")
        self.tk_rect_text = frame.tk_canvas.create_text(25, 25, text="0", font=("Arial", 20), fill="white")
    
    def tk_move_left(self, frame):
        frame.tk_canvas.move(self.tk_rect, -10, 0)
        frame.tk_canvas.move(self.tk_rect_text, -10, 0)
    
    def tk_move_right(self, frame):
        frame.tk_canvas.move(self.tk_rect, 10, 0)
        frame.tk_canvas.move(self.tk_rect_text, 10, 0)

    def tk_move_up(self, frame):
        frame.tk_canvas.move(self.tk_rect, 0, -10)
        frame.tk_canvas.move(self.tk_rect_text, 0, -10)

    def tk_move_down(self, frame):
        frame.tk_canvas.move(self.tk_rect, 0, 10)
        frame.tk_canvas.move(self.tk_rect_text, 0, 10)

class Exit_button:
    def __init__(self, frame):
        #create an exit button
        self.exit_button = tk.Button(frame.tk_root, text="Exit", command=self.exit)
        self.tk_frame = frame
        self.exit_button.pack()
        self.exit_button_window = frame.tk_canvas.create_window(tk_width / 2, 20, anchor=tk.CENTER, window=self.exit_button)

    def exit(self):
        self.tk_frame.tk_root.destroy()
    


class Game_logic:
    # def __innit__(self, frame, rect, plus):
    #     self.tk_frame = frame
    #     self.tk_rect = rect
    #     self.tk_plus = plus

    def __init__(self):
        self.tk_frame = Frame()
        self.tk_exit_btn = Exit_button(self.tk_frame)
        self.tk_rect = Rectangle(self.tk_frame)
        self.tk_plus = Plus_sign(self.tk_frame)
    
    def check_is_touching_plus(self):
        rect_coords = self.tk_frame.tk_canvas.coords(self.tk_rect.tk_rect)
        rect_left = rect_coords[0]
        rect_top = rect_coords[1]
        rect_right = rect_coords[2]
        rect_bottom = rect_coords[3]
        
        plus_left = self.tk_plus.plus_x - self.tk_plus.plus_size
        plus_top = self.tk_plus.plus_y - self.tk_plus.plus_size
        plus_right = self.tk_plus.plus_x + self.tk_plus.plus_size
        plus_bottom = self.tk_plus.plus_y + self.tk_plus.plus_size
        
        if (rect_right > plus_left and
            rect_left < plus_right and
            rect_bottom > plus_top and
            rect_top < plus_bottom):
            return True
        return False
    
    #moving sprite with arrow key input
    def tk_move_rectangle(self, event):
        if event.keysym == 'Up':
            self.tk_rect.tk_move_up(self.tk_frame)
        elif event.keysym == 'Down':
            self.tk_rect.tk_move_down(self.tk_frame)
        elif event.keysym == 'Left':
            self.tk_rect.tk_move_left(self.tk_frame)
        elif event.keysym == 'Right':
            self.tk_rect.tk_move_right(self.tk_frame)
        #logic check forthe two sprites checking
        if self.check_is_touching_plus():
            #update number
            self.tk_rect.number += 1
            self.tk_frame.tk_canvas.itemconfigure(self.tk_rect.tk_rect_text, text=str(self.tk_rect.number))

            #move plus sign to a random location
            self.tk_plus.tk_move_plus(self.tk_frame)

    def start_new_game(self):
        # Bind arrow keys to the move_rectangle function
        self.tk_frame.tk_root.bind('<Up>', self.tk_move_rectangle)
        self.tk_frame.tk_root.bind('<Down>', self.tk_move_rectangle)
        self.tk_frame.tk_root.bind('<Left>', self.tk_move_rectangle)
        self.tk_frame.tk_root.bind('<Right>', self.tk_move_rectangle)

        #main loop
        self.tk_frame.tk_root.mainloop()

new_game = Game_logic()
new_game.start_new_game()
