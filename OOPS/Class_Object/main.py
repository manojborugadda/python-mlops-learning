class Waiter:
    tables = []

    def __init__(self):
        self.tables = []  # Instance variable to hold tables for each waiter

Alex = Waiter()
Katie = Waiter()

print(Alex.tables)  # Output: []
print(Katie.tables)  # Output: []
print(Waiter.tables)  # Output: []
print("\n")
print("Adding tables to Alex's list , Katie's list...")
Alex.tables.append(1)
print(Alex.tables)  # Output: [1]
Katie.tables.append(2)
print(Katie.tables)  # Output: [2]
print(Waiter.tables)  # Output: [1, 2]

