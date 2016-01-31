'''
Class to represent courses for the course info page on sitstuff
'''
import os
import pickle

def file_name():
    return 'courses.dat'

def remove_spaces(my_str):
    """Remove the spaces from the end of a string"""
    if(my_str == ""):
        return ""
    if(my_str[-1] == " "):
        return remove_spaces(my_str[:-1])
    else:
        return my_str

def load_data():
    """Loads the data from .dat file... get it? dat file? No? Okay..."""
    my_dir = os.path.dirname(__file__)
    file_path = os.path.join(my_dir, file_name() )
    try:
        with open(file_path) as f:
            data = pickle.load(f)
    except:
        data = []
    return data

def save_data(data):
    """Saves the data to the .dat file"""
    my_dir = os.path.dirname(__file__)
    file_path = os.path.join(my_dir, file_name() )
    with open(file_path, "wb") as f:
        pickle.dump(data, f)

class Tutor:

    def __init__(self, first, last, courses, schedule):
        self._first = first
        self._last = last
        self._courses = courses
        self._sched = schedule

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

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

    @courses.setter
    def courses(self, courses):
        self._courses = courses

    @sched.setter
    def sched(self, sched):
        self._sched = sched

    # output stuff
    def __str__(self):
        info = "{Courses:" + self._courses + "}{Schedule:" + self._sched + "}"
        resp = "<" + self._first + " " + self._last + ":" + info + ">"
        return resp

    def __repr__(self):
        info = "{Courses:" + self._courses + "}{Schedule:" + self._sched + "}"
        resp = "<" + self._first + " " + self._last + ":" + info + ">"
        return resp

def buildDB(filename):
    """Takes the data from a .csv file and puts it into the tutor objects"""
    my_dir = os.path.dirname(__file__)
    file_path = os.path.join(my_dir, filename )
    try:
        with open(file_path) as f:
            data = pickle.load(f)
    except:
        data = []
    for row in data:
        for cell in row:
            print cell

if __name__ == '__main__':
    buildDB("tutors.csv")
