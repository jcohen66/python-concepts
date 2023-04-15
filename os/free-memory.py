import psutil
import humanize

# Get the total amount of memory available on the system
total_memory = psutil.virtual_memory().total

# Get the amount of used memory
used_memory = psutil.virtual_memory().used

# Calculate the amount of free memory
free_memory = total_memory - used_memory

# Format the free memory into a more readable way
formatted_total_memory = humanize.naturalsize(total_memory, gnu=True)
formatted_used_memory = humanize.naturalsize(used_memory, gnu=True)
formatted_free_memory = humanize.naturalsize(free_memory, gnu=True)

print("Total Memory: ", total_memory, formatted_free_memory)
print("Used Memory:  ", used_memory, formatted_used_memory)
print("Free Memory:  ", free_memory, formatted_free_memory)
