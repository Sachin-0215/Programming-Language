# pypi.org

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmanter"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)