class Attack:
    def __init__(self, village, lid, troops):
        self.__village = village
        self.__lid = lid
        self.__troops = troops

    @property
    def lid(self):
        return self.__lid

    @lid.setter
    def age(self, lid):
        self.__lid = lid

    @property
    def village(self):
        return self.__village

    @village.setter
    def age(self, village):
        self.__village = village @ property

    @property
    def troops(self):
        return self.__troops

    @troops.setter
    def age(self, troops):
        self.__troops = troops

    def __str__(self):
        return f"sendRequest({self.village.x}, {self.village.y}, {self.lid}, {self.troops});"
