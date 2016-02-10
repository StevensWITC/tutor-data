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
            name = row[0]
            data[name]={}
            data[name]['sched']={}
            for x in range(6):
                data[name]['sched'][days[x]] = row[x+1]
            #print name + "    :    " + str(data[name]['sched'])
            data[name]['courses'] = row[8].split(", ")

    result  = {}
    """
        Loop through `data` and fill `result` with courses and who tutors them
    """
    for tutor in data:
        for course in data[tutor]['courses']:
            if not course in result:
                result[course] = {}
                result[course]['tutors'] = []
            result[course]['tutors'] += [tutor]
            result[course]['times'] = {}

    for course in result:
        for tutor in result[course]['tutors']:
            for day in data[tutor]['sched']:
                if not data[tutor]['sched'][day] == '':
                    if not day in result[course]['times']:
                        result[course]['times'][day] = []
                    result[course]['times'][day] += [ data[tutor]['sched'][day] ]

    with open('out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ 'Course', 'Tutors', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ])
        for course in sorted(result):
            cell1 = course
            cell2 = []
            for tutor in sorted(result[course]['tutors']):
                cell2 += [tutor]
            cell3 = ''
            cell4 = ''
            cell5 = ''
            cell6 = ''
            cell7 = ''
            cell8 = ''
            if 'Sunday' in result[course]['times']:
                cell3 = result[course]['times']['Sunday']
            if 'Monday' in result[course]['times']:
                cell4 = result[course]['times']['Monday']
            if 'Tuesday' in result[course]['times']:
                cell5 = result[course]['times']['Tuesday']
            if 'Wednesday' in result[course]['times']:
                cell6 = result[course]['times']['Wednesday']
            if 'Thursday' in result[course]['times']:
                cell7 = result[course]['times']['Thursday']
            if 'Friday' in result[course]['times']:
                cell8 = result[course]['times']['Friday']
            writer.writerow([ cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8 ])


        #for day in result[course]['times']:
        #    print "    " + day + str(result[course]['times'][day])


