def my_average(x):
    total = 0
    for the_num in range(0, len(x)):
        total = total + x[the_num]
    ave = total/len(x)
    return ave

def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            lines.append(line)
    return lines

a = getFileLines('MH8811-04-Data.csv')
lst = list(map(int, a))

"-----------------------------------------------------------------------------------------"

def my_sample_variance(x):
    var = sum((xi - my_average(x)) ** 2 for xi in x) / (len(x)-1)
    return var

print('the sample variance of dataset is:', my_sample_variance(lst))
