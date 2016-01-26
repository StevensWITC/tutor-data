# tutor-data
Some scripts to run on the tutor data to work with the data easier

##Plans
All tutor info except hours are on a spreadsheet right now. The class, or maybe a seperate script will pull info from that file, put it in class objects, then save to another file, probably `tutors.dat` through pickle.

There will be getters and setters for everything.

Courses can be stored as a list, I think hours will be a dictionary, with a tuple of 0s, 1s, or 0.5s, to show if they are working that hour of that day. Another option would be to store start and stop times. The only problem I see with that is if someone works more than once in one day, but then it could just be another level of dictionary to show multiple shifts.

This will be used mainly for stuff like generating the list of tutors for each course, and when to go to the center for a certain course. This could even be a little flask app to query the database eventually.

There should also be a method to "pretty print" everything, and maybe some more for just one tutor, course, or day.

##Libraries
Probably just `os` and `pickle`, unless this becomes a flask thing eventually.
