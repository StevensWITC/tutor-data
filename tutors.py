'''
Class to represent courses for the course info page on sitstuff
'''
import csv

class Tutor:

    def __init__(self, first, last, email, courses, schedule):
        """
        Constructor
        first : string
        last : string
        email : string
        courses : list
        schedule : dictionary
        """
        self._first = first
        self._last = last
        self._email = email
        self._courses = courses
        self._sched = schedule

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def email(self):
        return self._email


    @property
    def courses(self):
        return self._courses

    @property
    def sched(self):
        return self._sched

    @first.setter
    def first(self, first):
        self._first = first

    @last.setter
    def last(self, last):
        self._last = last

    @email.setter
    def email(self, email):
        self._email = email

    @courses.setter
    def courses(self, courses):
        self._courses = courses

    @sched.setter
    def sched(self, sched):
        self._sched = sched

    def __str__(self):
        return self._first + " " + self._last

    def __repr__(self):
        resp = "<Tutor name:{" + self._first + " " + self._last + "}>"
        return resp


################################################
#                                              #
#              [BELOW THIS POINT]              #
#   Scripts to create the tutor courses file   #
#                                              #
################################################
def buildDB():
    """
    Takes the data from a .csv file and puts it into the tutor objects
    """
    fname = "tutors.csv"
    data = []
    with open(fname, 'rb') as f:
        csv_read = csv.reader(f, delimiter=",")
        count = 0
        for row in csv_read:
            name = row[0].split(", ")
            last = name[0]
            first = name[-1]

            sched = {}
            sched["m"] = row[1]
            sched["t"] = row[2]
            sched["w"] = row[3]
            sched["r"] = row[4]
            sched["f"] = row[5]
            sched["s"] = row[6]

            email = row[7]
            courses = row[8].split(", ")

            tutor = Tutor(first, last, email, courses, sched)
            data = data + [tutor]
    return data

def get_tutored_courses(data):
    """
    Return a list of all courses tutored now
    data : list of 'Tutor's
    """
    tutored_courses = []
    for tutor in data:
        courses = tutor.courses
        for course in courses:
            if not course in tutored_courses and not course is '':#had to add the second part because it kept adding '' for some reason
                tutored_courses += [course]
    return tutored_courses

def get_tutors(course, data):
    """
    Return a list of all the tutors for a given course
    course : string
    """
    tutors = []
    for tutor in data:
        if course in tutor.courses:
            tutors += [str(tutor)]
    return tutors

def get_course_tutors(data):
    """
    Returns a dictionary of all the courses tutored and who tutors them
    data : a lists of 'Tutor's
    """
    tutored_courses = get_tutored_courses(data)
    course_tutors = {}
    for course in tutored_courses:
        tutors = get_tutors(course, data)
        course_tutors[course] = tutors
    return course_tutors

def get_course_tutor_file():
    """
    Output a .csv file of courses and tutors for them
    """
    data = buildDB()
    course_tutors = get_course_tutors(data)
    with open('out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for course in course_tutors:
            tutor_list = course_tutors[course][0]
            for tutor in course_tutors[course]:
                tutor_list += ", " + tutor
            writer.writerow([course, tutor_list])


if __name__ == '__main__':
    get_course_tutor_file()
