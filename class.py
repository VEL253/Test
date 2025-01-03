class Bags():#Определяем класс.
    def __init__(self, color, brand):#Метод (а тут всё относится к свойствам).
        self.color=color#Эта и след. строка -- есть ссылки на color и brand. Остальное в этом классе относится к методу.
        self.brand=brand
    def info(self):
        print(f"Это {self.color} портфель от бренда {self.brand}!")
