import sample_module

def get_sample_data() -> dict:
    return {"user": "mario123", 'id': 123456}

if __name__ == "__main__":
    print("Before:", sample_module.get_data())

    # Give function that belongs to another module a new function
    sample_module.get_data = get_sample_data
    
    print("After:", sample_module.get_data())

