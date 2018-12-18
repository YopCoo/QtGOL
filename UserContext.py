from PyQt5.Qt import QColor


class UserContext():
    def __init__(self):
        file = open("config.ini", "r")
        for line in file:
            key = line.split("=")[0].strip()
            val = line.split("=")[1]
            if "XCELL" == key:
                self.x_cell = int(val)
            elif "YCELL" == key:
                self.y_cell = int(val)
            elif "DENSITY" == key:
                self.density = float(val)
            elif "SPEED" == key:
                self.speed = int(val)
            elif "SIZECELL" == key:
                self.size_cell = int(val)
            elif "INACTIVE_COLOR" == key:
                rgb = val.split(',')
                self.inactive_color = QColor.fromRgb(int(rgb[0].strip()),int(rgb[1].strip()),int(rgb[2].strip()))
            elif "ACTIVE_COLOR" == key:
                rgb = val.split(',')
                self.active_color = QColor.fromRgb(int(rgb[0].strip()), int(rgb[1].strip()), int(rgb[2].strip()))
