# To Create Employee and update experience in the database

import sqlite3
from datetime import datetime

con = sqlite3.connect('employees.db')
cursor = con.cursor()

# Table Creation
'''
cursor.execute("""
CREATE TABLE EMP (
    EMP_ID INT PRIMARY KEY, 
    ENAME VARCHAR(50), 
    SAL DECIMAL(6,2), 
    DESIGNATION VARCHAR(32), 
    REPORTING_MANAGER INT, 
    DOJ DATE, 
    LOCATION VARCHAR(10), 
    GENDER VARCHAR(10), 
    EMAIL VARCHAR(30), 
    PHONE_NUMBER BIGINT, 
    YOE_YEARS INT DEFAULT 0, 
    YOE_MONTHS INT DEFAULT 0
);
""")
'''

while True:
    print("**********Welcome to Employee Management**********")
    print("\nMenu:")
    print("1. Add Employee Details")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        # User Input and Insertion into Table
        ID = int(input('Enter the Emp_ID: '))
        Name = input('Enter the Name: ')
        Sal = int(input('Enter the Salary: '))
        Desg = input('Enter the Designation: ')
        mgr = int(input('Reporting Manager ID: '))
        date = input('Date of Joining (YYYY-MM-DD): ')
        loc = input('Enter location: ')
        gen = input('Enter Gender: ')
        e_mail = f"{ID}@{loc.lower()}.com"
        number = int(input('Enter phone number: '))

        cursor.execute(f"""INSERT INTO EMP (EMP_ID, ENAME, SAL, DESIGNATION, REPORTING_MANAGER, DOJ, LOCATION, GENDER, PHONE_NUMBER, EMAIL) VALUES ({ID}, '{Name}', {Sal}, '{Desg}', '{mgr}', '{date}', '{loc}', '{gen}', '{number}', '{e_mail}');""")
        con.commit()
        print("Employee added successfully!")

        # Get the DOJ and update experience
        cursor.execute("SELECT DOJ FROM EMP WHERE EMP_ID = ?", (ID,))
        result = cursor.fetchone()

        if result is None:
            print("Employee not found!")
        else:
            doj = result[0]
            
            # Check if DOJ is NULL
            if doj is None:
                print("Date of Joining is not available for this employee.")
            else:
                # Manually parse the date string
                year, month, day = map(int, doj.split("-"))
                doj_date = datetime(year, month, day)
                current_date = datetime.now()
                
                # Calculate the total months of experience
                total_months = (current_date.year - doj_date.year) * 12 + (current_date.month - doj_date.month)
                
                # Calculate years of experience
                years = round(total_months / 12.0, 2)
                
                # Update the database with the years of experience and total months
                cursor.execute("""
                    UPDATE EMP 
                    SET YOE_YEARS = ?, YOE_MONTHS = ? 
                    WHERE EMP_ID = ?
                """, (years, total_months, ID))
                
                # Commit the changes
                con.commit()
                print(f"Experience updated successfully for Employee ID {ID}: {years} years or {total_months} months.")
    
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

