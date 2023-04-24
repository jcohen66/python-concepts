class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return f"Node({self.value})"
    
    