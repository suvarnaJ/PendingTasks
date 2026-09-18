# Student Registration Application
# Using Python File Handling

# --------------------------------------------------
# 1. Create and write student records
# --------------------------------------------------

students = [
    "101,Sudhanshu,sudh@example.com,9999999999,Python,Bangalore",
    "102,Rahul,rahul@example.com,8888888888,Data Science,Delhi",
    "103,Priya,priya@example.com,7777777777,Java,Pune",
    "104,Amit,amit@example.com,6666666666,Python,Mumbai",
    "105,Neha,neha@example.com,5555555555,Machine Learning,Hyderabad",
    "106,Rohan,rohan@example.com,4444444444,Java,Chennai",
    "107,Anjali,anjali@example.com,3333333333,Data Science,Pune",
    "108,Vikram,vikram@example.com,2222222222,Python,Bangalore",
    "109,Pooja,pooja@example.com,1111111111,AI,Mumbai",
    "110,Karan,karan@example.com,9999999998,Java,Delhi"
]

# Write records into students.txt
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Student records created successfully.")


# --------------------------------------------------
# 2. Append a new student record
# --------------------------------------------------

new_student = "111,Meena,meena@example.com,8888888887,Python,Pune"

with open("students.txt", "a") as file:
    file.write(new_student + "\n")

print("New student record added successfully.")


# --------------------------------------------------
# 3. Read complete records
# --------------------------------------------------

print("\n--- Complete Student Records ---")

with open("students.txt", "r") as file:
    data = file.read()

print(data)


# --------------------------------------------------
# 4. Read individual lines
# --------------------------------------------------

print("--- Individual Student Records ---")

with open("students.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


# --------------------------------------------------
# 5. Count number of student records
# --------------------------------------------------

with open("students.txt", "r") as file:
    records = file.readlines()

record_count = len(records)

print("\nTotal number of student records:", record_count)


# --------------------------------------------------
# 6. Copy data into students_backup.txt
# --------------------------------------------------

with open("students.txt", "r") as source:
    data = source.read()

with open("students_backup.txt", "w") as backup:
    backup.write(data)

print("Backup file students_backup.txt created successfully.")


# --------------------------------------------------
# 7. Create file containing only names and courses
# --------------------------------------------------

with open("students.txt", "r") as file:
    records = file.readlines()

with open("student_names_courses.txt", "w") as file:

    for record in records:

        # Remove newline
        record = record.strip()

        # Split record using comma
        fields = record.split(",")

        # Fields:
        # 0 = student_id
        # 1 = name
        # 2 = email
        # 3 = phone
        # 4 = course
        # 5 = city

        name = fields[1]
        course = fields[4]

        file.write(name + "," + course + "\n")

print("Names and courses file created successfully.")


# --------------------------------------------------
# 8. Display names and courses
# --------------------------------------------------

print("\n--- Student Names and Courses ---")

with open("student_names_courses.txt", "r") as file:
    data = file.read()

print(data)