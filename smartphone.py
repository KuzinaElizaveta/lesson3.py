# Конструктор должен принимать на вход следующие параметры:

# - марка телефона,
# - модель телефона,
# - абонентский номер (”+79…”).

class Smartphone:
    def __init__(self, marka, model, number):         
        self.marka = marka
        self.model = model
        self.number = number

ph = Smartphone ("Iphone", "XS", "+79112223344")
print(ph.marka)
print(ph.model)
print(ph.number)
