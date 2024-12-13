def safe_input(prompt):
    while True:
        valid_number = input(prompt)
        try:
            return int(valid_number)
        except ValueError:
            print("Please enter a valid integer.")