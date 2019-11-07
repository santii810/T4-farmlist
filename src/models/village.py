from src.utils import calculator, setup_values


class Village:
    def __init__(self, x, y, natare):
        self.__x = int(x)
        self.__y = int(y)
        self.__natare = natare
        self.__dist = calculator.calcular_distancia(setup_values.vill14_coords, [self.x, self.y])

    @property
    def x(self):
        return self.__x

    @x.setter
    def age(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def age(self, y):
        self.__y = y

    @property
    def dist(self):
        return self.__dist

    @dist.setter
    def age(self, dist):
        self.__dist = dist

    @property
    def natare(self):
        return self.__natare

    @natare.setter
    def age(self, natare):
        self.__natare = natare

    def __str__(self):
        return f"({self.x}|{self.y}) \t {round(self.dist, 1)}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o: object):
        return o.x == self.x and o.y == self.y

    def __hash__(self) -> int:
        return super().__hash__()

    def __lt__(self, other):
        return self.dist < other.dist
