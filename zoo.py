class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def add_bear(self, name):
        self.animals.append( Bear(name) )
class animal:
    def __init__(self,name,age,health,happiness):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness
    
    def display_info(self):
        print("name:"+ self.name , "age:" , self.age , "health:", self.health, "happiness:" , self.happiness )
    def feed(self):
        self.health += 10

class Lion(animal):
    def __init__(self,name, color = "Red" ,age=6,health=90,happiness=70 ):
        super().__init__(name,age,health,happiness)
        self.color = color
    def feed(self):
        self.health += 25
        
class Tiger(animal):
    def __init__(self,name, color = "Blue" ,age=8,health=6,happiness=50 ):
        super().__init__(name,age,health,happiness)
        self.color = color
    def feed(self):
        self.health += 15

class Bear(animal):
    def __init__(self,name, color = "Brown" ,age=3,health=100,happiness=120 ):
        super().__init__(name,age,health,happiness)
        self.color = color
    def feed(self):
        self.health += 30     

    pass
class tiger(animal):
    pass
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("lucy")
zoo1.print_all_info()
