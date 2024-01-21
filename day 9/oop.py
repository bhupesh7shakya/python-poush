class House:
    def __init__(self, window=10, color="yellow", door=3):
        self.window = window
        self.color = color
        self.door = door

    def ghar(self):
        color = "green"
        print('mero ghar ko color', self.color)

    def set_color(self, color):
        self.color = color


# ram_ko_ghar = House()
# ram_ko_ghar.color = "yellow"


# print(ram_ko_ghar.color)
binit = House(color='black')
# binit.set_color("yellow")
print(binit.color)
binit.ghar()

# binita = House()
# binita.color = "green"
# print(binita.color)
