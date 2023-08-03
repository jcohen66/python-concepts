age = 25
smokes = True

# Health classification using a ternary operator
health = "Poor" if age > 60 or smokes else  "Good" if age < 30 else "Fair"

print("Health classification:", health)

# Equivalent
if age > 60 or smokes:
    health = "Poor"
else:
    if age < 30:
        health = "Good"
    else:
        health = "Fair"