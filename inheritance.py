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



Class Example Challenge Finished:
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
  
  def speak(self):
    return "I don't speak"
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
  def speak(self):
    return 'Meow'
class Dog(Pet):
  def speak(self):
    return "Woof"
class Fish(Pet):
  pass





















