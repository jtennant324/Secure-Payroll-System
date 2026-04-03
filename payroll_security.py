import os
import bcrypt
from datetime import datetime


# Function to load existing user IDs from the file
def load_users(file_name):
    user_data = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                user_id, password, authorization = line.strip().split("|")
                user_data[user_id] = {"password": password, "authorization": authorization}
    return user_data


# Function to add user IDs and passwords
def add_users(file_name):
    print("Starting data entry for user accounts...\n")
    user_data = load_users(file_name)
    with open(file_name, "a") as file:
        while True:
            user_id = input("Enter User ID (or type 'End' to stop): ").strip()
            if user_id.lower() == "end":
                break
            if user_id in user_data:
                print(f"Error: User ID '{user_id}' already exists. Please try again.")
                continue

            password = input("Enter Password: ").strip()
            authorization = input("Enter Authorization Code (Admin/User): ").strip().capitalize()

            if authorization not in ["Admin", "User"]:
                print("Error: Authorization code must be 'Admin' or 'User'. Please try again.")
                continue

            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            file.write(f"{user_id}|{hashed_pw}|{authorization}\n")
            user_data[user_id] = {"password": password, "authorization": authorization}
            print(f"User '{user_id}' added successfully.")


# Function to display all user data
def display_users(file_name):
    print("\nDisplaying all user accounts:")
    print("User ID | Password | Authorization Code")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("No user accounts found.")


# Function to input and validate the from and to dates
def input_dates():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            to_date = input("Enter to date (mm/dd/yyyy): ")

            from_date_obj = datetime.strptime(from_date, "%m/%d/%Y")
            to_date_obj = datetime.strptime(to_date, "%m/%d/%Y")

            if to_date_obj < from_date_obj:
                print("The 'to date' cannot be earlier than the 'from date'. Please re-enter.")
                continue

            return from_date, to_date
        except ValueError:
            print("Invalid date format or value. Please use mm/dd/yyyy formatting.")


# Function to input employee details and write to payroll file
def input_employee_data(file_name):
    from_date, to_date = input_dates()
    employee_name = input("Enter employee name: ")
    try:
        hours_worked = float(input(f"Enter hours worked for {employee_name} from {from_date} to {to_date}: "))
        hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
        income_tax_rate = float(input(f"Enter income tax rate (as a decimal, e.g., 0.15 for 15%): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours, rate, and tax.")
        return None

    with open(file_name, "a") as file:
        file.write(f"{from_date}|{to_date}|{employee_name}|{hours_worked}|{hourly_rate}|{income_tax_rate}\n")

    print(f"Payroll record for {employee_name} added successfully.")


# Function to calculate payroll
def calculate_payroll(hours_worked, hourly_rate, income_tax_rate):
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * income_tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay


# Function to generate a payroll report
def generate_report(file_name):
    from_date_filter = input("Enter From Date for the report (mm/dd/yyyy) or 'All' for all records: ")
    if from_date_filter.lower() != "all":
        try:
            datetime.strptime(from_date_filter, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")
            return

    totals = {
        "total_employees": 0,
        "total_hours_worked": 0,
        "total_gross_pay": 0,
        "total_income_tax": 0,
        "total_net_pay": 0
    }

    print("\nEmployee Records:")
    records_found = False

    try:
        with open(file_name, "r") as file:
            for line in file:
                from_date, to_date, employee_name, hours_worked, hourly_rate, income_tax_rate = line.strip().split("|")
                hours_worked = float(hours_worked)
                hourly_rate = float(hourly_rate)
                income_tax_rate = float(income_tax_rate)

                if from_date_filter.lower() == "all" or from_date == from_date_filter:
                    records_found = True
                    gross_pay, income_tax, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate)

                    print(f"From: {from_date}, To: {to_date}, Name: {employee_name}, "
                          f"Hours: {hours_worked:.1f}, Pay Rate: {hourly_rate:.2f}, "
                          f"Gross Pay: {gross_pay:.2f}, Tax: {income_tax:.2f}, Net Pay: {net_pay:.2f}")

                    totals["total_employees"] += 1
                    totals["total_hours_worked"] += hours_worked
                    totals["total_gross_pay"] += gross_pay
                    totals["total_income_tax"] += income_tax
                    totals["total_net_pay"] += net_pay

        if not records_found:
            print(f"No records found for From Date: {from_date_filter}")

    except FileNotFoundError:
        print("No payroll data found. Please add employee records first.")

    if records_found:
        display_totals(totals)


# Function to display payroll totals
def display_totals(totals):
    print("\nTotals:")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours Worked: {totals['total_hours_worked']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Income Taxes: ${totals['total_income_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")


# Admin menu
def admin_menu(payroll_file):
    while True:
        print("\nAdmin Menu:")
        print("1 - Add Payroll Data")
        print("2 - Display Payroll Records")
        print("3 - Logout")
        print("4 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            input_employee_data(payroll_file)
        elif choice == "2":
            generate_report(payroll_file)
        elif choice == "3":
            print("Logging out...\n")
            break
        elif choice == "4":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


# User menu
def user_menu(payroll_file):
    while True:
        print("\nUser Menu:")
        print("1 - Display Payroll Records")
        print("2 - Logout")
        print("3 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_report(payroll_file)
        elif choice == "2":
            print("Logging out...\n")
            break
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


# Login process
def login_process(user_file, payroll_file):
    print("\nStarting login process...")
    user_data = load_users(user_file)

    while True:
        user_id = input("Enter your User ID: ").strip()
        if user_id not in user_data:
            print("Error: User ID not found. Please try again.\n")
            continue

        password = input("Enter your Password: ").strip()
        if not bcrypt.checkpw(password.encode(), user_data[user_id]["password"].encode()):
            print("Error: Incorrect password. Please try again.\n")
            continue

        authorization = user_data[user_id]["authorization"]
        print(f"\nWelcome, {user_id}. Your authorization level is {authorization}.")

        if authorization == "Admin":
            admin_menu(payroll_file)
        elif authorization == "User":
            user_menu(payroll_file)
        break


# Main program flow
def main():
    user_file = "user_data.txt"
    payroll_file = "employee_data.txt"

    add_users(user_file)
    display_users(user_file)
    while True:
        login_process(user_file, payroll_file)


if __name__ == "__main__":
    main()