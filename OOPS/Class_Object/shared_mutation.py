class Waiter:
    tables = []

    # def __init__(self):
    #     self.tables = []  # Instance variable to hold tables for each waiter

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
print(Katie.tables)  # Output: [1, 2]
print(Waiter.tables)  # Output: [1, 2]

# Shared mutation 
# Multiple references point to the same object in memory. 
# When one reference mutates it, all other references see the change because they're looking at the same object.


"""
Alex.tables, Katie.tables, and Waiter.tables all point to the same list object in memory.
When Alex.tables.append(1) runs, it mutates that one shared list.
Everyone sees it: Katie.tables becomes [1] after the first append, and [1, 2] after the second append.

Memory diagram (before append):

Waiter.tables ──┐
Alex.tables ────┼──→ []  (one list object in memory)
Katie.tables ───┘


After Alex.tables.append(1):

Waiter.tables ──┐
Alex.tables ────┼──→ [1]  (same list, now mutated)
Katie.tables ───┘

Why it happens: Python looks up Alex.tables, doesn't find it on the instance, so it returns the class attribute—which is the same list object. Mutating it changes the shared memory.

How to avoid it: Give each instance its own list in __init__:
class Waiter:
    def __init__(self):
        self.tables = []  # each instance gets its own list

"""