class Bags():
    def __init__(self, color, brand):
        self.color=color
        self.brand=brand
    def info(self):
        print(f"Это {self.color} портфель от бренда {self.brand}!")

A=Bags('салатовый','puma')#Однажды вы приобрели порфель.
A.info()#Заполнив на сайте его данные, вам чего-то не хватало.
#Вы захотели заклеймить портфель, введя свои имя и возраст в программу.
#Вы подумали и написали для этого следущий код:

class Bags_owner(Bags):
    def __init__(self, color, brand, name, age):#Добавили имя и возраст
        super().__init__(color, brand)
        self.name=name
        self.age=age
    def info(self):
        print(f"Это {self.color} портфель от бренда {self.brand}, принадлежащий {self.name} с возрастом в {self.age} лет.")#Так компания подтверждает данные пользователя, но и злоумышленники смогут так получить данные пользователя.

#Вот незадача. Вдруг, кто-то захочет узнать данные пользователя?
#Подумав, для решения этой проблемы вы модернизировали программу и предложили бренду дополнить сайт, на что бренд, конечно же, согласился.


class Bags_owner(Bags):
    def __init__(self, color, brand, name, age):
        super().__init__(color, brand)
        self.name=name
        self.age=age
    def __info(self):#Благодаря вашим усилиям, вы поможете многим пользователям!
        print(f"Это {self.color} портфель от бренда {self.brand}, принадлежащий {self.name} с возрастом в {self.age} лет.")

B=Bags_owner('салатовый','puma','Василий','29')
B.__info()#В классе "B" пропускается наличие __info и выводится ошибка об отсутствии этого метода. Благодаря этому, данные скрыты! Все спасены!
