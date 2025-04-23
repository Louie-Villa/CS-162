#defining functions
def dequeue_premium():
    dequeue_premium_counter = 0
    while dequeue_premium_counter < 3:
        element1 = queue_premium.pop(0)
        print("Dequeue: ", element1)
        dequeue_premium_counter += 1
    if len(queue_premium) ==0:
        print("Queue_Premium is empty")
def dequeue_standard():
    dequeue_standard_counter = 0
    while dequeue_standard_counter <2 :
        element1 = queue_standard.pop(0)
        print("Dequeue: ", element1)
        dequeue_standard_counter += 1
    if len(queue_standard) == 0:
        print("Queue_Standard is empty")

def dequeue_economy():
    dequeue_economy_counter = 0
    while dequeue_economy_counter < 1:
        element1 = queue_economy.pop(0)
        print("Dequeue: ", element1)
        dequeue_economy_counter += 1
    if len(queue_economy) == 0:
        print("Queue_Economy is empty")

#List of names with priority: "P,S,E"
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
#Updated list after the sort
print('Updated queue_premium list:', queue_premium, len(queue_premium))
print('Updated queue_standard list:', queue_standard, len(queue_standard))
print('Updated queue_economy list:', queue_economy, len(queue_economy))

# Dequeue functions
dequeue_premium()
dequeue_standard()
dequeue_economy()
dequeue_premium()
dequeue_standard()
dequeue_economy()
dequeue_premium()
dequeue_economy()
dequeue_economy()
dequeue_economy()
dequeue_economy()
dequeue_economy()
dequeue_economy()






