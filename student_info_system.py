# 1. Create a list to hold students
students = []

# Ask how many students you want to enter
count = int(input("How many students? "))

for i in range(count):
    # 1. Ask for details
    name = input("Enter name: ")
    student_id = input("Enter student id: ")
    ai = input("Enter favourite AI tool: ")

    # 2. Save data in a dictionary
    student_data = {
        "name": name, 
        "id": student_id, 
        "tool": ai
    }

    # 3. Add dictionary to the list
    students.append(student_data)

# 4. Print the total and details
print(f"\nTotal students: {len(students)}")
for s in students:
    print(f"Name: {s['name']}, ID: {s['id']}, Tool: {s['tool']}")

# 5. Function to save to a text file
def save_to_file(student_list):
    with open("students.txt", "w") as file:
        for s in student_list:
            file.write(f"{s['name']}, {s['id']}, {s['tool']}\n")

# Call the function to actually save the file
save_to_file(students)
print("Check students.txt-your data is saved!")
