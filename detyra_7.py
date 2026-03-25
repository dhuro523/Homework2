users = [
    {"id": 1, "name": "John", "salary": 500},
    {"id": 2, "name": "", "salary": 300},
    {"id": 3, "name": "Anna", "salary": -100},
    {"id": None, "name": "Mike", "salary": 400}
]

invalid_records = []

for user in users:
    errors = []

    if user["id"] is None:
        errors.append("ID must not be None.")
    
    if user["name"] == "":
        errors.append("Name must not be Empty.")

    if user["salary"] < 0:
        errors.append("Salary must be a positive.")

    
    