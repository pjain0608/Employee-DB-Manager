# Update employee salaries based on years of experience

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Update salary by 10% for employees with more than 2.5 years of experience
cursor.execute("""
    UPDATE EMP
    SET SAL = ROUND(SAL * 1.10, 2)
    WHERE YOE_YEARS > 2.5 AND YOE_YEARS <= 5.0
""")

# Update salary by 25% for employees with more than 5 years of experience
cursor.execute("""
    UPDATE EMP
    SET SAL = ROUND(SAL * 1.25, 2)
    WHERE YOE_YEARS > 5.0
""")

# Commit the changes
conn.commit()

# Verify the updates
cursor.execute("SELECT * FROM EMP")
updated_data = cursor.fetchall()
print("Updated employee details:")
for row in updated_data:
    print(row)

