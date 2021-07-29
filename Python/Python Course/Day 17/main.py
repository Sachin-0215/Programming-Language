class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_one = User("046","Shivaay")
# print(user_one.username)
user_two = User("047","Sachin")

user_one.follow(user_two)
print(user_one.followers)
print(user_one.following)
print(user_two.followers)
print(user_two.following)
