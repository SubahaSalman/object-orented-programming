class Dog:
    breed1= "Golden Retriever"
    breed2= "Teckle"
    def __init__(self, name, size):
        self.name = name
        self.size= size

Charlie = Dog("Charlie", "Large")
Joey = Dog("Joey", "Small")

print("{} is a {}, and its size is {}".format(Charlie.name, Charlie.breed1, Charlie.size))
print("{} is a {}, and its size is {}".format(Joey.name, Joey.breed2, Joey.size))