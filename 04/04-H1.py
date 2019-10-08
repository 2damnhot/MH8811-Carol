def my_min(x):
    smallest_so_far = None
    for the_num in x:
        if smallest_so_far is None:
            smallest_so_far = the_num
            continue
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far

def my_max(x):
    largest_so_far = None
    for the_num in x:
        if largest_so_far is None:
            largest_so_far = the_num
            continue
        elif the_num > largest_so_far:
            largest_so_far = the_num
    return largest_so_far

def my_median(x):
    x.sort()
    for the_num in x:
        if len(x) % 2 != 0:
            r=int(len(x)/2)
            median = x[r]
        if len(x) % 2 == 0:
            r=int(len(x)/2)
            median = (x[r]+x[r-1])/2
    return median

def my_average(x):
    total = 0
    for the_num in range(0, len(x)):
        total = total + x[the_num]
    ave = total/len(x)
    return ave

def my_range(x):
    ran = my_max(x) - my_min(x)
    return ran

def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            lines.append(line)
    return lines

a = getFileLines('MH8811-04-Data.csv')
for i in range(len(a)):
    a[i] = int(a[i])

"-----------------------------------------------------------------------------------------"

def my_sample_variance(x):
    total = 0
    for xi in x:
        total = total + (xi - my_average(x)) ** 2 
    return total/(len(x)-1)

print('Here are the descriptive statistics for the file:\n', 
'min is:',my_min(a),'\n'
'max is:',my_max(a),'\n'
'average is:',my_average(a),'\n'
'median is:',my_median(a),'\n'
'range is:',my_range(a),'\n'
'sample variance is:',my_sample_variance(a))
