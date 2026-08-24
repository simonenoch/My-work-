import pandas as pd

students = {
    "Name": ["Enoch", "Mary", "John", "Grace", "David"],
    "Age": [22, 20, 21, 23, 19],
    "Department": [
        "Mechatronics",
        "Computer Science",
        "Electrical",
        "Civil",
        "Computer Science"
    ],
    "Score": [85, 90, 78, 95, 65]
}

df = pd.DataFrame(students)

print("Student Records")
print(df)

print("\nAverage Score:")
print(df["Score"].mean())

print("\nHighest Score:")
print(df["Score"].max())

print("\nStudents Who Passed:")
print(df[df["Score"] >= 70])

print("\nComputer Science Students:")
print(df[df["Department"] == "Computer Science"])
