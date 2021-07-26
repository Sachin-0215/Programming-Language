# scope
# enemies = 1

# def increase_enemies():
#     enemies=2
#     print(f"enemies inside functons: {enemies}")

# increase_enemies()
# print(f"enemies ouside function: {enemies}")


# Local scope
# def drink_portion():
#     portion_strength = 2
#     print(portion_strength)

# drink_portion()
# print(portion_strength)


# global scope
# player_health = 20
# def game():
#     def drink_portion():
#         portion_strength = 2
#         print(player_health)

#     drink_portion()

# print(player_health)


# There is no block scope
# remember that in python there is no block scope inside a if/else/for/while code blocks is same as outside it

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton","Zombies","Alien"]
#     if game_level<5:
#         new_enemies = enemies[2]

#     print(new_enemies)

# Modifying the global variable
# enemies = 1

# def increase_enemies():
#     # global enemies # by using this line you can modify global enemies
#     # enemies += 1
#     print(f"enemies inside functons: {enemies}")
#     return enemies+1

# increase_enemies()
# print(f"enemies ouside function: {enemies}")

# Global Constants

PI = 3.14159
