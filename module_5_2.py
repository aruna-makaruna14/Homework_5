class House:

    def __init__(self, name, number_of_floor):
       self.name = name
       self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floor:
            for floor in range (1, new_floor + 1):
                print(floor)
            else:
                print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"

h1 = House('ЖК Эльбррус', 10)
h2 = House('Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
