#importing module
import numpy as np
#list of names with priority
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", \
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",\
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",\
                 "E Sue"]
#Created containers for entries in input_packets that organize by letter in index 0
queue_premium = []
queue_standard = []
queue_economy = []
for x in input_packets:
    if x[0] == "P":
        queue_premium.append(x)
    if x[0] == "S":
        queue_standard.append(x)
    if x[0] == "E":
        queue_economy.append(x)
#updated list after the sort
print('Updated queue_premium list:', queue_premium)
print('Updated queue_standard list:', queue_standard)
print('Updated queue_economy list:', queue_economy)
#I'm not exactly sure where to start with the queue. I thought I watched a video online describing it better but cant for the life of me find it now.
