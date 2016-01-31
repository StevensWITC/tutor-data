# tutor-data
Some scripts to run on the tutor data to work with the data easier

##Tutor class
\_\_init\_\_(self, first:string, last:string, email:string, courses:list, schedule:dictionary)

Getters and setters for everything

\_\_str\_\_ and \_\_repr\_\_

##TutorScripts class
**\_\_init\_\_(self, filename)** - calls `buildDB()` to get the info for the other functions to use

**buildDB()** - returns a list of `Tutor`s based on data in `tutors.csv`

**get_tutored_courses()** - returns a list of all courses tutored now

**get_tutors(course)** - returns a list of tutors for a course

**get_course_tutors()** - returns a dictionary of all the courses tutored and who tutors each one

**get_course_tutor_file()** - creates a file `out.csv` with a column of courses tutored now and a column of who is tutoring each one

##Libraries
Just `csv` right now to read and write *.csv files easier
