class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Error: {age} is not a valid age. Age must be between 0 and 120.")

    return "Valid age"

try:
    print(check_age(25))  
    print(check_age(150))  
except InvalidAgeError as e:
    print(e)