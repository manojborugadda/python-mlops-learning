

# python iterators

Python has two primitive loop commands: `for` loops and `while` loops. 
The `for` loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. 
An iterable is any Python object capable of returning its members one at a time, allowing it to be iterated over in a loop.

Python provides several types of loops to manage iteration:

| Sr.No. | Name of the Loop  | Loop Type & Description |
| ------ | ------------------ | ----------------------- |
| 1 | While Loop | Repeats a statement or group of statements while a given condition is True. It tests the condition before executing the loop body. |
| 2 | For Loop | Executes a code block multiple times and manages the loop variable. It is often used to iterate over sequences like lists, strings, or ranges. |
| 3 | Nested Loops | A loop inside another loop. Useful for working with multi-dimensional data or performing complex iterations. |

🔧 Loop Control Statements
Loop control statements are used to change the course of iteration or exit a loop early. These are essential for managing loops effectively:

| Sr.No. | Name of the Control Statement | Description |
| ------ | ----------------------------- | ----------- |
| 1 | Break Statement | Terminates the loop's execution and transfers control to the statement following the loop. |
| 2 | Continue Statement | Skips the current iteration of the loop. The remaining code in the loop body is not executed for that iteration. |
| 3 | Pass Statement | Used when a statement is syntactically required but no code needs to be executed. Useful as a placeholder. |


# PASS and CONTINUE statements
continue:

    - used inside loops (for / while)
    - skips rest of current iteration and moves to next iteration
    - affects flow control
pass:

    - no-op statement, does nothing
    - placeholder when syntax needs a statement (empty block, stub function/class)
    - does not alter loop iteration by itself

```python
for i in range(5):
    if i % 2 == 0:
        continue   # go to next i
    print(i)       # prints 1, 3

for i in range(3):
    if i == 1:
        pass       # nothing happens
    print(i)       # prints 0, 1, 2
```