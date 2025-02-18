from peewee import *
db = SqliteDatabase('sqlite_python.db')
class BaseModel(Model):
    class Meta:
        database = db
class Student(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()
    class Meta:
        table_name = 'Students'
class Course(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    time_start = CharField()
    time_end = CharField()
    class Meta:
        table_name = 'Courses'
class StudentCourse(BaseModel):
    student = ForeignKeyField(Student, backref='courses')
    course = ForeignKeyField(Course, backref='students')
    class Meta:
        table_name = 'Student_courses'
class sqlite_pythonDB:
    def __init__(self):
        db.connect()
        db.create_tables([Student, Course, StudentCourse], safe=True)
    def is_database_populated(self):
        return Student.select().exists()
    def populate_database(self):
        if not self.is_database_populated():
            self.add_student(1, 'Max', 'Brooks', 24, 'Spb')
            self.add_student(2, 'John', 'Stones', 15, 'Spb')
            self.add_student(3, 'Andy', 'Wings', 45, 'Manchester')
            self.add_student(4, 'Kate', 'Brooks', 34, 'Spb')

            self.add_course(1, 'python', '21.07.21', '21.08.21')
            self.add_course(2, 'java', '13.07.21', '16.08.21')

            self.enroll_student(1, 1)
            self.enroll_student(2, 1)
            self.enroll_student(3, 1)
            self.enroll_student(4, 2)

            print("База данных успешно заполнена начальными данными.")
        else:
            print("База данных уже заполнена. Повторное заполнение не требуется.")
    def add_student(self, id, name, surname, age, city):
        Student.create(id=id, name=name, surname=surname, age=age, city=city)
    def add_course(self, id, name, time_start, time_end):
        Course.create(id=id, name=name, time_start=time_start, time_end=time_end)
    def enroll_student(self, student_id, course_id):
        student = Student.get(Student.id == student_id)
        course = Course.get(Course.id == course_id)
        StudentCourse.create(student=student, course=course)
    def get_students_older_than(self, age):
        return Student.select().where(Student.age > age)
    def get_students_younger_than(self, age):
        return Student.select().where(Student.age < age)
    def get_students_by_name(self, name):
        return Student.select().where(Student.name == name)
    def get_students_by_surname(self, surname):
        return Student.select().where(Student.surname == surname)
    def get_students_by_city(self, city):
        return Student.select().where(Student.city == city)
    def get_students_by_course(self, course_name):
        return Student.select().join(StudentCourse).join(Course).where(Course.name == course_name)
    def get_students_by_multiple_criteria(self, name=None, surname=None, city=None, course_name=None, min_age=None, max_age=None):
        query = Student.select()
        if name:
            query = query.where(Student.name == name)
        if surname:
            query = query.where(Student.surname == surname)
        if city:
            query = query.where(Student.city == city)
        if course_name:
            query = (query.join(StudentCourse).join(Course).where(Course.name == course_name))
        if min_age:
            query = query.where(Student.age >= min_age)
        if max_age:
            query = query.where(Student.age <= max_age)
        return query
    def close(self):
        db.close()
university_db = sqlite_pythonDB()

print("Студенты с именем 'Max':")
for student in university_db.get_students_by_name('Max'):
    print(student.id, student.name, student.surname, student.city)
print("\nСтуденты из города 'Spb':")
for student in university_db.get_students_by_city('Spb'):
    print(student.id, student.name, student.surname, student.city)
print("\nСтуденты, записанные на курс 'python':")
for student in university_db.get_students_by_course('python'):
    print(student.id, student.name, student.surname, student.city)
print("\nСтуденты с именем 'Max' и фамилией 'Brooks':")
for student in university_db.get_students_by_multiple_criteria(name='Max', surname='Brooks'):
    print(student.id, student.name, student.surname, student.city)
print("\nСтуденты из города 'Spb' и записанные на курс 'python':")
for student in university_db.get_students_by_multiple_criteria(city='Spb', course_name='python'):
    print(student.id, student.name, student.surname, student.city)
print("\nСтуденты старше 30 лет:")
for student in university_db.get_students_by_multiple_criteria(min_age=30):
    print(student.id, student.name, student.surname, student.age, student.city)
print("\nСтуденты младше 20 лет:")
for student in university_db.get_students_by_multiple_criteria(max_age=20):
    print(student.id, student.name, student.surname, student.age, student.city)
print("\nСтуденты из города 'Spb' старше 20 лет:")
for student in university_db.get_students_by_multiple_criteria(city='Spb', min_age=20):
    print(student.id, student.name, student.surname, student.age, student.city)
university_db.close()