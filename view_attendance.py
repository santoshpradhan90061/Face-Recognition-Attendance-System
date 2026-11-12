import csv
import os

file_name = "attendance.csv"

if not os.path.exists(file_name):
    print("Attendance file not found!")
    exit()

with open(file_name, "r", newline="") as file:
    reader = csv.reader(file)

    print("\n========== ATTENDANCE RECORDS ==========\n")

    records = list(reader)

    if len(records) <= 1:
        print("No attendance records found.")
    else:
        for row in records:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]}")

    print("\n========================================")