from tkinter import Tk, Canvas, Button, messagebox, Label, Entry, Scale, HORIZONTAL, IntVar, StringVar
from math import floor
from Board import Board
from Generator import Generator


class App:

    def __init__(self, x_cell, y_cell, size_cell, tolerance, speed):

        self.start = False
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.size_cell = size_cell
        self.tolerance = tolerance
        self.speed = speed
        self.toggle_state = True

        # Widgets

        self.root = Tk()
        self.canvas = Canvas(self.root, height=self.x_cell*self.size_cell, width=self.y_cell*self.size_cell)
        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.btn_start = Button(self.root, text="Stop/Start", command=self.toggle_start)
        self.btn_close = Button(self.root, text="Exit", command=self.close)
        self.btn_reset = Button(self.root, text="Reset", command=self.reset)

        self.lb_x_cell = Label(self.root, text="Cells X : ")
        self.ib_x_cell_str_var = StringVar()
        self.ib_x_cell_str_var.set(str(self.x_cell))
        self.ib_x_cell = Entry(self.root, textvariable=self.ib_x_cell_str_var)

        self.lb_y_cell = Label(self.root, text="Cells Y : ")
        self.ib_y_cell_str_var = StringVar()
        self.ib_y_cell_str_var.set(str(self.y_cell))
        self.ib_y_cell = Entry(self.root, textvariable=self.ib_y_cell_str_var)

        self.lb_size_cell = Label(self.root, text="Cell size : ")
        self.ib_size_cell_str_var = StringVar()
        self.ib_size_cell_str_var.set(str(self.size_cell))
        self.ib_size_cell = Entry(self.root, textvariable=self.ib_size_cell_str_var)

        self.lb_speed = Label(self.root, text="Speed : ")
        self.sc_speed_int_var = IntVar()
        self.sc_speed_int_var.set(self.speed)
        self.sc_speed = Scale(self.root,
                              orient=HORIZONTAL,
                              from_=300,
                              to=50,
                              showvalue=0,
                              variable=self.sc_speed_int_var,
                              command=self.on_speed_changed)

        # Layout
        self.root.columnconfigure(0, weight=self.x_cell*self.size_cell)
        self.root.rowconfigure(0, weight=self.y_cell*self.size_cell)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=5)

        self.btn_start.grid(row=5, column=0, sticky="W")
        self.btn_reset.grid(row=5, column=1, sticky="W")
        self.btn_close.grid(row=5, column=2, sticky="W")

        self.lb_x_cell.grid(row=1, column=3, sticky="W")
        self.ib_x_cell.grid(row=1, column=4, sticky="E")

        self.lb_y_cell.grid(row=2, column=3, sticky="W")
        self.ib_y_cell.grid(row=2, column=4, sticky="E")

        self.lb_size_cell.grid(row=3, column=3, sticky="W")
        self.ib_size_cell.grid(row=3, column=4, sticky="E")

        self.lb_speed.grid(row=4, column=3, sticky="SW")
        self.sc_speed.grid(row=4, column=4, sticky="E")

        # Init
        self.board = Board(self.x_cell, self.y_cell, self.tolerance)
        self.pixels = self.init_board()
        self.update_board()
        self.root.after(10, self.refresh)
        self.root.mainloop()

    def init_board(self):
        pixels = []
        for cell in self.board.cells:
            color = "white"
            pixels.append(self.canvas.create_rectangle(cell.c_x*self.size_cell,
                                                     cell.c_y*self.size_cell,
                                                     self.size_cell+(self.size_cell*cell.c_x),
                                                     self.size_cell+(self.size_cell*cell.c_y),
                                                     tags="#"+str(cell.c_x)+"#"+str(cell.c_y),
                                                     fill=color))
        return pixels

    def update_board(self):
        for cell in self.board.cells:
            color = "yellow" if cell.state else "grey"
            self.canvas.itemconfigure("#"+str(cell.c_x)+"#"+str(cell.c_y), fill=color)

    def refresh(self):
        if self.start:
            self.update_board()
            self.board.nextgen()
            self.root.after(self.speed, self.refresh)

    def toggle_start(self):
        if self.start:
            self.start = False
        else:
            self.start = True
            self.refresh()

    def close(self):
        if self.start:
            self.toggle_start()
        result = messagebox.askokcancel("Question?", "Do you want quit?")
        if result:
            self.root.quit()
        else:
            self.toggle_start()

    def reset(self):
        self.x_cell = int(self.ib_x_cell_str_var.get())
        self.y_cell = int(self.ib_y_cell_str_var.get())
        self.size_cell = int(self.ib_size_cell_str_var.get())
        self.board = Board(self.x_cell, self.y_cell, self.tolerance, Generator.Blank)
        self.canvas.destroy()
        self.create_canvas()
        self.pixels = self.init_board()
        self.update_board()
        self.refresh()

    def on_speed_changed(self):
        pass

    def toggle_cell(self, event):
        self.toggle_state = False
        x, y = event.x, event.y
        x_cell, y_cell = int(floor(x / self.size_cell)), int(floor(y / self.size_cell))
        if x_cell in range(self.x_cell) and y_cell in range(self.y_cell):
            cell = self.board.getcelltocoord(x_cell, y_cell)
            color = "grey" if cell.state else "yellow"
            self.board.getcelltocoord(x_cell, y_cell).state = False if cell.state else True
            self.canvas.itemconfigure("#" + str(cell.c_x) + "#" + str(cell.c_y), fill=color)

    def create_canvas(self):
        self.canvas = Canvas(self.root, height=self.x_cell * self.size_cell, width=self.y_cell * self.size_cell)
        self.canvas.bind("<Button-1>", self.toggle_cell)
        # Layout
        self.root.columnconfigure(0, weight=self.x_cell * self.size_cell)
        self.root.rowconfigure(0, weight=self.y_cell * self.size_cell)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=5)

