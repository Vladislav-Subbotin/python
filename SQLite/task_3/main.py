import sqlite3

class Table():
    def connect_db(self):
        return sqlite3.connect('university.db')
    def create_tables(self):
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            age INTEGER,
            city TEXT
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time_start TEXT NOT NULL,
            time_end TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student_courses (
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(id),
            FOREIGN KEY (course_id) REFERENCES Courses(id),
            PRIMARY KEY (student_id, course_id)
        )
        ''')
        students = [
            (1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manchester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')
        ]
        cursor.executemany("INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)", students)
        courses = [
            (1, 'python', '21.07.21', '21.08.21'),
            (2, 'java', '13.07.21', '16.08.21')
        ]
        cursor.executemany("INSERT INTO Courses (id, name, time_start, time_end) VALUES (?, ?, ?, ?)", courses)
        enrollments = [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2)
        ]
        cursor.executemany("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)", enrollments)
        conn.commit()
        print("База данных успешно заполнена начальными данными.")
    def get_students_older_than(self, age):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE age > ?", (age,))
        return cursor.fetchall()
    def get_students_in_course(self, course_name):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT Students.id, Students.name, Students.surname 
        FROM Students
        JOIN Student_courses ON Students.id = Student_courses.student_id
        JOIN Courses ON Student_courses.course_id = Courses.id
        WHERE Courses.name = ?
        ''', (course_name,))
        return cursor.fetchall()

    def get_students_in_course_from_city(self, course_name, city):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT Students.id, Students.name, Students.surname 
        FROM Students
        JOIN Student_courses ON Students.id = Student_courses.student_id
        JOIN Courses ON Student_courses.course_id = Courses.id
        WHERE Courses.name = ? AND Students.city = ?
        ''', (course_name, city))
        return cursor.fetchall()

    def get_students_by_name(self, name):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE name = ?", (name,))
        return cursor.fetchall()

    def get_students_by_surname(self, surname):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE surname = ?", (surname,))
        return cursor.fetchall()

    def get_students_by_city(self, city):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE city = ?", (city,))
        return cursor.fetchall()

    def get_students_by_course(self, course_name):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT Students.id, Students.name, Students.surname 
        FROM Students
        JOIN Student_courses ON Students.id = Student_courses.student_id
        JOIN Courses ON Student_courses.course_id = Courses.id
        WHERE Courses.name = ?
        ''', (course_name,))
        return cursor.fetchall()

    def get_students_by_two_criteria(self, name=None, surname=None, city=None, course_name=None, min_age=None, max_age=None):
        cursor = conn.cursor()
        query = "SELECT * FROM Students"
        conditions = []
        params = []

        if name:
            conditions.append("name = ?")
            params.append(name)
        if surname:
            conditions.append("surname = ?")
            params.append(surname)
        if city:
            conditions.append("city = ?")
            params.append(city)
        if course_name:
            query = '''
            SELECT Students.id, Students.name, Students.surname 
            FROM Students
            JOIN Student_courses ON Students.id = Student_courses.student_id
            JOIN Courses ON Student_courses.course_id = Courses.id
            WHERE Courses.name = ?
            '''
            params.append(course_name)
        if min_age:
            conditions.append("age >= ?")
            params.append(min_age)
        if max_age:
            conditions.append("age <= ?")
            params.append(max_age)

        if conditions and not course_name:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, tuple(params))
        return cursor.fetchall()
conn = Table()
conn.connect_db()
