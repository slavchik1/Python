class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " видає звук")

cat = Animal("Кіт")
dog = Animal("Собака")
cat.speak() # Кіт видає звук
dog.speak() # Собака видає звук