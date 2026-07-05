# student_operations.py
from db_config import get_connection

def add_student(first_name, last_name, email, course):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO students (first_name, last_name, email, course) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, course)
            cursor.execute(query, values)
            conn.commit()
            print(f"\nSuccess: {first_name} {last_name} has been added to the system.")
        except Exception as e:
            print(f"\nFailed to add student: {e}")
        finally:
            cursor.close()
            conn.close()

def view_students():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()
            
            print("\n--- Student Records ---")
            print(f"{'ID':<5} | {'First Name':<15} | {'Last Name':<15} | {'Email':<25} | {'Course'}")
            print("-" * 75)
            for row in records:
                print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<15} | {row[3]:<25} | {row[4]}")
        except Exception as e:
            print(f"\nError retrieving students: {e}")
        finally:
            cursor.close()
            conn.close()

def update_student_course(student_id, new_course):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE students SET course = %s WHERE student_id = %s"
            cursor.execute(query, (new_course, student_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"\nSuccess: Student ID {student_id} updated successfully.")
            else:
                print(f"\nNotice: Student ID {student_id} not found.")
        except Exception as e:
            print(f"\nFailed to update student: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_student(student_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"\nSuccess: Student ID {student_id} has been deleted.")
            else:
                print(f"\nNotice: Student ID {student_id} not found.")
        except Exception as e:
            print(f"\nFailed to delete student: {e}")
        finally:
            cursor.close()
            conn.close()