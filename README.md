# tutor-data
Some scripts to run on the tutor data to work with the data easier

##Tutor class
__init__(self, first:string, last:string, email:string, courses:list, schedule:dictionary)

Getters and setters for everything

__str__ and __repr__

##Other scripts
**buildDB()** - returns a list of `Tutor`s based on data in `tutors.csv`

**get_tutored_courses(data)** - returns a list of all courses tutored now given the list from `buildDB()`

**get_tutors(course, data)** - returns a list of tutors for a course given the course and the list from `buildDB()`

**get_course_tutors(data)** - returns a dictionary of all the courses tutored and who tutors each one given the list from `buildDB()`

**get_course_tutor_file()** - creates a file `out.csv` with a column of courses tutored now and a column of who is tutoring each one

##Libraries
Just `csv` right now to read and write *.csv files easier
