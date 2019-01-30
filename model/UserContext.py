from PyQt5.Qt import QColor


class UserContext:

    def __init__(self, x_cell, y_cell, size_cell, density, speep, inactive_color, active_color, new_color):
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.density = density
        self.speed = speep
        self.size_cell = size_cell
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.new_color = new_color

    def __str__(self):
        ret="["
        for attr, val  in self.__dict__.items():
            ret += attr
            ret += "="
            if isinstance(val,QColor):
                ret += val.name().__str__()+";"
            else:
                ret += "None;" if val is None else str(val)+";"
        ret += "]"
        return ret

