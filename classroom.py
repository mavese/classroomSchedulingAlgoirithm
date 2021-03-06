#Matthew Mantese
# Implementation of interval partitioning algorithm
import datetime
from heapq import heappush, heappop, heapify

def scheduleRooms(rooms,cls):
    """
    Input: rooms - list of available rooms
           cls   - dictionary mapping class names to pair of (start,end) times
    Output: Return a dictionary mapping the room name to a list of 
    non-conflicting scheduled classes. 
    If there are not enough rooms to hold the classes, return 'Not enough rooms'.
    """
    rmassign = {}
    #get a sorted list based on start time
    classList = list(sorted(cls,key=cls.get, reverse=True))   
    #create priority queue
    pQ = []
    #set boolean value empty to false to use to find difference between not enough rooms and normal ending loop
    empty = False
    heapify(pQ)
    for i in xrange(len(cls)):
        if empty:
            break
        clss = classList.pop()
        #short circuiting and so it doesn't give error when run for the first time. ie order matters for this statement
        if len(pQ) != 0 and pQ[0][0] <= cls[clss][0]:
            room = heappop(pQ)[1]
            rmassign[room].append(clss)
            heappush(pQ, [cls[clss][1], room])
        else:
            #if there are no more rooms but still classes left to place
            if(len(rooms) is 0): 
                empty = True
                continue
            room = rooms.pop()
            heappush(pQ, [cls[clss][1], room])
            rmassign[room] = [clss]
    if empty:
        return "Not enough rooms"           
    return rmassign

if __name__=="__main__":
    cl1 = {"a": (datetime.time(9),datetime.time(10,30)),
           "b": (datetime.time(9),datetime.time(12,30)),
           "c": (datetime.time(9),datetime.time(10,30)),
           "d": (datetime.time(11),datetime.time(12,30)),
           "e": (datetime.time(11),datetime.time(14)),
           "f": (datetime.time(13),datetime.time(14,30)),
           "g": (datetime.time(13),datetime.time(14,30)),
           "h": (datetime.time(14),datetime.time(16,30)),
           "i": (datetime.time(15),datetime.time(16,30)),
           "j": (datetime.time(15),datetime.time(16,30))}
    rm1 = [1,2,3]
    print cl1
    print scheduleRooms(rm1,cl1)
    print scheduleRooms([1,2],cl1)
    ensrooms = ['KEH U1','KEH M1','KEH M2','KEH M3','KEH U2','KEH U3','KEH U4','KEH M4','KEH U8','KEH U9']
    csclasses = {'CS 1043': (datetime.time(9,30),datetime.time(11)),
              'CS 2003': (datetime.time(10,30),datetime.time(12)),
              'CS 2123': (datetime.time(11,15),datetime.time(12,45)),
              'CS 3003': (datetime.time(8,15),datetime.time(11,30)),
              'CS 3353': (datetime.time(11),datetime.time(12)),
              'CS 4013': (datetime.time(13),datetime.time(14,45)),
              'CS 4063': (datetime.time(12,30),datetime.time(14,30)),
              'CS 4123': (datetime.time(14),datetime.time(15)),
              'CS 4163': (datetime.time(14),datetime.time(16,30)),
              'CS 4253': (datetime.time(12),datetime.time(16)),
    }
    print csclasses
    print scheduleRooms(ensrooms,csclasses)
    print scheduleRooms(ensrooms[:4],csclasses)
