class house():
    def __init__(self, street, number):
        self.street = street
        self.number = number
        
    def bulid(self):
        print(f"улица {self.street}, номер {self.number}")
        
house1 = house("Anet baba", 19)
house2 = house("Kabanbai batyra", 40)

print(house1.street)
print(house2.street)
print(house1.number)
print(house2.number)

house1.bulid()