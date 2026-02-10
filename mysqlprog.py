import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection"""
    try:
        conn = mysql.connector.connect(
            host='localhost',       # your host
            user='root',            # your MySQL username
            password='root@1234',    # your MySQL password
            database='anagha'       # database name
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def reset_table(conn):
    """Drop table if exists and create a new one"""
    try:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("""
        CREATE TABLE students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            grade VARCHAR(10)
        )
        """)
        print("Table 'students' has been reset and is ready.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_value(conn):
    """Insert a new record"""
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
        conn.commit()
        print("Record inserted successfully!")
    except ValueError:
        print("Invalid input! Age must be a number.")
    except Error as e:
        print(f"Database error: {e}")

def view_values(conn):
    """View all records"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")
    except Error as e:
        print(f"Database error: {e}")

def update_value(conn):
    """Update a record"""
    try:
        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_grade = input("Enter new grade: ")

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s",
            (new_name, new_age, new_grade, student_id)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print("Record updated successfully!")
        else:
            print("No record found with that ID.")
    except ValueError:
        print("Invalid input! ID and Age must be numbers.")
    except Error as e:
        print(f"Database error: {e}")

def delete_value(conn):
    """Delete a record"""
    try:
        student_id = int(input("Enter student ID to delete: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Record deleted successfully!")
        else:
            print("No record found with that ID.")
    except ValueError:
        print("Invalid input! ID must be a number.")
    except Error as e:
        print(f"Database error: {e}")

def main():
    conn = create_connection()
    if not conn:
        return

    reset_table(conn)  # Drop & create table fresh

    while True:
        print("\n--- MENU ---")
        print("1. Insert Value")
        print("2. View Values")
        print("3. Update Value")
        print("4. Delete Value")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number from 1 to 5.")
            continue

        match choice:
            case 1:
                insert_value(conn)
            case 2:
                view_values(conn)
            case 3:
                update_value(conn)
            case 4:
                delete_value(conn)
            case 5:
                print("Exiting program...")
                break
            case _:
                print("Invalid choice! Enter a number from 1 to 5.")

    conn.close()

if __name__ == "__main__":
    main()
