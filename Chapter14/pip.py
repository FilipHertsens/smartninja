from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity", "ffff"])

table.add_row(["wolverine", 100, "lala"])
table.add_row(["grizzly", 87, "kaka"])
table.add_row(["cat", -1,""])
table.add_row(["dolphin", 63,""])

print(table)