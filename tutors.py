"""
Class to represent courses for the course info page on sitstuff
"""

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
        #changed this for now because sched_parse needs to be updated for the new time format
        self._sched = sched#self.sched_parse(schedule)

    def sched_parse(self, inDict):
        for day in inDict:
            if not inDict[day] is '':
                #patting myself on the back because both of these lines worked first try. They take the day which is in the format "#pm - ##pm" and et just the numbers regardless of single or double digits
                start = inDict[day].split(" - ")[0][0:-2]
                end = inDict[day].split(" - ")[-1][0:-2]
                resp = start + " " + end
                inDict[day] = resp
        return inDict

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
        resp = "<Tutor name:{" + self._first + " " + self._last + "} sched:{" + str(self._sched) + "} courses:{" + str(self._courses) + "}>"
        return resp


class TutorScripts:

    def __init__(self, filename):
        self._filename = filename
        self._data = self.buildDB()

    @property
    def data(self):
        return self._data

    def buildDB(self):
        """
        Takes the data from a .csv file and puts it into the tutor objects
        """
        import csv
        fname = self._filename
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

    def get_tutored_courses(self):
        """
        Return a list of all courses tutored now
        data : list of 'Tutor's
        """
        tutored_courses = []
        for tutor in self._data:
            courses = tutor.courses
            for course in courses:
                if not course in tutored_courses and not course is '':#had to add the second part because it kept adding '' for some reason
                    tutored_courses += [course]
        return tutored_courses

    def get_tutors(self, course):
        """
        Return a list of all the tutors for a given course
        course : string
        """
        tutors = []
        for tutor in self._data:
            if course in tutor.courses:
                tutors += [str(tutor)]
        return tutors

    def get_course_tutors(self):
        """
        Returns a dictionary of all the courses tutored and who tutors them
        data : a lists of 'Tutor's
        """
        tutored_courses = self.get_tutored_courses()
        course_tutors = {}
        for course in tutored_courses:
            tutors = self.get_tutors(course)
            course_tutors[course] = tutors
        return course_tutors

    def get_course_tutor_file(self, filename):
        """
        Output a .csv file of courses and tutors for them
        """
        import csv
        course_tutors = self.get_course_tutors()
        with open(filename) as csvfile:
            writer = csv.writer(csvfile)
            for course in course_tutors:
                tutor_list = course_tutors[course][0]
                for tutor in course_tutors[course]:
                    tutor_list += ", " + tutor
                writer.writerow([course, tutor_list])


def parse_sched():
    """
    Takes the data from a .csv file and puts it into a dictionary
    """
    import csv
    fname = "sched.csv"
    data = {}
    with open(fname, 'rb') as f:
        csv_read = csv.reader(f, delimiter=",")
        count = 0
        day = "DAY_ERROR: Day not set yet"
        for row in csv_read:
            if not row[0] is '':
                day = row[0].split(" ")[0]
            name = row[1]
            if not name in data:
                data[name] = {}
            time = row[2]
            data[name][day] = time
    return data

def make_sched():
    """
    Output a .csv file of tutors and when they work
    """
    import csv
    sched = parse_sched()
    with open('sched_out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for tutor in sched:
            name = tutor.split(" ")[-1]
            s = ""
            m = ""
            t = ""
            w = ""
            r = ""
            f = ""
            for day in sched[tutor]:
                if day == "Monday":
                    m = sched[tutor][day]
                elif day == "Tuesday":
                    t = sched[tutor][day]
                elif day == "Wednesday":
                    w = sched[tutor][day]
                elif day == "Thursday":
                    r = sched[tutor][day]
                elif day == "Friday":
                    f = sched[tutor][day]
                elif day == "Sunday":
                    s = sched[tutor][day]
                else:
                    m = t = w = r = f = s = "ERROR"
            writer.writerow([name, m, t, w, r, f, s])

def proc_day(day):
    if not day is '':
        start = day.split('-')[0]
        end = day.split('-')[-1]
        if len(start) < 3:
            start = start + ":00"
        if len(end) < 3:
            end = end + ":00"
        day = start + '-' + end
        return day
    return ''

def proc_days(day_arr):
    for day in day_arr:
        day = proc_day(day)
    return day_arr


def fix_times(in_file, out_file):
    """
    Takes the data from the .csv file and reformats time from #-# to ##:##-##:##
    """
    import csv
    data = []
    with open(in_file, 'rb') as i_f:
        csv_read = csv.reader(i_f, delimiter=",")
        with open(out_file, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            count = 0
            for row in csv_read:
                day_arr = proc_days(row[1:7])
                print row[0], day_arr[0], day_arr[1], day_arr[2], day_arr[3], day_arr[4], day_arr[5], row[7], row[8]
                #writer.writerow( [row[0], day_arr[0], day_arr[1], day_arr[2], day_arr[3], day_arr[4], day_arr[5]], row[7], row[8] ])


if __name__ == '__main__':
    ###########################################################
    import time                                              ##
    start_time = time.time()                                 ##
    ###########################################################

    #ts = TutorScripts("tutors.csv")

    #for tutor in ts.data:
    #    print tutor
    #    print "    " + str(tutor.courses)
    #    print "    " + str(tutor.sched)

    #ts.get_course_tutor_file("out.csv")

    #sched = parse_sched()
    #for tutor in sched:
    #    print tutor
    #    for day in sched[tutor]:
    #        print "    " + day + ":" + sched[tutor][day]

    #make_sched()

    fix_times("tutors.csv", "out.csv")

    ###########################################################
    print "Run time: ", time.time() - start_time, " seconds" ##
    ###########################################################
