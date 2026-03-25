def log_cleaning(func):
    def wrapper(data):
        print(f"Cleaning started for: {data}")
        result = func(data)
        print(f"Cleaned list: {result}")
        return result
    return wrapper

@log_cleaning
def clean_data(values):
    def convert_to_int(val):
        try:
            return int(val)
        except ValueError:
            return None

    mapped_results = map(convert_to_int, values)
    return [x for x in mapped_results if x is not None]

values = ["5", "10", "x", "15", "NaN", "20"]
cleaned_values = clean_data(values)