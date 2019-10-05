sample = [9,41,12,3,74,15]

def my_min(x):
    smallest_so_far = None
    for the_num in x:
        if smallest_so_far is None:
            smallest_so_far = the_num
            continue
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far

print(sample, 'the min is:', my_min(sample))

def my_max(x):
    largest_so_far = None
    for the_num in x:
        if largest_so_far is None:
            largest_so_far = the_num
            continue
        elif the_num > largest_so_far:
            largest_so_far = the_num
    return largest_so_far

print(sample, 'the max is:', my_max(sample))

def my_median(x):
    x.sort()
    for the_num in x:
        if len(x) % 2 != 0:
            r=int(len(x)/2)
            median = x[r]
        if len(x) % 2 == 0:
            r=int(len(x)/2)
            median = (x[r]+x[r+1])/2
    return median

def my_average(x):
    total = 0
    for the_num in range(0, len(x)):
        total = total + x[the_num]
    ave = total/len(x)
    return ave

print(sample, 'the average is:', my_average(sample))

def my_range(x):
    ran = my_max(x) - my_min(x)
    return ran








