import sqlite3 as sq

class DbManager:
  
  def __init__(self):
    self.db_file = 'logBook.db'

  def Db_init(self):
    try:
      with sq.connect(self.db_file) as conn:
        cur = conn.cursor()
     
        # Enable foreign key support 
        cur.execute('PRAGMA foreign_keys = ON')

        # Create role table
        create = "CREATE TABLE IF NOT EXISTS role (role_id INTEGER PRIMARY KEY, role_name varchar(15) UNIQUE)"

        cur.execute(create)
        conn.commit()

        # Create the class table
        create = "CREATE TABLE IF NOT EXISTS class (class_id INTEGER PRIMARY KEY, class_name varchar(15) UNIQUE)"
        cur.execute(create)
        conn.commit()


        # Create student table
        create = '''CREATE TABLE IF NOT EXISTS students (
          id INTEGER PRIMARY KEY, 
          name varchar(50) UNIQUE COLLATE NOCASE,
          Dob DATE,
          gender char(2) CHECK(gender IN('M', 'F')),
          Tel varchar(12),
          role_id INTEGER default 2,
          class_id INTEGER,
          FOREIGN KEY(role_id) REFERENCES role(role_id),
          FOREIGN KEY(class_id) REFERENCES role(class_id)
          
        )'''
        cur.execute(create)
        conn.commit()

        # Create the course table
        create = '''CREATE TABLE IF NOT EXISTS courses (
          course_id INTEGER PRIMARY KEY,
          course_name varchar(25) UNIQUE,
          teacher varchar(30)
        )'''
        cur.execute(create)
        conn.commit()

        # Create the course information table
        create = '''CREATE TABLE IF NOT EXISTS class_courses (
          class_id INTEGER,
          course_id INTEGER,
          course_info TEXT,
          PRIMARY KEY(class_id, course_id)
        )'''
        cur.execute(create)
        conn.commit()

        # Create the index on the students table
        create = '''CREATE UNIQUE INDEX IF NOT EXISTS unq ON students(id, name)'''
        cur.execute(create)
        conn.commit()

        # Create the index on the students table
        create = '''CREATE UNIQUE INDEX IF NOT EXISTS uniq ON class_courses(class_id, course_id)'''
        cur.execute(create)
        conn.commit()

        print("Tables created successfully")

    except sq.Error as e:
      print("\nan error occured: ", e ,"\n")


  def insert(self,list, table):
    try:
       with sq.connect(self.db_file) as conn:
        cur = conn.cursor()
     
        if table == "role":
          for rol in list:
            insert = f"INSERT INTO role (role_id, role_name) VALUES (?, ?)"
            cur.execute(insert, (rol['id'], rol['name']))
            conn.commit()

        elif table == "class":
          for cl in list:

            insert = "INSERT INTO class(class_name) VALUES ('{}')".format(cl)
            cur.execute(insert)
            conn.commit()

        elif table == "courses":
          for course in list:

            insert = "INSERT INTO courses(course_name, teacher) VALUES (?, ?)"
            cur.execute(insert, course)
            conn.commit()
        
        elif table == "students":
          for stud in list:
            insert = '''INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?)'''
            cur.execute(insert, stud)
            conn.commit()

        print("Data inserted successfully")

    except sq.Error as e:
      print("\nan error occured: ", e ,"\n")


  def select(self, table, condition=None):
    try:
       with sq.connect(self.db_file) as conn:
        cur = conn.cursor()

        if condition is None:
          sel = f"SELECT * FROM {table}"
        else:
          sel = f"SELECT * FROM {table} WHERE {condition}"

        cur.execute(sel)

        result =  cur.fetchall()

        return True, result
    
    except sq.Error as e:
      return False, e

  def dropTable(self, table):
    try:
       with sq.connect(self.db_file) as conn:
        cur = conn.cursor()
     
        sel = f"DROP TABLE {table}"
        cur.execute(sel)
        conn.commit()

        print ("Table dropped successfully")

    except sq.Error as e:
      print(e)

# End of class declaration
      
Dbcode = DbManager()


# Program body
  

