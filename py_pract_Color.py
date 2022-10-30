class Color:

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __eq__(self, other):
        tuple_self = (self.red, self.green, self.blue)
        tuple_other = (other.red, other.green, other.blue)
        return tuple_self == tuple_other

    def __str__(self):
        return (f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}')


    def __add__(self, other):
        self.add_red = min(255, (self.red + other.red))
        self.add_green = min(255, (self.green + other.green))
        self.add_blue = min(255, (self.blue + other.blue))
        return type(self)(self.add_red, self.add_green, self.add_blue)


    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        new_colors = []
        for color in self.red, self.green, self.blue:
            cl = -256 * (1 - c)
            F = (259 * (cl + 255))/(255 * (259 - cl))
            L = int(F * (color - 128) + 128)
            new_colors.append(L)
        return Color(*new_colors)

    __rmul__ = __mul__


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(0.3 * red)
    print(red * 0.6)



