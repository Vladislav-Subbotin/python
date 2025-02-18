import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    age INTEGER,
                                    city TEXT); ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    time_start TEXT NOT NULL,
                                    time_end TEXT NOT NULL); ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
                                    student_id INTEGER,
                                    course_id INTEGER,
                                    FOREIGN KEY (student_id) REFERENCES Students(id),
                                    FOREIGN KEY (course_id) REFERENCES Courses(id),
                                    PRIMARY KEY (student_id, course_id)); ''')
    students_data = [
        (1, 'Max', 'Brooks', 24, 'Spb'),
        (2, 'John', 'Stones', 15, 'Spb'),
        (3, 'Andy', 'Wings', 45, 'Manchester'),
        (4, 'Kate', 'Brooks', 34, 'Spb')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Students(id, name, surname, age, city) VALUES(?, ?, ?, ?, ?)', students_data)
    courses_data = [
        (1, 'python', '21.07.21', '21.08.21'),
        (2, 'java', '13.07.21', '16.08.21')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Courses(id, name, time_start, time_end) VALUES(?, ?, ?, ?)', courses_data)
    students_courses_data = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Student_courses(student_id, course_id) VALUES(?, ?)', students_courses_data)
    sqlite_connection.commit()
    cursor.execute('SELECT id, name, surname FROM Students WHERE age>30')
    age30 = cursor.fetchall()
    cursor.execute('''SELECT Students.id, Students.name, Students.surname 
                    FROM Students
                    JOIN Student_courses ON Students.id = Student_courses.student_id
                    JOIN Courses ON Student_courses.course_id = Courses.id
                    WHERE Courses.name = 'python' ''')
    python_students = cursor.fetchall()
    cursor.execute('''SELECT Students.id, Students.name, Students.surname 
                      FROM Students
                      JOIN Student_courses ON Students.id = Student_courses.student_id
                      JOIN Courses ON Student_courses.course_id = Courses.id
                      WHERE Courses.name = 'python' AND Students.city = 'Spb' ''')
    python_spb_students = cursor.fetchall()
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite:", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
print(age30)
print(python_students)
print(python_spb_students)