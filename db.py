import sqlite3

connection = sqlite3.connect("itstep.sl3")
cursor = connection.cursor()

# cursor.execute("""
# create table students (
#     ID INTEGER PRIMARY KEY,
#     FULL_NAME TEXT,
#     GROUP_NAME TEXT,
#     AVG_SCORE REAL,
#     CRYSTALS INTEGER,
#     COINS INTEGER);
# """)

cursor.execute(f"""
    INSERT INTO students (ID, FULL_NAME, GROUP_NAME, AVG_SCORE, CRYSTALS, COINS) VALUES (
        {input("ID: ")},
        "{input("FULL_NAME: ")}",
        "{input("GROUP_NAME: ")}",
        {input("AVG_SCORE: ")},
        {input("CRYSTALS: ")},
        {input("COINS: ")}
    );
""")
connection.commit()

cursor.execute("SELECT * FROM students;")
connection.commit()
for student in cursor.fetchall():
    print(student)

connection.close()