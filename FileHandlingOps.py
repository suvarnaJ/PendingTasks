# --------------------------------------------
# Python File Handling Demo
# --------------------------------------------

# --------------------------------------------
# 1. Creating the file using "w" mode
# --------------------------------------------

file = open("notes.txt", "w")

file.write("Python is easy to learn.\n")
file.write("Python supports file handling.\n")
file.write("We can create files using Python.\n")
file.write("The open() function is used to open files.\n")
file.write("The write() function writes data into a file.\n")
file.write("The read() function reads file contents.\n")
file.write("The readline() function reads one line.\n")
file.write("The readlines() function reads all lines.\n")
file.write("The append mode adds new data to a file.\n")
file.write("Python provides different file modes.\n")

file.close()

print("notes.txt created successfully.")


# --------------------------------------------
# 2. Reading the entire file using read()
# --------------------------------------------

file = open("notes.txt", "r")

data = file.read()

print("\n--- Entire File ---")
print(data)

file.close()


# --------------------------------------------
# 3. Reading specific number of characters
# --------------------------------------------

file = open("notes.txt", "r")

data = file.read(30)

print("--- First 30 Characters ---")
print(data)

file.close()


# --------------------------------------------
# 4. Using readline()
# --------------------------------------------

file = open("notes.txt", "r")

line = file.readline()

print("\n--- First Line Using readline() ---")
print(line)

file.close()


# --------------------------------------------
# 5. Using readlines()
# --------------------------------------------

file = open("notes.txt", "r")

lines = file.readlines()

print("--- All Lines Using readlines() ---")

for line in lines:
    print(line.strip())

file.close()


# --------------------------------------------
# 6. Appending additional notes using "a"
# --------------------------------------------

file = open("notes.txt", "a")

file.write("File handling is useful for storing data.\n")
file.write("Always close a file after using it.\n")
file.write("The with open() statement closes files automatically.\n")

file.close()

print("\nAdditional notes appended successfully.")


# --------------------------------------------
# 7. Reopen the file and display updated contents
# --------------------------------------------

file = open("notes.txt", "r")

updated_data = file.read()

print("\n--- Updated File Contents ---")
print(updated_data)

file.close()


# --------------------------------------------
# 8. Demonstrating "with open()"
# --------------------------------------------

with open("notes.txt", "r") as file:
    data = file.read()

print("--- Reading Using with open() ---")
print(data)