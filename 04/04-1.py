smallest_so_far = None
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
print('[9,41,12,3,74,15], the minimum value is:', smallest_so_far)