
import subprocess
import sys
import os

def run_program(filename):
    print(f"\nStarting {filename}...")
    subprocess.run([sys.executable, filename])

while True:
    print("\n====================================")
    print("  FACE RECOGNITION ATTENDANCE SYSTEM")
    print("====================================")
    print("1. Register New Face")
    print("2. Recognize Face")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")
    print("====================================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        run_program("register_face.py")

    elif choice == "2":
        run_program("recognize_face.py")

    elif choice == "3":
        run_program("attendance.py")

    elif choice == "4":
        run_program("view_attendance.py")

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
