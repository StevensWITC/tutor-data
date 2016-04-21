import csv

#Some good data to test with
#Now I don't have to deal with the 30 minute times though!
times = [['5-7', '6-9', '8-11', '9-11'],\
    ['2-4', '4-7', '6-8', '7-9', '9-11'],\
    ['2-4', '3-5', '4-6', '7-9', '9-11'],\
    ['2-4', '4-6', '4-7', '7-9', '9-11'],\
    ['2-4', '2-5', '4-7', '6-8', '7-9', '9-11'],\
    ['1-3', '12-2', '2-5', '3-5']]
times2 = [['5-7', '7-9', '8-11', '9-11'],\
    ['2-4', '3-5', '4-6', '4-7', '6-8', '6-9', '7-9', '9-11'],\
    ['2-4', '3-6', '4-6', '5-7', '6-9', '7-9', '9-11'],\
    ['4-6', '4-7', '5-7', '7-9', '9-11'],\
    ['2-4', '2-5', '4-6', '4-7', '5-7', '6-8', '7-9', '9-11'],\
    ['1-3', '12-2', '2-5', '3-5']]

def convert_time_24(time):
    """
    Given a number, convert to 24 H unless it's the hour 12
    """
    if not time == "12":
        time = str(int(time) + 12)
    return time
def convert_time_12(time):
    """
    Given a number, convert to 12 H unless its the hour 12-2
    """
    if not time == "12":
        time = str(int(time)-12)
    return time
def convert_times_24(lst):
    """
    Take a list of time periods in 12H format and covnert to 24H
    """
    for t_period in lst:
        times = t_period.split('-')#get a 2-element array of the start and end of the time period
        for time in times:#for both the start and end...
            times[times.index(time)] = convert_time_24(time)
        lst[lst.index(t_period)] = times[0] + '-' + times[1]
    return lst
def convert_times_12(lst):
    """
    Take a list of time periods in 24H format and convert to 12H
    """
    for t_period in lst:
        times = t_period.split('-')#get a 2-element array of the start and end of the time period
        for time in times:#for both the start and end...
            times[times.index(time)] = convert_time_12(time)
        lst[lst.index(t_period)] = times[0] + '-' + times[1]
    return lst
def combine_times_24(lst):
    """
        Take a list of times that may not be in order, convert to 24H
        Then sort elements and combine as many as possible
    """
    for t_period in sorted(convert_times_24(lst)):
        print t_period
    print "---"

def consolidate(lst):
    """
    Given a list of time periods, return the list of the consolidated times
    """
    lst = convert_times_24(lst)
    start = lst[0].split("-")[0]
    end = lst[0].split("-")[-1]
    resp = []
    for x in range(1, len(lst)):
        if len(lst) == 1:
            return convert_times_12(lst)
        if lst[x].split("-")[0] <= end:#we can include this
            end = lst[x].split("-")[-1]
            if x+1 == len(lst):#if it's the end then add the last part
                new = start + "-" + end
                resp = resp + [new]
        else:#time to make a new one
            new = start + "-" + end
            resp = resp + [new]
            start = lst[x].split("-")[0]
            end = lst[x].split("-")[-1]
    return convert_times_12(resp)

def run():
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
                cell3 = consolidate(sorted(result[course]['times']['Sunday']))
            if 'Monday' in result[course]['times']:
                cell4 = consolidate(sorted(result[course]['times']['Monday']))
            if 'Tuesday' in result[course]['times']:
                cell5 = consolidate(sorted(result[course]['times']['Tuesday']))
            if 'Wednesday' in result[course]['times']:
                cell6 = consolidate(sorted(result[course]['times']['Wednesday']))
            if 'Thursday' in result[course]['times']:
                cell7 = consolidate(sorted(result[course]['times']['Thursday']))
            if 'Friday' in result[course]['times']:
                cell8 = consolidate(sorted(result[course]['times']['Friday']))
            #write the row with all the info
            writer.writerow([ cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8 ])


        #for day in result[course]['times']:
        #    print "    " + day + str(result[course]['times'][day])


if __name__ == '__main__':
    run()
#    for time in times:
#        #combine_times(time)
#        print time
#        print consolidate(time)
#        print "---"
