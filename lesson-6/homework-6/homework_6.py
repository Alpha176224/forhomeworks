# def check(func):
#     def wrapper(*args, **kwargs):
#         if args[1] == 0: 
#             raise ValueError("Denominator cannot be zero.")
#         return func(*args, **kwargs)
#     return wrapper


def add_employee_to_file():
    with open("employees.txt", "a") as file:
        while True:
            print("\nEnter the employee details:")
            employee_id = input("Employee ID: ")
            name = input("Name: ")
            position = input("Position: ")
            salary = input("Salary: ")
            employee_record = f"{employee_id},{name},{position},{salary}\n"
            file.write(employee_record)
            print("Employee record added successfully.")
            continue_adding = input("\nDo you want to add another employee? (y/n): ").lower()
            if continue_adding != 'y':
                print("Exiting the program.")
                break