#создаём класс портфель и вносим в него СВОЙСТВА.
class Bag():
    #создаём класс портфель
    def __init__(self, color, len_book):
        #записываем СВОЙСТВА данных(цвет и вместимость)
        self.color=color
        self.len_book=len_book
    def types(self):
        print(f"Ваш портфель имеет {self.color} цвет.")
        print(f"Ваш портфель имеет вместимость в {self.len_book} книг.")
class School(Bag):
    def __init__(self, color, len_book, int_book):
        #создаём наследственный класс
        super().__init__(color, len_book)
        self.int_book=int_book
