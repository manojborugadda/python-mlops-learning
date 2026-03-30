
# FOR loop

# multiplication table of 5

for i in range (1 , 11) :
    print(f"5 x {i} = {5*i}")

# iterating through a list

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

# while loop

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # This will increment the count by 1 in each iteration of the loop.

# pass , break and continue

for i in range(1, 10):
    if i == 3:
        continue  # This will skip the rest of the code inside the loop for this iteration when i is 3 and move to the next iteration.
    elif i == 5:
        break  # This will exit the loop entirely when i is 5.
    else:
        print(i)  # This will print the value of i for all iterations except when i is 3 and when i is 5.

for i in range(1, 5):
    if i == 3:
        pass  # This will do nothing when i is 3 and the loop will continue to the next iteration.
    else:
        print(i)  # This will print the value of i for all iterations except when i is 3, where it will do nothing due to the pass statement.

for i in range(1, 5):
    if i == 3:
        pass  
    print(i)

