import sqlite3

connection = sqlite3.connect("itstep.sl3")
cursor = connection.cursor()

search_name = input("Введіть ім'я або прізвище для пошуку: ")

cursor.execute("SELECT * FROM students WHERE FULL_NAME LIKE ?", (f"%{search_name}%",))
results = cursor.fetchall()

if results:
    for student in results:
        print(student)
else:
    print("Нікого не знайдено.")

connection.close()
