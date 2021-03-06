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


# class Cat:

#     def __init__(self, name):
#         self.name = name
    
#     def speak(name):
#         return self.name

# sam = Cat('Meow')
# tom = Cat('Mew')

# print(sam.speak())
# print(tom.speak())


# How to Work with Python Properties and Decorators
class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)



# Overview of Dunder Methods in Python: __init__ 
class Invoice:
  def __str__(self):
    return "This is the invoice class!"


inv = Invoice()
print(str(inv))

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"


inv = Invoice('Google', 500)
print(str(inv))