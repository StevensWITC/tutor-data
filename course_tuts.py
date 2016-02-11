import csv
if __name__ == '__main__':
    data = {}
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    """
        Parse the csv file and fill `data` with the info
    """
    with open('tutors.csv', 'rb') as f:
        csv_read = csv.reader(f, delimiter=",")
        for row in csv_read:
            temp_arr = row[0].split(', ')
            name = temp_arr[1] + " " + temp_arr[0]
            data[name]={}
            data[name]['sched']={}
            #loop through the schedule cells and fill `data[name]['sched']` with the key:value pair of day_of_week:hours
            for x in range(6):
                data[name]['sched'][days[x]] = row[x+1]
            #`courses` is a list of the courses a tutor tutors
            data[name]['courses'] = row[8].split(", ")

    result  = {}
    """
        Loop through `data` and fill `result` with courses and who tutors them
    """
    for tutor in data:
        #for each course a tutor tutors
        for course in data[tutor]['courses']:
            #if it's not in the result yet add the course
            if not course in result:
                result[course] = {}
                result[course]['tutors'] = []
            #add the tutor to the list of tutors for the course, now as 'first last'
            result[course]['tutors'] += [tutor]
            #initialize a dictionary to store the times the course is tutored each day
            result[course]['times'] = {}

    """
        Loop through the tutors for each course, and add the times they'll be in the center to the result dictionary
    """
    for course in result:
        for tutor in result[course]['tutors']:
            for day in data[tutor]['sched']:
                if not data[tutor]['sched'][day] == '':
                    if not day in result[course]['times']:
                        result[course]['times'][day] = []
                    if not data[tutor]['sched'][day] in result[course]['times'][day]:
                        result[course]['times'][day] += [ data[tutor]['sched'][day] ]

    with open('out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        #write some row headers
        writer.writerow([ 'Course', 'Tutors', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ])
        #loop through all courses, each course will be a row on the csv
        for course in sorted(result):
            cell1 = course
            cell2 = []
            for tutor in sorted(result[course]['tutors']):
                cell2 += [tutor]
            #initialize cells to be empty in case there isn't anyone there for that day
            cell3 = ''
            cell4 = ''
            cell5 = ''
            cell6 = ''
            cell7 = ''
            cell8 = ''

            ###################################################
            ## TODO: Take the sorted list and put it through a
            ## function or something to look at each element.
            ## If the first number of the second one is bigger
            ## than the second of the first, they can be
            ## combined. Edge cases with 10/11/12
            ###################################################

            ###################################################
            ## Another idea: I could get the names for all the
            ## courses by using web.stevens.edu/sit/courses/
            ## ?courseID=<AA>%20<###> then parsing the page for
            ## the name of the course
            ###################################################

            #Fill the cells with the sorted times
            if 'Sunday' in result[course]['times']:
                cell3 = sorted(result[course]['times']['Sunday'])
            if 'Monday' in result[course]['times']:
                cell4 = sorted(result[course]['times']['Monday'])
            if 'Tuesday' in result[course]['times']:
                cell5 = sorted(result[course]['times']['Tuesday'])
            if 'Wednesday' in result[course]['times']:
                cell6 = sorted(result[course]['times']['Wednesday'])
            if 'Thursday' in result[course]['times']:
                cell7 = sorted(result[course]['times']['Thursday'])
            if 'Friday' in result[course]['times']:
                cell8 = sorted(result[course]['times']['Friday'])
            #write the row with all the info
            writer.writerow([ cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8 ])


        #for day in result[course]['times']:
        #    print "    " + day + str(result[course]['times'][day])


