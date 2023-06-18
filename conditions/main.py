# Inline
x = 0
x = 1 if x > 1 else 2


# Guard
def should_i_wear_this_hat(self, hat):
    # guard for quick return.
    if not isinstance(hat, Hat):
        return False

    current_fashion = get_fashion()
    weather_outside = self.look_out_of_window()
    is_stylish = self.evaluate_style(hat, current_fashion)
    if weather_outside.is_raining:
        print("Damn.")
        return True
    else:
        print("Great")
        return is_stylish


# Guard
def should_i_wear_this_hat2(self, hat):
    # guard for quick return.
    if not isinstance(hat, Hat):
        return False

    weather_outside = self.look_out_of_window()
    if weather_outside.is_raining:
        print("Damn.")
        return True
    else:
        print("Great")
        current_fashion = get_fashion()
        is_stylish = self.evaluate_style(hat, current_fashion)
        return is_stylish
