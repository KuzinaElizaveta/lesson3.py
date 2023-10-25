class User :
    def __init__(self, first_name, last_name):         
        self.first_name= first_name
        self.last_name = last_name


us1 = User ("Liza", "Kuzina")
print(us1.first_name)
print(us1.last_name)
print(us1.first_name , us1.last_name)