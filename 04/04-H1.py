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
for i in range(len(a)):
    a[i] = int(a[i])

"-----------------------------------------------------------------------------------------"

def my_sample_variance(x):
    total = 0
    for xi in x:
        total = total + (xi - my_average(x)) ** 2 
    return total/(len(x)-1)

print('the sample variance of dataset is:', my_sample_variance(a))
