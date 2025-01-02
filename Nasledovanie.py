class Bags():#Определяем класс.
    def __init__(self, color, brand):#Метод (а тут всё относится к свойствам).
        self.color=color#Эта и след. строка -- есть ссылки на color и brand. Остальное в этом классе относится к методу.
        self.brand=brand
    def info(self):
        print(f"Это {self.color} портфель от бренда {self.brand}!")
class Bags_owner(Bags):#Нам необходимо добавить имя и возраст, чтобы определить владельца портфеля, но вмешиваться в class Bags нельзя. В таком случае воспользуемся наследованием.
    def __init__(self, color, brand, name, age):
        super().__init__(color, brand)
        self.name=name
        self.age=age
    def info(self):
        print(f"Это {self.color} портфель от бренда {self.brand}, принадлежащий {self.name}.")
