# ITERATIVE 
def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{step}")

# RECURSIVE - Add frames to the callstack.
def walk_recursive(steps):
    # Base case so you dont blow out the stack.
    if steps == 0:
        return
    walk_recursive(steps - 1)
    print(f"You take step #{steps}")
    

# walk(100)
walk_recursive(100)