# # the ability to create specialized verstions of classes

# class User:
#   def __init__(self, email, first_name, last_name):
#     self.email = email
#     self.first_name = first_name
#     self.last_name = last_name

#   def greeting(self):
#     return f'Hi {self.first_name} {self.last_name}'

# class AdminUser(User):
#   def active_users(self):
#     return '500'


# tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

# kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

# print(tiffany.active_users())
# print(tiffany.greeting())
# print(kristine.active_users())



class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

class Cat(Pet):
    def speak(self):
        return 'Meow'

class Dog(Pet):
    def speak(self):
        return 'Woof'


cat_one = Cat('Bob', 9)
print(dog_one.speak())
print(cat_one.name)
print(cat_one.age)
cat_one.purchase_Pet('Todd')

dog_one = Dog('Billy', 6)
print(dog_one.speak())
print(dog_one.name)
print(dog_one.age)
dog_one.purchase_Pet('Sally')






















