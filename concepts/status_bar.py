import time

def display_status_bar(iteration, total):
    # Calculate the percentage of completion
    percent = round((iteration / total) * 100)
    
    # Use a dynamic number of hash symbols to represent the rogress
    # The number of hash symbols should be proportional to the percentage of completion
    num_hashes = int(percent / 5)
    status_bar = f'\r[{"#" * num_hashes}{"_" * (20 - num_hashes)}] {percent}%'
    
    # Print the status bar
    print(status_bar, end='')
    
# Example Usage
total = 100
for i in range(total):
    display_status_bar(i, total)
    time.sleep(0.1)
    
# Make sure to print a new line after the status bar is done.
print('')