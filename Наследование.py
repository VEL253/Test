class Bags():
    def __init__(self, color, brand):
        self.color=color
        self.brand=brand
    def info(self):
        return f"Это {self.color} портфель от бренда {self.brand}!"

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
        return f"Это {self.color} портфель от бренда {self.brand}, принадлежащий {self.name} с возрастом в {self.age} лет."#Так компания подтверждает данные пользователя.
B=Bags_owner('салатовый','puma','Василий','29')
print(B.info())#Итак, в случае пропажи портфеля вы легко сможете его вернуть, предъявив данные компании, чтобы она сверилась с введённые вами ранее!
