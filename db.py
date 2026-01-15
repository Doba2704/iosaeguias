import sqlite3

connection = sqlite3.connect("itstep.sl3")
cursor = connection.cursor()

# Розкоментовано та додано IF NOT EXISTS для стабільності
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID INTEGER PRIMARY KEY,
    FULL_NAME TEXT,
    GROUP_NAME TEXT,
    AVG_SCORE REAL,
    CRYSTALS INTEGER,
    COINS INTEGER
);
""")

# Використовуємо INSERT OR IGNORE, щоб не було помилок при повторному запуску через однакові ID
cursor.executescript("""
INSERT OR IGNORE INTO students (ID, FULL_NAME, GROUP_NAME, AVG_SCORE, CRYSTALS, COINS) VALUES
(1, 'Ivan Petrenko', 'CS-101', 88.5, 12, 340),
(2, 'Olena Shevchenko', 'CS-101', 91.2, 15, 420),
(3, 'Andrii Kovalenko', 'CS-101', 76.8, 5, 180),
(4, 'Maria Bondarenko', 'CS-101', 84.1, 9, 260),
(5, 'Dmytro Melnyk', 'CS-101', 69.4, 3, 120),
(6, 'Sofiia Koval', 'CS-102', 95.3, 20, 600),
(7, 'Maksym Tkachenko', 'CS-102', 81.0, 8, 240),
(8, 'Yuliia Moroz', 'CS-102', 87.9, 11, 310),
(9, 'Artem Lysenko', 'CS-102', 73.2, 4, 150),
(10, 'Anna Romanenko', 'CS-102', 90.5, 14, 380),
(11, 'Bohdan Savchuk', 'CS-103', 66.7, 2, 90),
(12, 'Kateryna Hnatiuk', 'CS-103', 92.1, 16, 450),
(13, 'Vladyslav Marchenko', 'CS-103', 78.4, 6, 210),
(14, 'Polina Kravets', 'CS-103', 85.6, 10, 290),
(15, 'Oleh Yaremchuk', 'CS-103', 71.9, 4, 160),
(16, 'Iryna Zakharchenko', 'CS-104', 89.8, 13, 360),
(17, 'Roman Ponomarenko', 'CS-104', 74.5, 5, 170),
(18, 'Alina Danyliuk', 'CS-104', 93.6, 18, 520),
(19, 'Taras Horbach', 'CS-104', 68.2, 3, 110),
(20, 'Natalia Kuts', 'CS-104', 82.7, 9, 250),
(21, 'Denys Fedorov', 'CS-105', 77.1, 6, 200),
(22, 'Viktoriia Prykhodko', 'CS-105', 91.9, 15, 430),
(23, 'Mykhailo Bilous', 'CS-105', 70.8, 4, 140),
(24, 'Daria Sydorenko', 'CS-105', 86.4, 11, 300),
(25, 'Ihor Polishchuk', 'CS-105', 79.9, 7, 230),
(26, 'Yaroslav Klymenko', 'CS-106', 83.3, 9, 270),
(27, 'Anastasiia Boiko', 'CS-106', 94.7, 19, 560),
(28, 'Serhii Ostapenko', 'CS-106', 72.6, 4, 155),
(29, 'Liliia Chernenko', 'CS-106', 88.1, 12, 330),
(30, 'Pavlo Rudenko', 'CS-106', 65.9, 2, 95),
(31, 'Oleksandr Havryliuk', 'CS-107', 80.2, 8, 245),
(32, 'Yana Holub', 'CS-107', 92.8, 17, 480),
(33, 'Kyrylo Mazur', 'CS-107', 74.0, 5, 165),
(34, 'Tetiana Levchenko', 'CS-107', 87.5, 11, 315),
(35, 'Stepan Dubovyi', 'CS-107', 69.1, 3, 125),
(36, 'Nazar Chumak', 'CS-108', 81.6, 8, 255),
(37, 'Oksana Fedorenko', 'CS-108', 90.9, 14, 395),
(38, 'Illia Karpov', 'CS-108', 76.3, 6, 205),
(39, 'Svitlana Nesterenko', 'CS-108', 85.0, 10, 285),
(40, 'Yevhen Myronenko', 'CS-108', 67.8, 3, 115),
(41, 'Ruslan Zubko', 'CS-109', 78.9, 7, 225),
(42, 'Olha Kalinina', 'CS-109', 93.2, 18, 540),
(43, 'Vadym Protsenko', 'CS-109', 71.5, 4, 150),
(44, 'Inna Sokolova', 'CS-109', 86.9, 11, 305),
(45, 'Borys Hrytsenko', 'CS-109', 64.7, 2, 85),
(46, 'Arina Lozova', 'CS-110', 89.3, 13, 350),
(47, 'Danylo Kruk', 'CS-110', 75.8, 6, 195),
(48, 'Marharyta Oliinyk', 'CS-110', 92.5, 16, 460),
(49, 'Oleksii Antonenko', 'CS-110', 70.2, 4, 145),
(50, 'Iuliia Rybak', 'CS-110', 84.6, 9, 275),
(51, 'Volodymyr Pasichnyk', 'CS-111', 79.4, 7, 235),
(52, 'Kseniia Panchenko', 'CS-111', 91.6, 15, 425),
(53, 'Mykola Bereza', 'CS-111', 68.9, 3, 120),
(54, 'Veronika Lytvyn', 'CS-111', 87.2, 11, 320),
(55, 'Andrii Shapoval', 'CS-111', 73.7, 5, 165),
(56, 'Yurii Kostiuk', 'CS-112', 82.5, 9, 260),
(57, 'Alona Chorna', 'CS-112', 94.1, 18, 550),
(58, 'Petro Kozak', 'CS-112', 76.9, 6, 210),
(59, 'Milana Romaniuk', 'CS-112', 88.8, 12, 340),
(60, 'Oleksii Baran', 'CS-112', 66.4, 2, 100),
(61, 'Stanislav Hlushko', 'CS-113', 80.7, 8, 250),
(62, 'Diana Vovk', 'CS-113', 92.9, 17, 485),
(63, 'Rostyslav Kachur', 'CS-113', 74.6, 5, 170),
(64, 'Nina Pylypenko', 'CS-113', 86.1, 11, 300),
(65, 'Ihor Holovko', 'CS-113', 69.8, 3, 130),
(66, 'Valeriia Tymoshenko', 'CS-114', 89.9, 13, 365),
(67, 'Orest Humenyuk', 'CS-114', 75.1, 6, 190),
(68, 'Karina Shcherbak', 'CS-114', 93.7, 18, 530),
(69, 'Taras Dovhan', 'CS-114', 71.0, 4, 150),
(70, 'Yuliia Zaitseva', 'CS-114', 85.4, 10, 290),
(71, 'Bohdan Kovalchuk', 'CS-115', 78.3, 7, 220),
(72, 'Elina Martynenko', 'CS-115', 91.3, 15, 410),
(73, 'Arsenii Bondar', 'CS-115', 67.5, 3, 110),
(74, 'Iryna Malakhova', 'CS-115', 88.0, 12, 335),
(75, 'Pavlo Synenko', 'CS-115', 73.9, 5, 175),
(76, 'Denys Hladkyi', 'CS-116', 82.9, 9, 265),
(77, 'Mariya Andrusiv', 'CS-116', 94.5, 19, 580),
(78, 'Oleksandr Babii', 'CS-116', 76.0, 6, 205),
(79, 'Yevheniia Prokopenko', 'CS-116', 87.6, 11, 310),
(80, 'Vasyl Pankiv', 'CS-116', 65.2, 2, 95),
(81, 'Larysa Kostiuk', 'CS-117', 90.1, 14, 390),
(82, 'Maksym Derevianko', 'CS-117', 74.3, 5, 165),
(83, 'Sofia Klymchuk', 'CS-117', 92.6, 16, 455),
(84, 'Oleh Chaban', 'CS-117', 70.6, 4, 145),
(85, 'Anhelina Dziuba', 'CS-117', 85.9, 10, 295);
""")

connection.commit()

cursor.execute("SELECT * FROM students;")
for student in cursor.fetchall():
    print(student)

connection.close()
