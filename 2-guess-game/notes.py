import random

start = -5
stop = 11

# akan memberikan angka random dari -5 -- 10 (11 tidak termasuk)
print(random.randrange(start, stop))

# akan memberikan angka random dari -5 -- 11 (11 termasuk)
print(random.randint(start, stop))

#  akan memberikan angka random dari 0 - 11
print(random.randint(0,stop))