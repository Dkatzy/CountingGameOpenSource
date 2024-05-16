import tkinter as tk
import random

#frame variables and creation
tk_root = tk.Tk()
tk_width, tk_height = tk_root.winfo_screenwidth(), tk_root.winfo_screenheight()
tk_canvas = tk.Canvas(tk_root, width=tk_width, height=tk_height, bg="white")
tk_canvas.pack()

#creating addition sprite
plus_size = 20
plus_x = 300
plus_y = 200
tk_plus = [
    tk_canvas.create_line(plus_x - plus_size, plus_y, plus_x + plus_size, plus_y, width=10, fill="black"),
    tk_canvas.create_line(plus_x, plus_y - plus_size, plus_x, plus_y + plus_size, width=10, fill="black")
]

#rectangle and rectangle label
rect_size = 50
number = 0
tk_rect = tk_canvas.create_rectangle(50, 50, 50 + rect_size, 50 + rect_size, fill="blue")
tk_rect_text = tk_canvas.create_text(75, 75, text="0", font=("Arial", 20), fill="white")

# Function to check if the rectangle and plus are touching
def check_is_touching_plus():
    rect_coords = tk_canvas.coords(tk_rect)
    rect_left = rect_coords[0]
    rect_top = rect_coords[1]
    rect_right = rect_coords[2]
    rect_bottom = rect_coords[3]
    
    plus_left = plus_x - plus_size
    plus_top = plus_y - plus_size
    plus_right = plus_x + plus_size
    plus_bottom = plus_y + plus_size
    
    if (rect_right > plus_left and
        rect_left < plus_right and
        rect_bottom > plus_top and
        rect_top < plus_bottom):
        return True
    return False

def tk_move_plus():
    global plus_x, plus_y
    plus_x = random.randint(plus_size, tk_width - 2 * plus_size)
    plus_y = random.randint(plus_size, tk_height - 2 * plus_size)
    tk_canvas.coords(tk_plus[0], plus_x - plus_size, plus_y, plus_x + plus_size, plus_y)
    tk_canvas.coords(tk_plus[1], plus_x, plus_y - plus_size, plus_x, plus_y + plus_size)

#moving sprite with arrow key input
def tk_move_rectangle(event):
    if event.keysym == 'Up':
        tk_canvas.move(tk_rect, 0, -10)
        tk_canvas.move(tk_rect_text, 0, -10)
    elif event.keysym == 'Down':
        tk_canvas.move(tk_rect, 0, 10)
        tk_canvas.move(tk_rect_text, 0, 10)
    elif event.keysym == 'Left':
        tk_canvas.move(tk_rect, -10, 0)
        tk_canvas.move(tk_rect_text, -10, 0)
    elif event.keysym == 'Right':
        tk_canvas.move(tk_rect, 10, 0)
        tk_canvas.move(tk_rect_text, 10, 0)

    #logic check forthe two sprites checking
    if check_is_touching_plus():
        #update number
        global number
        number += 1
        tk_canvas.itemconfigure(tk_rect_text, text=str(number))

        #move plus sign to a random location
        tk_move_plus()


    

# Bind arrow keys to the move_rectangle function
tk_root.bind('<Up>', tk_move_rectangle)
tk_root.bind('<Down>', tk_move_rectangle)
tk_root.bind('<Left>', tk_move_rectangle)
tk_root.bind('<Right>', tk_move_rectangle)


#main loop
tk_root.mainloop()