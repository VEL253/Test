#создаём класс портфель и вносим в него СВОЙСТВА.
#Так же объект состоит из данных, которые можно отдельно назвать. Например, в портфеле можно выделить: сам портфель, книги, что хранятся в нём, материал, из чего состоит портфель и т.д.
#Так же выделяют несколько видов программирования: Процедурное, которое понимает сама машина. Декларативное, в котором в приоритете стоит сама задача, а способ её исполнения второстепенен. Функциональное, которое оперирует самими функциями. Логическое, которое работает с простой математической логикой. Динамическое, в котором удобно минимизировать кол-во циклов исполнения и графическое, которое работает напрямую с изображением.
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
