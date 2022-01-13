class User:
   def __init__(self, name, user_id):
       self.name = name
       self.id = user_id
       self.followers = 0
       self.following = 0
       print("New user is beeing created....")

   def follow(self, user):
       user.followers += 1
       self.following += 1


user_1 = User('Sven', 1)

print(user_1.name)