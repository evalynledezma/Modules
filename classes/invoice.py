# class Invoice: 
#     def greeting(self):
#         return 'Hi there'


# inv_one = Invoice()
# print(inv_one.greeting())

# inv_one = Invoice()
# print(inv_one.greeting())


# class Dog:
#     def speak(self):
#         return 'Woof'

# dog_one = Dog()
# print(dog_one.speak())

# dog_two = Dog()
# print(dog_two.speak())


# class Invoice:

#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100)
# snapchat = Invoice('SnapChat', 200)

# print(google.formatter())
# print(snapchat.formatter())


class Cat:

    def __init__(self, name):
        self.name = name
    
    def speak(name):
        return self.name

sam = Cat('Meow')
tom = Cat('Mew')

print(sam.speak())
print(tom.speak())
