class Animal:

    def __init__(self, name: str, age: int, num_legs: int) -> None:
        self.name = name 
        self.age = age 
        self.num_legs = num_legs 

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def talk(self) -> None:
        "Makes animal talk"
        print(f"{self.name} can't talk yet!")

class Dog(Animal):

    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed 
        self.type = "Dogs"
    
    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"


a1 = Animal("Robbin", 10, 4)
print(a1)
a1.talk()

d1 = Dog("Whisky", age=5, num_legs=7, breed="Doberman")
print(d1)