def generate_report(name, m1, m2, m3):
    # Step 2: Calculate average
    total = m1 + m2 + m3
    average = total / 3

    # Step 3: Determine grade using conditions
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    # Step 4: Return the report card as a dictionary
    report = {
        "Name": name,
        "Marks": [m1, m2, m3],
        "Average": average,
        "Grade": grade
    }

    return report

# Step 5: Take input from user
student_name = input("Enter student's name: ")
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

student_report = generate_report(student_name,mark1,mark2,mark3)

print("\n📄 Report Card:")
print("Name:", student_report["Name"])
print("Marks:", student_report["Marks"])
print("Average:", round(student_report["Average"], 2))
print("Grade:", student_report["Grade"])
