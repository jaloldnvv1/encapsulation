import uuid


class Avto:
    def __init__(self, model, year, color):
        self.__id = uuid.uuid4()
        self.model = model
        self.year = year
        self.color = color
        self.__km = 0

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id


a = Avto("Mala", 2024, "Black")
print(a.get_id())
