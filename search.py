import sqlite3

connection = sqlite3.connect("itstep.sl3")
cursor = connection.cursor()

group_name = input("Введіть назву групи для пошуку: ")
cursor.execute(f"SELECT * FROM students WHERE GROUP_NAME = '{group_name}';")

print(f"Результати для групи {group_name}:")
for student in cursor.fetchall():
    print(student)

print("\nСтуденти з балом >= 4.5 та кристалами > 200:")
cursor.execute("SELECT * FROM students WHERE avg_score >= 4.5 AND CRYSTALS > 200;")
for student in cursor.fetchall():
    print(student)

connection.close()
